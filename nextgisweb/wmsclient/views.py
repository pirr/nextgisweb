# -*- coding: utf-8 -*-
import urllib
import urllib2

from lxml import etree

from ..object_widget import ObjectWidget

from .models import WMSClientLayer, WMSClientStyle


class WMSClientLayerObjectWidget(ObjectWidget):

    def is_applicable(self):
        return self.operation in ('create', 'edit')

    def populate_obj(self):
        ObjectWidget.populate_obj(self)
        self.obj.url = self.data['url']
        self.obj.version = self.data['version']
        self.obj.srs_id = self.data['srs_id']

    def widget_params(self):
        result = ObjectWidget.widget_params(self)

        if self.obj:
            result['value'] = dict(
                url=self.obj.url,
                version=self.obj.version,
                srs_id=self.obj.srs_id,
            )

        return result

    def widget_module(self):
        return 'wmsclient/LayerWidget'


class WMSClientStyleObjectWidget(ObjectWidget):

    def is_applicable(self):
        return self.operation in ('create', 'edit')

    def populate_obj(self):
        ObjectWidget.populate_obj(self)
        self.obj.wmslayers = self.data['wmslayers']
        self.obj.imgformat = self.data['imgformat']

    def widget_params(self):
        result = ObjectWidget.widget_params(self)

        if self.obj:
            result['value'] = dict(
                wmslayers=self.obj.wmslayers,
                imgformat=self.obj.imgformat,
            )

        client = self.options['layer'].client
        result['imgformat'] = client.getOperationByName('GetMap').formatOptions

        wmslayers = []
        for id, layer in client.contents.iteritems():
            wmslayers.append(dict(
                id=id, title=layer.title,
                index=layer.index))

        wmslayers.sort(key=lambda x: x['index'])

        result['wmslayers'] = wmslayers

        return result

    def widget_module(self):
        return 'wmsclient/StyleWidget'


def setup_pyramid(comp, config):
    DBSession = comp.env.core.DBSession

    WMSClientLayer.object_widget = (
        (WMSClientLayer.identity, WMSClientLayerObjectWidget),
    )

    WMSClientStyle.object_widget = (
        (WMSClientStyle.identity, WMSClientStyleObjectWidget),
    )

    # Функция выполнения WMS-запроса GetFeatureInfo.
    # Предполагаемое использование: идентификация объектов ПКК
    # Особенности:
    #   1) Выполняется запрос к первому WMS-слою карты
    #   2) Если в настройках слоя указан параметр column_id, то он используется для фильтрации
    #   3) На клиента передаются все поля в неизменном виде
    #   4) Формат запроса - text/xml
    def identify(request):

        result = dict()

        # Один и тот же слой может быть добавлен на карту с различными
        # параметрами стиля (перечнем удаленных слоёв)
        styles = map(int, request.json_body['styles'])

        # Координаты клика
        x = int(request.json_body['x'])
        y = int(request.json_body['y'])

        # Ширина и высота области карты
        width = request.json_body['width']
        height = request.json_body['height']

        # Географический охват
        bbox = request.json_body['bbox']

        # Выбираем первый стиль, соответствующий одному слою карты (ПКК)
        style = DBSession.query(WMSClientStyle).filter(WMSClientStyle.id.in_(styles)).scalar()

        if style:

            # Формируем и выполняем запрос GetFeatureInfo
            url = style.layer.url
            params = {
                "REQUEST": "GetFeatureInfo",
                "SRS": "EPSG:4326",
                "INFO_FORMAT": "text/xml",
                "X": x,
                "Y": y,
                "BBOX": bbox,
                "WIDTH": width,
                "HEIGHT": height,
                "VERSION": style.layer.version,
                "QUERY_LAYERS": style.wmslayers
            }

            url = url + "?" + urllib.urlencode(params)

            try:
                response = urllib2.urlopen(url)
                try:
                    doc = etree.parse(response)
                    response.close()
                    root = doc.getroot()
                    
                    # empty namespace prefix is not supported in XPath
                    nsmap = dict(((k,v) for k,v in root.nsmap.iteritems() if k is not None))
                    prefix = nsmap.iterkeys().next()

                    records = doc.xpath("%s:%s" % (prefix, "FIELDS"), namespaces=nsmap)
                    result['data'] = []
                    for record in records:
                        result['data'].append(dict((k,v) for k,v in record.attrib.iteritems()))

                    # Удаляем повторяющиеся записи
                    result['data'] = [dict(t) for t in set([tuple(d.items()) for d in result['data']])]


                except etree.XMLSyntaxError:
                    result['error'] = u"Невалидный XML-ответ"

            except urllib2.URLError:
                result['error'] = u"Ошибка подключения к удалённому хосту"

        else:
            result['error'] = u"На карте нет включенных WMS-слоёв"

        return result

    config.add_route('wmsclient.identify', '/wmsclient/identify')
    config.add_view(identify, route_name='wmsclient.identify', renderer='json')
