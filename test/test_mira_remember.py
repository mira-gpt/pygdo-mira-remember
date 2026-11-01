import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.mira_remember.module_mira_remember import module_mira_remember
from gdotest.TestUtil import cli_plug, reinstall_module, cli_gizmore, GDOTestCase, WebPlug, install_module, web_plug


class module_mira_remember_Test(GDOTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        install_module('mira_remember')
        loader.load_modules_db(True)
        WebPlug.COOKIES = {}
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()

    def test_00_reinstall(self):
        reinstall_module('mira_remember')
        self.assertIs(type(module_mira_remember.instance()), module_mira_remember, "Cannot re-install module mira_remember.")

    def test_03_overview_cli(self):
        giz =  cli_gizmore()
        out = cli_plug(giz, "$mira_remember.overview")
        self.assertIsNotNone(out, '$mira_remember.overview does not work.')

    def test_02_overview_web(self):
        giz =  cli_gizmore()
        out = web_plug("mira_remember.overview.html")
        self.assertIsNotNone(out, 'mira_remember.overview.html does not work.')


if __name__ == '__main__':
    unittest.main()
