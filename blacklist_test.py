import pathlib, unittest
import blacklist

TEST_DATA_DIR = pathlib.Path(__file__).parent / 'testdata'
ACCUMULATE_FILE = str(TEST_DATA_DIR / 'accumulate.json')
RULES_FILE = str(TEST_DATA_DIR / 'rules.json')


class BlacklistTest(unittest.TestCase):
    def test_blacklist_file(self):
        bl = blacklist.compute_blacklists(ACCUMULATE_FILE, RULES_FILE)
        expected = {'spam': ['evil.com', 'evil2.com']}
        self.assertEqual(bl, expected)
