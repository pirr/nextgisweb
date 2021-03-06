/*global define, require*/
define([
    "dojo/_base/declare",
    "./Base",
    "openlayers/ol",
    "ngw-pyramid/i18n!webmap"
], function (
    declare,
    Base,
    ol,
    i18n
) {
    return declare(Base, {
        out: false, 

        constructor: function (options) {
            if (!this.out) {
                this.label = i18n.gettext("Zoom in");
                this.iconClass = "iconZoomIn";
            } else {
                this.label = i18n.gettext("Zoom out");
                this.iconClass = "iconZoomOut";
            };

            this.interaction = new ol.interaction.DragZoom({
                condition: ol.events.condition.always,
                out: this.out
            });
            this.interaction.setActive(false);
            this.display.map.olMap.addInteraction(this.interaction);
        },

        activate: function () {
            this.interaction.setActive(true);
        },

        deactivate: function () {
            this.interaction.setActive(false);
        }

    });
});
