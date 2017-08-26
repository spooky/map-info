import sys
import os
import os.path

from PyQt5.QtCore import Qt, QCoreApplication, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from providers import HeatmapProvider
from view_models import MainViewModel


def cleanUp(obj):
    for i in obj.__dict__:
        item = obj.__dict__[i]
        clean(item)


def clean(item):
    """Clean up the memory by closing and deleting the item if possible."""
    if isinstance(item, list) or isinstance(item, dict):
        for _ in range(len(item)):
            clean(list(item).pop())
    else:
        try:
            item.close()
        except (RuntimeError, AttributeError):  # deleted or no close method
            pass
        try:
            item.deleteLater()
        except (RuntimeError, AttributeError):  # deleted or no deleteLater method
            pass


def start_ui(argv):
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QGuiApplication(argv)
    engine = QQmlApplicationEngine()

    mainViewModel = MainViewModel()

    rootContext = engine.rootContext()
    rootContext.setContextProperty('mainViewModel', mainViewModel)

    image_provider = HeatmapProvider()
    engine.addImageProvider('heatmap', image_provider)

    os.chdir(os.path.dirname(__file__))
    engine.load(QUrl('ui/main.qml'))

    app.aboutToQuit.connect(lambda: cleanUp(app))

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == '__main__':
    sys.exit(start_ui(sys.argv))
