"""Test computations of Dice similarity coefficients"""

import pytest
import shapely

from . import dice


def test_dice_for_shapely_polygons():

    # Test two unit squares with 50% overlap

    a_half = shapely.geometry.Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
    b_half = shapely.geometry.Polygon([(0.5, 0), (0.5, 1), (1.5, 1), (1.5, 0)])

    expected_dice = 2 * 0.5 / (1 + 1)
    computed_dice = dice.from_shapely(a_half, b_half)

    assert computed_dice == pytest.approx(expected_dice)

    # Test failure case

    b_bad = shapely.geometry.Polygon([(0.5, 0), (0.5, 1), (1.5, 1), (2, 0)])
    computed_dice_bad = dice.from_shapely(a_half, b_bad)

    assert computed_dice_bad != pytest.approx(expected_dice)
