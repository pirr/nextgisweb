# -*- coding: utf-8 -*-
import json
import urllib2

from ..component import Component, require

from .models import Base, FeaturePhoto

__all__ = ['FeaturePhotoComponent', 'FeaturePhoto']


@Component.registry.register
class FeaturePhotoComponent(Component):
    identity = 'feature_photo'
    metadata = Base.metadata

    @require('feature_layer', 'file_storage')
    def initialize(self):
        FeatureExtension = self.env.feature_layer.FeatureExtension

        @FeatureExtension.registry.register
        class FeaturePhotoExtension(FeatureExtension):
            identity = 'feature_photo'
            display_widget = 'feature_photo/DisplayWidget'

            comp = self

            def feature_data(self, feature):

                # Для проекта по Красногорску используется внешний сервис
                # доступа к фотографиям
                base_url = self.comp.settings['url']

                table = self.layer.table
                feature = feature.id

                query = "%s/%s/%s/images/" % (base_url, table, feature)
                images = json.loads(urllib2.urlopen(query).read())['images']

                if len(images) > 0:
                    return map(lambda image: image['id'], images)

            @property
            def feature_widget(self):
                class _Widget(self.comp.FeaturePhotoEditWidget):
                    layer = self.layer

                return _Widget

    def setup_pyramid(self, config):
        from . import views
        views.setup_pyramid(self, config)
