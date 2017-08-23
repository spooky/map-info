from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'z'])
Point.__new__.__defaults__ = (None,)
