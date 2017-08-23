import os

from tools.lua_map_helper import parse_lua, get_name, get_size, get_markers


class MapInfo():
    name = None
    size = None
    mass_markers = []

    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None)
        self.size = kwargs.pop('size', None)
        self.mass_markers = kwargs.pop('mass_markers', None)

    def __repr__(self):
        return '<{}.{} "{}" {}x{}, {} mex>'.format(self.__class__.__module__, self.__class__.__name__,
                                                   self.name, self.size.w, self.size.h, len(self.mass_markers))


def get_map_info(map_dir):
    assert os.path.isdir(map_dir)

    dir_name = os.path.basename(map_dir)
    map_name, _ = os.path.splitext(dir_name)
    save_file_path = os.path.join(map_dir, '{}_save.lua'.format(map_name))
    scenario_file_path = os.path.join(map_dir, '{}_scenario.lua'.format(map_name))

    with open(save_file_path) as save_file, open(scenario_file_path) as scenario_file:
        lua = parse_lua(save_file, scenario_file)

        name = get_name(lua)
        size = get_size(lua)
        mass_markers = [m for m in get_markers(lua)]

    return MapInfo(name=name, size=size, mass_markers=mass_markers)
