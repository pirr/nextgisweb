define([
    "dojo/_base/declare",
    "dojo/on",
    "dojo/dom-construct",
    "dojo/_base/lang",
    "dojox/image/Lightbox"
], function(
    declare,
    on,
    domConstruct,
    lang,
    Lightbox
) {
    return declare(dojox.image.LightboxDialog, {

        startup: function() {
            on(this.fullScreenButtonNode, "click", lang.hitch(this, this._fullScreenImage));
            this.inherited(arguments);
        },

        _fullScreenImage: function() {
            window.open(this.imgNode.src);
        },

        buildRendering: function() {
            this.inherited(arguments);
            this.fullScreenButtonNode = domConstruct.create("div", {
                "class": "dijitInline LightboxFullScreen"
            }, this.titleNode, 2);
        }
    });
});