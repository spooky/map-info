from PyQt5.QtCore import QObject, QUrl, QDir, pyqtSignal, pyqtProperty

from faf.map import get_map_info


class MainViewModel(QObject):
    map_dir_changed = pyqtSignal(name='map_dirChanged')
    dot_size_changed = pyqtSignal(name='dot_sizeChanged')
    map_size_changed = pyqtSignal(name='map_sizeChanged')
    map_name_changed = pyqtSignal(name='map_nameChanged')
    flip_changed = pyqtSignal(name='flipChanged')

    def __init__(self, *args, **kwargs):
        self.map_info = None
        self._map_dir = None
        self._dot_size = 1
        self._map_size = 1
        self._map_name = None
        self._flip = False
        super().__init__(*args, **kwargs)
        self.map_dir_changed.connect(self._on_map_dir_chaged)

    @pyqtProperty(str, notify=map_dir_changed)
    def map_dir(self):
        return self._map_dir

    @map_dir.setter
    def map_dir(self, value):
        if self._map_dir != value:
            self._map_dir = value
            self.map_dir_changed.emit()

    @pyqtProperty(int, notify=dot_size_changed)
    def dot_size(self):
        return self._dot_size

    @dot_size.setter
    def dot_size(self, value):
        if self._dot_size != value:
            self._dot_size = value
            self.dot_size_changed.emit()

    @pyqtProperty(int, notify=map_size_changed)
    def map_size(self):
        return self._map_size

    @map_size.setter
    def map_size(self, value):
        if self._map_size != value:
            self._map_size = value
            self.map_size_changed.emit()

    @pyqtProperty(str, notify=map_name_changed)
    def map_name(self):
        return self._map_name

    @map_name.setter
    def map_name(self, value):
        if self._map_name != value:
            self._map_name = value
            self.map_name_changed.emit()

    @pyqtProperty(bool, notify=flip_changed)
    def flip(self):
        return self._flip

    @flip.setter
    def flip(self, value):
        if self._flip != value:
            self._flip = value
            self.flip_changed.emit()

    def _on_map_dir_chaged(self):
        url = QUrl(self.map_dir)
        map_dir = QDir(url.toLocalFile()).path()
        self.map_info = get_map_info(map_dir)
        self.map_size = round(max(self.map_info.size.w, self.map_info.size.h))
        self.map_name = self.map_info.name
        self.dot_size = self._get_dot_size()

    def _get_dot_size(self):
        return min(150, self.map_size)
