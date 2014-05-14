/*global console, define, require, OpenLayers, ngwConfig*/
define([
    "dojo/_base/declare",
    "./Base",
    "dojo/_base/lang",
    "dojo/_base/array",
    "dojo/json",
    "dojo/io-query",
    "dojo/request/xhr",
    "dojo/dom-style",
    "dojo/on",
    "dijit/layout/BorderContainer",
    "dijit/layout/ContentPane",
    "dijit/form/Select",
    "ngw/openlayers",
    "ngw/openlayers/Popup",
    "put-selector/put",
    // settings
    "ngw/settings!webmap",
    // css
    "xstyle/css!./resources/Identify.css",
    "xstyle/css!./resources/FieldsDisplayWidget.css"
], function (
    declare,
    Base,
    lang,
    array,
    json,
    ioQuery,
    xhr,
    domStyle,
    on,
    BorderContainer,
    ContentPane,
    Select,
    openlayers,
    Popup,
    put,
    webmapSettings
) {

    var Control = OpenLayers.Class(OpenLayers.Control, {
        initialize: function (options) {
            OpenLayers.Control.prototype.initialize.apply(this, [options]);

            this.handler = new OpenLayers.Handler.Click(this, {
                click: this.clickCallback
            });
        },

        clickCallback: function (evt) {
            this.tool.execute([evt.xy.x, evt.xy.y]);
        }
    });

    var Widget = declare([BorderContainer], {
        style: "width: 100%; height: 100%",
        gutters: false,

        postCreate: function() {
            this.inherited(arguments);

            this.selectOptions = [];

            array.forEach(this.response, function(item, idx) {
                this.selectOptions.push({
                    label: "#" + (item['Кадастровый номер'] || item['Кадастровый номер земельного участка'] || idx),
                    value: idx
                });
            }, this);

            this.selectPane = new ContentPane({
                region: "top",
                layoutPriority: 1,
                style: "padding: 0px 4px;"
            });
            this.addChild(this.selectPane);

            this.select = new Select({
                style: "width: 100%",
                options: this.selectOptions
            }).placeAt(this.selectPane);

            this.fieldsPane = new ContentPane({
                region: "center",
                style: "padding: 2px;"
            });
            this.addChild(this.fieldsPane);

        },

        startup: function() {
            this.inherited(arguments);

            var widget = this;
            this.select.watch("value", function (attr, oldVal, newVal) {
                 widget._displayFeature(widget.response[newVal]);
            });

            this._displayFeature(widget.response[this.select.get("value")]);
        },

        _displayFeature: function(feature) {
            var tbody,
                containerNode = this.fieldsPane.containerNode;

            containerNode.innerHTML = "";
            tbody = put(
                containerNode,
                "table.data.ngwFeatureLayer-fieldTable.ngwFeatureLayer-fieldTable-compact tbody"
            );

            array.forEach(Object.keys(feature), function(key) {
                put(tbody,
                    "tr th.display_name $ < td.value $",
                    key,
                    feature[key]
                )
            });
        }

    });


    return declare(Base, {
        label: "Идентификация WMS",

        iconClass: "iconIdentifyWMS",

        // Ширина popup
        popupWidth: webmapSettings.popup_width,

        // Высота popup,
        popupHeight: webmapSettings.popup_height,

        // Маппинг полей для ПКК
        _pkkFields: {
            "Кадастровыйномер": "Кадастровый номер",
            "Кадастровыйномерземельногоучастка": "Кадастровый номер земельного участка",
            "Датаактуальности": "Дата актуальности",
            "Датаактуальностиквартала": "Дата актуальности квартала",
            "Датаактуальностиучастков": "Дата актуальности участков",
            "Датаактуальностисведений": "Дата актуальности сведений",
            "Наименование": "Наименование",
            "Аннотация": "Аннотация",
            "Статусземельногоучасткакод": "Статус земельного участка",
            "Категорияземелькод": "Категория земель",
            "Видразрешенногоиспользованиякод": "Вид разрешенного использования",
            "Значениекадастровойстоимости": "Значение кадастровой стоимости",
            "ЧислоЗУ": "Число ЗУ",
            "ЧислоКК": "Число КК",
            "ЧислоКР": "Число КР"
        },

        constructor: function (options) {
            this.map = this.display.map;
            this.control = new Control({tool: this});
            this.display.map.olMap.addControl(this.control);
        },

        activate: function () {
            this.control.activate();
        },

        deactivate: function () {
            this.control.deactivate();
        },

        execute: function (pixel) {
            var tool = this,
                olMap = this.display.map.olMap,
                olMapDiv = olMap.div,
                olMapProjection = olMap.getProjectionObject(),
                lonlatProjection = new openlayers.Projection("EPSG:4326"),
                bbox = olMap.getExtent().transform(olMapProjection, lonlatProjection),
                point = olMap.getLonLatFromPixel(new OpenLayers.Pixel(pixel[0], pixel[1]));

            var request = {
                "x": pixel[0],
                "y": pixel[1],
                "bbox": bbox.toBBOX(),
                "width": domStyle.get(olMapDiv, "width"),
                "height": domStyle.get(olMapDiv, "height")
            };

            this.display.getVisibleItems().then(function(items) {
                if (items.length === 0) {
                    console.log("Visible items not found");
                } else {
                    request.styles = array.map(items, function(i) {
                        return this.display.itemStore.getValue(i, "styleId");
                    });

                    xhr.post(ngwConfig.applicationUrl + "/wmsclient/identify", {
                        handleAs: "json",
                        data: json.stringify(request)
                    }).then(function(response) {
                        if (response.data) {
                            // Предполагается, что инструмент идентификации WMS будет работать только с ПКК,
                            // поэтому фильтрацию полей прописываем в коде
                            array.forEach(response.data, function(item) {
                                array.forEach(Object.keys(item), function(key) {
                                    if (tool._pkkFields.hasOwnProperty(key)) {
                                        item[tool._pkkFields[key]] = item[key];
                                        if (tool._pkkFields[key] !== key) {
                                            delete item[key];
                                        }
                                    } else {
                                        delete item[key];
                                    }
                                });
                            });
                            tool._responsePopup(response.data, point);
                        } else {
                            // Ошибка получения данных с удалённого WMS-сервера
                            console.warn("Ошибка идентификации WMS:" + response.error);
                        }
                    });
                }
            });
        },

        _removePopup: function() {
            if (this._popup) {
                this._popup.widget.select.closeDropDown(true);
                this._popup.widget.destroyRecursive();
                this.map.olMap.removePopup(this._popup);
                this._popup = null;
            };
        },

        _responsePopup: function(response, point) {

            this._removePopup();

            this._popup = new Popup({
                title: "Идентификация WMS",
                point: point,
                size: [this.popupWidth, this.popupHeight]
            });

            var widget = new Widget({
                response: response,
                tool: this,
                popupSize: [this.popupWidth, this.popupHeight]
            });
            this._popup.widget = widget;

            widget.placeAt(this._popup.contentDiv).startup();

            this.map.olMap.addPopup(this._popup);
            widget.resize();

            // Обработчик закрытия
            on(this._popup._closeSpan, 'click', lang.hitch(this, function () {
                this._removePopup();
            }));

        }

    });
});