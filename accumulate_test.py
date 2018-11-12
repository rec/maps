import json, pathlib, unittest
import accumulate

TEST_DATA_DIR = pathlib.Path(__file__).parent / 'testdata'
REPORT_FILE = TEST_DATA_DIR / 'report_file.json'
ACCUMULATE_FILE = TEST_DATA_DIR / 'accumulate.json'


class AccumulateTest(unittest.TestCase):
    def test_accumulate_file(self):
        table = {}
        accumulate.accumulate_file(table, str(REPORT_FILE))
        expected = json.load(open(str(ACCUMULATE_FILE)))

        self.assertEqual(table, expected)
