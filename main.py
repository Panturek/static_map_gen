from matplotlib import pyplot as plt
import svgutils.compose as sc
import svgutils.transform as sg
import numpy as np
from robinson import Robinson

robson = Robinson()

def make_meridian(latitude, von=-90, bis=90, step=5):
    _points = [robson.to_robinson(latitude, -lat) for lat in range(von, bis, step)]
    [ _points.append(x) for x in list(reversed(_points))]
    return _points

points_lat0 = make_meridian(-10)
points_lat1 = make_meridian(110, -50, 50)

o_mapw, o_maph = robson.orig_map_shape
mapw, maph = robson.map_shape

scale_x, scale_y = mapw/o_mapw, maph/o_maph

fig = sg.SVGFigure(f"{mapw}px", f"{maph}px")
fig1 = sg.fromfile("world_map.svg")
plot1 = fig1.getroot()
plot1.scale(scale_x, scale_y)
lat10 = sg.LineElement( np.linspace((mapw//2,0),(mapw//2, maph), 100), width=3, color="red" )
lat0 = sg.LineElement( points_lat0, width=1, color="green" )
lat1 = sg.LineElement( points_lat1, width=1, color="blue" )
equator = sg.LineElement( np.linspace((0,maph//2),(mapw, maph//2), 100), width=3, color="red" )

fig.append([plot1, lat0, lat1, lat10, equator])
fig.save("compose.svg")

