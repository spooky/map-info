import sys
import os
import os.path

from PyQt5.QtCore import Qt, QCoreApplication, QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

from providers import HeatmapProvider
from view_models import MainViewModel


class AppUi(QQmlApplicationEngine):

    def __init__(self, *args, **kwargs):
        os.chdir(os.path.dirname(__file__))

        super().__init__(*args, **kwargs)
        self.view_models = {}
        self.providers = {}

    def set_root_view_model(self, name, view_model):
        self.view_models[name] = view_model
        self.rootContext().setContextProperty(name, view_model)

    def set_image_provider(self, name, provider):
        self.providers[name] = provider
        self.addImageProvider(name, provider)

    def load_ui(self, url):
        self.load(QUrl(url))
        if not self.rootObjects():
            exit(-1)

    def clean(self):
        for i in self.__dict__:
            item = self.__dict__[i]
            self._clean(item)

    def _clean(self, item):
        """Clean up the memory by closing and deleting the item if possible."""
        if isinstance(item, list) or isinstance(item, dict):
            for _ in range(len(item)):
                self._clean(list(item).pop())
        else:
            try:
                item.close()
            except (RuntimeError, AttributeError):  # deleted or no close method
                pass
            try:
                item.deleteLater()
            except (RuntimeError, AttributeError):  # deleted or no deleteLater method
                pass


def main(argv):
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QGuiApplication(argv)

    ui = AppUi()
    ui.set_root_view_model('mainViewModel', MainViewModel())
    ui.set_image_provider('heatmap', HeatmapProvider())
    ui.load('ui/main.qml')

    app.aboutToQuit.connect(lambda: ui.clean())

    return app.exec_()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
