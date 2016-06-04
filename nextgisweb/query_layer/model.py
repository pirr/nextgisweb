# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

import re

from zope.interface import implements

from nextgisweb.feature_layer import IFeatureLayer, LayerFieldsMixin
from nextgisweb.models import declarative_base
from nextgisweb.resource import (
    Resource,
    ResourceScope,
    DataScope, DataStructureScope,
    Serializer,
    SerializedProperty as SP)
from nextgisweb import db

# from antlr4 import InputStream, CommonTokenStream

# from .grammar.CQLParser import CQLParser
# from .grammar.CQLLexer import CQLLexer
from .util import _

Base = declarative_base()


class QueryLayer(Base, Resource, LayerFieldsMixin):
    identity = 'query_layer'
    cls_display_name = _("Query layer")

    __scope__ = (DataScope, DataStructureScope)

    implements(IFeatureLayer)

    cql = db.Column(db.Unicode, nullable=False)
    flist = db.Column(db.Unicode, nullable=True)

    @classmethod
    def check_parent(cls, parent):
        return parent.cls in ('vector_layer', 'postgis_layer')

    # IFeatureLayer

    @property
    def fields(self):
        return self.parent.fields

    @property
    def geometry_type(self):
        return self.parent.geometry_type

    def feature_query(self, **kwargs):
        request = kwargs.get('request')
        query = self.parent.feature_query()

        if self.flist:
            query.fields(*self.flist.split(","))

        if self.cql:
            m = re.match(r'^(.*)=(.*)$', self.cql)
            if m:
                field, value = m.groups()
                value = value.replace("{{login}}", request.user.keyname)
                query.filter_by(**{field: value})

        return query

    # ??
    @property
    def feature_label_field_id(self):
        return self.parent.feature_label_field_id

    # ??
    @property
    def feature_label_field(self):
        return self.parent.feature_label_field

    # ??
    @feature_label_field.setter
    def feature_label_field(self, val):
        self.parent.feature_label_field = val


class _srs_attr(SP):

    def getter(self, srlzr):
        return dict(id=srlzr.obj.parent.srs_id)


class _geometry_type_attr(SP):

    def getter(self, srlzr):
        return srlzr.obj.parent.geometry_type


PR_READ = ResourceScope.read
PR_UPDATE = ResourceScope.update


class QueryLayerSerializer(Serializer):
    identity = QueryLayer.identity
    resclass = QueryLayer

    cql = SP(read=PR_READ, write=PR_UPDATE)
    flist = SP(read=PR_READ, write=PR_UPDATE)
    srs = _srs_attr(read=PR_READ)
    geometry_type = _geometry_type_attr(read=PR_READ)
