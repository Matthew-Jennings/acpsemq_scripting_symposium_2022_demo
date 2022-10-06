# Adapted from https://github.com/RadiotherapyAI/rai/blob/02cc0a8fb7679342a606a92641b48f00c452f508/radiotherapyai/metrics/dice.py

# Copyright (C) 2022 Radiotherapy AI Pty Ltd, Matthew Jennings

# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License. You may
# obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.

"""A module for computing the Dice similarity coefficient"""

from shapely.geometry.base import BaseGeometry as ShapelyGeom


def from_shapely(a: ShapelyGeom, b: ShapelyGeom) -> float:
    """Compute the Dice similarity coefficient from two `shapely` geometries.

    Explanation of the Dice similarity coefficient is available at:
    <https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient>

    Args:
        a (shapely.geometry.base.BaseGeometry)
        b (shapely.geometry.base.BaseGeometry)
    """

    return 2 * a.intersection(b).area / (a.area + b.area)
