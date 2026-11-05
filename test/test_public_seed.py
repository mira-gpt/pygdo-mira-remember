import unittest
from unittest.mock import patch

from gdo.mira_remember.module_mira_remember import PUBLIC_TIPS, module_mira_remember


class PublicSeedTest(unittest.IsolatedAsyncioTestCase):
    async def test_install_is_repeatable_and_keeps_private_entries(self):
        rows = [{'rm_text': PUBLIC_TIPS[0][1], 'rm_visibility': 'private'}]

        class FakeTable:
            def get_by_vals(self, values):
                return next((row for row in rows
                             if all(row.get(k) == v for k, v in values.items())), None)

        class FakeRecord:
            def __init__(self, values):
                self.values = values

            def insert(self):
                rows.append(self.values)

        with patch('gdo.mira_remember.module_mira_remember.GDO_Remember') as model:
            model.table.return_value = FakeTable()
            model.blank.side_effect = FakeRecord
            module = module_mira_remember()
            await module.gdo_install()
            await module.gdo_install()

        self.assertEqual(1, sum(row['rm_visibility'] == 'private' for row in rows))
        public = [row for row in rows if row['rm_visibility'] == 'public']
        self.assertEqual(len(PUBLIC_TIPS), len(public))
        self.assertEqual({text for _, text in PUBLIC_TIPS}, {row['rm_text'] for row in public})


if __name__ == '__main__':
    unittest.main()
