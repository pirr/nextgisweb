# -*- coding: utf-8 -*-
import json

import sqlalchemy.sql as sql
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound

from pyramid import httpexceptions
from pyramid.response import Response

from .model import VectorLayer
from ..models import DBSession
from ..resource import DataScope
from ..resource.exception import ValidationError
from ..feature_layer.api import serialize

from .util import _

from .. import db


PERM_READ = DataScope.read
PERM_WRITE = DataScope.write


def diff(request):

    try:
        obj = VectorLayer.filter_by(id=request.matchdict['id']).one()
    except NoResultFound:
        raise httpexceptions.HTTPNotFound()
    
    request.resource_permission(PERM_READ, obj)

    ts = request.GET.get('ts')
    tag = request.GET.get('tag')

    tracked = obj.tracked
    if not tracked:
        raise ValidationError(_("Tracking history is not enabled for this layer"))

    ts_func = "vector_layer.%s_Diff" % obj._tablename
    tag_func = "vector_layer.%s_DiffToTag" % obj._tablename
        
    if tag is not None:
        stmt = sql.text("SELECT id, operation FROM %s(:tag)" % tag_func,
                  bindparams=[sql.bindparam('tag', tag, type_=db.Integer)])

    elif ts is not None:
        stmt = sql.text("SELECT id, operation FROM %s(:ts)" % ts_func,
                  bindparams=[sql.bindparam('ts', ts, type_=db.DateTime)])

    else:
        stmt = sql.text("SELECT id, operation FROM %s()" % ts_func)

    try:
        track = DBSession.connection().execute(stmt)
        
        tracked_ids = []
        op_lookup = {}
        for id, op in track:
            op_lookup[id] = op
            tracked_ids.append(id)

        if not tracked_ids:
            result = []
        else:
            query = obj.feature_query()
            query.in_(id=tracked_ids)
            query.geom()

            result = map(serialize, query())

            for feat in result:
                feat["operation"] = op_lookup.get(feat.get('id'))

    except exc.SQLAlchemyError as e:
        raise ValidationError(e.message)


    return Response(
        json.dumps(result),
        content_type=b'application/json')

def setup_pyramid(comp, config):
    config.add_route(
        'vector_layer.diff',
        '/api/vector_layer/{id}/diff/') \
        .add_view(diff, request_method='GET')
