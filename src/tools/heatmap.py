import heatmap


def _adapt(map_info):
    return [(m.position.x, m.position.y) for m in map_info.mass_markers]


def get_heatmap(map_info, dot_size=150, opacity=255):
    hm = heatmap.Heatmap()
    # schemes: classic, fire, omg, pbj, pgaitch
    img = hm.heatmap(points=_adapt(map_info), dotsize=max(int(dot_size), 1), opacity=opacity,
                     size=map_info.size, scheme='fire', area=((0, 0), map_info.size))
    return img
