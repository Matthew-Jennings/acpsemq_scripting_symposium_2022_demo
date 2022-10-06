"""Test computations of the Dice similarity coefficient"""

import pytest
import shapely

from . import dice


def test_dice_for_shapely_polygons():

    # Test unit squares with 50% overlap

    a_half = shapely.geometry.Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
    b_half = shapely.geometry.Polygon([(0.5, 0), (0.5, 1), (1.5, 1), (1.5, 0)])

    expected_dice_half = 2 * 0.5 / (1 + 1)
    computed_dice_half = dice.from_shapely(a_half, b_half)

    assert computed_dice_half == pytest.approx(expected_dice_half)

    # Test fail case

    b_half_fail = shapely.geometry.Polygon([(0.5, 0), (0.5, 1), (1.5, 1), (2, 0)])
    computed_dice_half_fail = dice.from_shapely(a_half, b_half_fail)

    assert computed_dice_half_fail != pytest.approx(expected_dice_half)
