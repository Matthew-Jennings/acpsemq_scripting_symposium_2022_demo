"""A module for computing the Dice similarity coefficient"""

from shapely.geometry.base import BaseGeometry as ShapelyGeom


def from_shapely(a: ShapelyGeom, b: ShapelyGeom) -> float:
    """Compute the Dice similarity coefficient for two shapely geometries"""

    return 2 * a.intersection(b).area / (a.area + b.area)
