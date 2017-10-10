# -*- coding: utf-8 -*-
# Yet Another PBO Library
# Copyright (C) 2017 Lukasz Taczuk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from __future__ import print_function
from __future__ import unicode_literals

import os
import unittest
import yapbol


def get_resource(filename):
    return os.path.join(os.path.dirname(__file__), 'resources', filename)



class YapbolTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_open_regular_pbo(self):
        f = yapbol.PBOFile.read_file(get_resource('DFL_HillMission.Malden.pbo'))
        files = (
            'cfg\\cfgBaseSettings.hpp',
            'cfg\\cfgSides.hpp',
            'cfgRespawn.hpp',
            'cfgSectors.hpp',
            'cfgWeather.hpp',
            'description.ext',
            'init.sqf',
            'mission.sqm',
            'ui\\common\\aawCore.hpp',
            'ui\\common\\aaw_baseclasses.hpp',
            'ui\\common\\baseclasses.hpp',
            'ui\\common\\defines.hpp',
            'ui\\common\\do_not_Change_Anything',
            'ui\\do_not_Change_Anything',
            'ui\\hud\\do_not_Change_Anything',
            'ui\\hud\\Notification.hpp',
            'ui\\hud\\PerformanceStatus.hpp',
            'ui\\media\\AAWLogo_ca.paa',
            'ui\\media\\badClientFrames_ca.paa',
            'ui\\media\\badServerFrames_ca.paa',
            'ui\\media\\base_ca.paa',
            'ui\\media\\do_not_Change_Anything',
            'ui\\media\\fob_ca.paa',
            'ui\\media\\loadingscreen_co.paa',
            'ui\\media\\notification_gradient_ca.paa',
            'ui\\media\\rally_ca.paa',
        )

        counter = 0
        for entry in f:
            self.assertIn(entry.filename, files)
            counter +=1

        self.assertEqual(counter, len(files))

    def test_zolc_utf8(self):
        f = yapbol.PBOFile.read_file(get_resource('zolc_utf.pbo'))
        files = (
            'test.Malden/description.ext',
            'test.Malden/mission.sqm',
            'test.Malden/żółć.hpp',
        )

        counter = 0
        for entry in f:
            self.assertIn(entry.filename, files)
            counter += 1

        self.assertEqual(counter, len(files))

    def test_zolc_addonbuilder(self):
        f = yapbol.PBOFile.read_file(get_resource('zolc_addonbuilder.pbo'))
        files = (
            'config.bin',
            b'z\xf3lc.txt',  # zólc.txt in mbcs
        )

        counter = 0
        for entry in f:
            self.assertIn(entry.filename, files)
            counter += 1

        self.assertEqual(counter, len(files))
