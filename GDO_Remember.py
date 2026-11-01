from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Enum import GDT_Enum
from gdo.core.GDT_Text import GDT_Text
from gdo.date.GDT_Created import GDT_Created
from gdo.mira_remember.GDT_Stance import GDT_Stance


class GDO_Remember(GDO):
    """One helpful or interesting tip."""

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('rm_id'),
            GDT_Text('rm_text').not_null(),
            GDT_Enum('rm_section').choices({
                'general': 'General', 'work': 'Work', 'technology': 'Technology',
                'social': 'Social', 'creativity': 'Creativity',
            }).not_null().initial('general'),
            GDT_Stance('rm_stance'),
            GDT_Creator('rm_creator'),
            GDT_Created('rm_created'),
            GDT_Enum('rm_visibility').choices({'public': 'Public', 'private': 'Private'})
                .not_null().initial('public').tooltip('tt_rm_visibility'),
        ]
