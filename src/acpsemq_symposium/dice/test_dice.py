"""Test computations of the Dice similarity coefficient"""

import pytest
import shapely

from . import dice


def test_dice_from_polygons():

    # Test case of two unit square that half overlap

    a_half = shapely.geometry.Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
    b_half = shapely.geometry.Polygon([(0.5, 0), (0.5, 1), (1.5, 1), (1.5, 0)])

    expected_dice = 2 * 0.5 / (1 + 1)

    computed_dice = dice.from_shapely(a_half, b_half)

    assert computed_dice == pytest.approx(expected_dice)

    # test that half overlap also fails

    b_half_bad = shapely.geometry.Polygon([(0.5, 0), (0.5, 1), (1.5, 1), (2, 0)])

    computed_dice_bad = dice.from_shapely(a_half, b_half_bad)

    assert computed_dice_bad != pytest.approx(expected_dice)
