# -*- coding: utf-8 -*-
from ..component import Component, require
from .model import Base, QueryLayer

__all__ = ['QueryLayer', ]


class QueryLayerComponent(Component):
    identity = 'query_layer'
    metadata = Base.metadata

    @require('feature_layer')
    def setup_pyramid(self, config):
        from . import view # NOQA
