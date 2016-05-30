# -*- coding: utf-8 -*-
from ..component import Component
from .model import Base, QueryLayer

__all__ = ['QueryLayer', ]


class QueryLayerComponent(Component):
    identity = 'query_layer'
    metadata = Base.metadata

    def setup_pyramid(self, config):
        from . import view # NOQA
