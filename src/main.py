import sys
import os
import os.path

from PyQt5.QtCore import Qt, QCoreApplication, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from providers import HeatmapProvider
from view_models import MainViewModel


def start_ui(argv):
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    mainViewModel = MainViewModel()

    rootContext = engine.rootContext()
    rootContext.setContextProperty('mainViewModel', mainViewModel)

    image_provider = HeatmapProvider()
    engine.addImageProvider('heatmap', image_provider)

    os.chdir(os.path.dirname(__file__))
    engine.load(QUrl('ui/main.qml'))

    mainViewModel.map_size = 10

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == '__main__':
    sys.exit(start_ui(sys.argv))
