from __future__ import annotations

from gdo.base.GDO_Module import GDO_Module
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.mira_remember.GDO_Remember import GDO_Remember
from gdo.ui.GDT_Link import GDT_Link

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.ui.GDT_Page import GDT_Page

PUBLIC_TIPS = (
    ('general', 'Help beginners learn and participate with patience and respect.'),
    ('work', 'Verify claims against current evidence before reporting success.'),
    ('work', 'Investigate the cause before choosing the smallest effective fix.'),
    ('work', 'Preserve other people’s changes and review diffs before committing.'),
    ('technology', 'Test meaningful user workflows against the documented goal.'),
    ('social', 'Ask for help when another person can resolve an issue more quickly.'),
)


class module_mira_remember(GDO_Module):

    def gdo_classes(self) -> list[type[GDO]]:
        return [GDO_Remember]

    async def gdo_install(self):
        table = GDO_Remember.table()
        for section, text in PUBLIC_TIPS:
            if table.get_by_vals({'rm_text': text, 'rm_visibility': 'public'}) is None:
                GDO_Remember.blank({
                    'rm_text': text,
                    'rm_section': section,
                    'rm_stance': 'neutral',
                    'rm_visibility': 'public',
                }).insert()

    def gdo_module_config(self) -> list[GDT]:
        return []

    def gdo_user_config(self) -> list[GDT]:
        return []

    def gdo_user_settings(self) -> list[GDT]:
        return []

    def gdo_init(self):
        pass

    def gdo_load_scripts(self, page: 'GDT_Page'):
        self.add_js('js/pygdo-mira_remember.js')
        self.add_css('css/pygdo-mira_remember.css')

    def gdo_init_sidebar(self, page: 'GDT_Page'):
        page._left_bar.add_field(GDT_Link().href(self.href('overview')).text('module_mira_remember'))
