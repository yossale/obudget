# -*- coding: iso-8859-15 -*-
"""Simple FunkLoad test

$Id$
"""
import unittest
from random import random
from funkload.FunkLoadTestCase import FunkLoadTestCase

class LoadHome(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    def setUp(self):
        """Setting up test."""
        self.server_url = self.conf_get('main', 'url')

    def test_load_home(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------
        nb_time = self.conf_getInt('test_simple', 'nb_time')
        self.setBasicAuth('guest', 'powertothepeople')
        for i in range(nb_time):
            self.get(server_url, description='Get url')
            self.get('%s/00' % server_url, description='Get url')
        # end of test -----------------------------------------------


if __name__ in ('main', '__main__'):
    unittest.main()
