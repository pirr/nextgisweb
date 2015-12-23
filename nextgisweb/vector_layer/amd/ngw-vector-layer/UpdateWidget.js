define([
    "dojo/_base/declare",
    "dojo/Deferred",
    "dojo/when",
    "dijit/_TemplatedMixin",
    "dijit/_WidgetsInTemplateMixin",
    "dijit/layout/ContentPane",
    "ngw-pyramid/i18n!vector_layer",
    "ngw-pyramid/hbs-i18n",
    "ngw-resource/serialize",
    // resource
    "dojo/text!./template/UpdateWidget.hbs",
    // template
    "dojox/layout/TableContainer",
    "dijit/form/CheckBox"
], function (
    declare,
    Deferred,
    when,
    _TemplatedMixin,
    _WidgetsInTemplateMixin,
    ContentPane,
    i18n,
    hbsI18n,
    serialize,
    template
) {
    return declare([ContentPane, serialize.Mixin, _TemplatedMixin, _WidgetsInTemplateMixin], {
        templateString: hbsI18n(template, i18n),
        title: i18n.gettext("Vector layer"),
        prefix: "vector_layer"
    });
});
