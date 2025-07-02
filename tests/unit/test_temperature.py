# -*- coding: utf-8 -*-
# Copyright (c) 2025 Sandra McCann <samccann@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or
# https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

import pytest

from ansible_collections.samccann.validateme.plugins.modules.temperature import (  # noqa E501
    _temperature,
)


"""Unit tests for samccann.validateme.temperature."""


class TestTemperature:
    # test that the temperature is converted correctly
    def test_convert_temperature(self):
        assert _temperature(0.0, "celsius") == 32.0
        assert abs(_temperature(100.0, "fahrenheit") - 37.78) < 0.01

    # test that module fails if the temp option is not provided
    def test_no_temp(self):
        with pytest.raises(TypeError):
            _temperature(None, "celsius")  # type: ignore

    # test that module fails if the temp is not a number
    def test_invalid_temp(self):
        with pytest.raises(TypeError):
            _temperature("X", "celsius")  # type: ignore

    # test that module fails if the unit option is not provided
    def test_no_unit(self):
        with pytest.raises(TypeError):
            _temperature(100.0, None)  # type: ignore

    # test that module fails if the unit is not a string
    def test_invalid_unit_type(self):
        with pytest.raises(TypeError):
            _temperature(100.0, 1)  # type: ignore

    # test that module fails if the unit is not a valid choice
    def test_invalid_unit(self):
        with pytest.raises(ValueError):
            _temperature(100.0, "X")
