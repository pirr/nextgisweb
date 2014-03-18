# -*- coding: utf-8 -*-
import sqlalchemy as sa
import sqlalchemy.orm as orm

from ..models import declarative_base
from ..layer import Layer
from ..file_storage import FileObj

Base = declarative_base()


class FeaturePhoto(Base):
    __tablename__ = 'feature_photo'

    id = sa.Column(sa.Integer, primary_key=True)
    layer_id = sa.Column(sa.ForeignKey(Layer.id), nullable=False)
    feature_id = sa.Column(sa.Integer, nullable=False)
    fileobj_id = sa.Column(sa.ForeignKey(FileObj.id), nullable=False)

    fileobj = orm.relationship(FileObj)

    layer = orm.relationship(
        Layer,
        backref=orm.backref('__feature_photo', cascade='all')
    )