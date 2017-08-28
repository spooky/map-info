from PyQt5.QtCore import QSize, QUrl, QUrlQuery, QDir
from PyQt5.QtGui import QPixmap
from PyQt5 import QtQuick

from PIL.ImageOps import flip

from faf.map import get_map_info
from tools.heatmap import get_heatmap


class HeatmapProvider(QtQuick.QQuickImageProvider):
    def __init__(self):
        super().__init__(QtQuick.QQuickImageProvider.Pixmap)

    def requestPixmap(self, id, size):
        url = QUrl(id)
        query = QUrlQuery(url.query())
        map_dir = QDir(url.toLocalFile()).path()
        dot_size = round(float(query.queryItemValue('dot_size')))
        should_flip = query.queryItemValue('flip') in ['True', 'true']
        opacity = round(float(query.queryItemValue('opacity')))

        try:
            img, size = self._generate_heatmap(map_dir, dot_size, opacity)
            if should_flip:
                img = flip(img)
            p = QPixmap.fromImage(img.toqimage())
            return p, size
        except Exception:
            return QPixmap(), QSize(-1, -1)

    def _generate_heatmap(self, map_dir, dot_size, opacity):
        map_info = get_map_info(map_dir)
        return get_heatmap(map_info, dot_size, opacity), QSize(map_info.size.w, map_info.size.h)
