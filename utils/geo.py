import folium
import math
import numpy as np

def get_polygons(clat=39.922353, clon=116.391958, grid_w=32, grid_h=32, acc=1000):
    """
    @brief 将区域划分成32*32网格
    @param clat: float
    @param center latitude, 划分区域的中心纬度
    @param clat: float
    @param center longitude, 划分区域的中心经度
    @param acc: int
    @param accuracy, 精度, 单位为m
    """
    polar_radius = 6356908.8  # 地球极半径
    lat_perimeter = 2 * math.pi * 1000 / math.sqrt(
        1 / (6377.830 ** 2) + (math.tan(math.radians(clat)) / 6377.830) ** 2)  # 区域所在纬半径

    lon_delta = 360 * acc / lat_perimeter  # 经度划分精度
    lat_delta = 360 * acc / (polar_radius * math.pi * 2)  # 纬度划分精度

    lats = np.linspace(clat + grid_h/2.0 * lat_delta, clat - grid_h/2.0 * lat_delta, grid_h + 1)
    lons = np.linspace(clon - grid_w/2.0 * lon_delta, clon + grid_w/2.0 * lon_delta, grid_w + 1)

    polygons = []

    for i in range(0, grid_w):
        for j in range(0, grid_h):
            polygons.append([
                [lats[i], lons[j]],
                [lats[i], lons[j + 1]],
                [lats[i + 1], lons[j + 1]],
                [lats[i + 1], lons[j]]
            ])
    return polygons

def get_map(clat=39.922353, clon=116.391958, polygons=None, colors=None, show=False, save=False):
    cur_map = folium.Map(location=[clat, clon], zoom_start=12, tiles='CartoDB positron', png_enabled=False)

    index = 0
    for grid in list(polygons):
        _curr_ = folium.Polygon(
            locations=grid,
            color='white',
            weight=1,
            fill_color=colors[index] if isinstance(colors[index], str) else rgb2hex(colors[index]),
            fill_opacity=0.4,
            fill=True,
        )
        _curr_.add_to(cur_map)
        index = index + 1

    if save:
        cur_map.save('./map.html')
    if show:
        return cur_map

    return None