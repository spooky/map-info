import os.path
from lupa import LuaRuntime

from core import Point, Size


class Marker(object):
    type = None
    position = None
    orientation = None

    def __init__(self, *args, **kwargs):
        self.type = kwargs.get('type', None)
        self.position = self.__to_point(kwargs.get('position', None))
        # self.orientation = self.__to_point(kwargs.get('orientation', None))

    def __repr__(self):
        return '<{}.{} {}@{}>'.format(self.__class__.__module__, self.__class__.__name__, self.type, self.position)

    def __to_point(self, lua_table):
        if not lua_table:
            return None

        # assumption that this is a lua table type
        p = dict(zip('xyz', lua_table.values()))
        return Point(**p)


def parse_lua(*scripts):
    lua = LuaRuntime(unpack_returned_tuples=True)
    script_path = os.path.dirname(__file__)

    # import stub function definitions used in the save file
    with open(os.path.join(script_path, 'stubs.lua')) as f:
        lua.execute(f.read())

    # read the scripts
    for script in scripts:
        lua.execute(script.read())

    return lua


def get_markers(lua):
    markers = lua.globals()['Scenario']['MasterChain']['_MASTERCHAIN_']['Markers']
    if not markers:
        raise Exception('Markers not found')

    mass_points = (Marker(**m) for m in markers.values() if m['type'] == 'Mass')
    return mass_points


def get_size(lua):
    size = lua.globals()['ScenarioInfo']['size']
    return Size(**dict(zip('wh', size.values())))


def get_name(lua):
    name = lua.globals()['ScenarioInfo']['name']
    return name
