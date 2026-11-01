from gdo.ui.GDT_IconedEnum import GDT_IconedEnum


class GDT_Stance(GDT_IconedEnum):
    def __init__(self, name: str = 'rm_stance'):
        super().__init__(name)
        self.choices({'aggressive': 'Aggressive', 'neutral': 'Neutral', 'passive': 'Passive'})
        self.icons({'aggressive': 'flash', 'neutral': 'legal', 'passive': 'pause'})
        self.not_null().initial('neutral')
