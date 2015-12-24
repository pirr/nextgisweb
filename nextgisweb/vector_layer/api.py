# -*- coding: utf-8 -*-
import json

import sqlalchemy.sql as sql
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound

from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from pyramid.response import Response

from .model import VectorLayer
from ..models import DBSession
from ..resource import DataScope
from ..feature_layer.api import serialize

from .util import _

from .. import db


PERM_READ = DataScope.read
PERM_WRITE = DataScope.write


def diff(request):

    try:
        obj = VectorLayer.filter_by(id=request.matchdict['id']).one()
    except NoResultFound:
        raise HTTPNotFound()
    
    request.resource_permission(PERM_READ, obj)

    ts = request.GET.get('ts')
    tag = request.GET.get('tag')

    tracked = obj.tracked
    if not tracked:
        raise HTTPBadRequest(_("Tracking history is not enabled for this layer"))

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
        
        op_lookup = {}
        c_ids = []
        u_ids = []
        d_ids = []
        for id, op in track:
            op_lookup[id] = op
            if op == '+':
                c_ids.append(id)
            elif op == ':':
                u_ids.append(id)
            elif op == '-':
                d_ids.append(id)

        if not (c_ids or u_ids):
            result = []
        else:
            query = obj.feature_query()
            query.in_(id=(c_ids + u_ids))
            query.geom()

            features = map(serialize, query())

            result = dict(added=[], changed=[])
            for feat in features:
                if feat.get('id') in c_ids:
                    result.get("added").append(feat)
                elif feat.get('id') in u_ids:
                    result.get("changed").append(feat)

            result["deleted"] = d_ids

    except exc.SQLAlchemyError as e:
        raise HTTPBadRequest(e.message)


    return Response(
        json.dumps(result),
        content_type=b'application/json')

def setup_pyramid(comp, config):
    config.add_route(
        'vector_layer.diff',
        '/api/vector_layer/{id}/diff/') \
        .add_view(diff, request_method='GET')
