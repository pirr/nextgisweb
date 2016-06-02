/* globals define, console */
define([
    "dojo/_base/declare",
    "dijit/_TemplatedMixin",
    "dijit/_WidgetBase",
    "dijit/_WidgetsInTemplateMixin",
    "ngw-pyramid/i18n!query_layer",
    "ngw-pyramid/hbs-i18n",
    "ngw-resource/serialize",
    "dojo/text!./template/Widget.hbs",
    // template
    "dijit/form/TextBox",
    "dojox/layout/TableContainer",
    "dijit/layout/BorderContainer"
], function (
    declare,
    _TemplatedMixin,
    _WidgetBase,
    _WidgetsInTemplateMixin,
    i18n,
    hbsI18n,
    serialize,
    template
) {
    return declare([_WidgetBase, _TemplatedMixin, _WidgetsInTemplateMixin, serialize.Mixin], {
        templateString: hbsI18n(template, i18n),
        serializePrefix: "query_layer",
        title: i18n.gettext("Query")
    });
});
