/* globals define, console */
define([
    "dojo/_base/declare",
    "dijit/layout/ContentPane",
    "dijit/_TemplatedMixin",
    "dijit/_WidgetsInTemplateMixin",
    "ngw-pyramid/i18n!query_layer",
    "ngw-pyramid/hbs-i18n",
    "ngw-resource/serialize",
    "dojo/text!./template/Widget.hbs",
    // template
    "dijit/Dialog",
    "dijit/layout/BorderContainer",
    "ngw-pyramid/form/CodeMirror"
], function (
    declare,
    ContentPane,
    _TemplatedMixin,
    _WidgetsInTemplateMixin,
    i18n,
    hbsI18n,
    serialize,
    template
) {
    return declare([ContentPane, serialize.Mixin, _TemplatedMixin, _WidgetsInTemplateMixin], {
        templateString: hbsI18n(template, i18n),
        prefix: "query_layer",
        title: "CQL"
    });
});
