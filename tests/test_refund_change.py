"""Assertions on teaching fixtures, NOT an implemented payment/refund API."""
import json
import os
from pathlib import Path
import unittest

DEFAULT = Path(__file__).resolve().parents[1] / 'examples/refund-change/scenarios.json'


class RefundSpecificationTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path(os.environ.get('REFUND_SCENARIOS', DEFAULT)).read_text(encoding='utf-8'))

    def test_eligibility_includes_outstanding_reservations(self):
        self.assertEqual(len(self.data['eligibility']), 6)
        for case in self.data['eligibility']:
            with self.subTest(case=case['id']):
                for field in ('paid', 'refunded', 'reserved', 'request'):
                    self.assertIs(type(case[field]), int)
                available = case['paid'] - case['refunded'] - case['reserved']
                self.assertGreaterEqual(available, 0)
                self.assertEqual(case['eligible'], 0 < case['request'] <= available)

    def test_settlement_unknown_and_duplicate_preserve_ledger_rules(self):
        events = {c['event'] for c in self.data['outcomes']}
        self.assertEqual(events, {'success', 'failure', 'unknown', 'duplicate_success'})
        self.assertEqual(len(self.data['outcomes']), 4)
        for case in self.data['outcomes']:
            with self.subTest(event=case['event']):
                before, after = case['before'], case['after']
                self.assertEqual(after['paid'], before['paid'])
                for snapshot in (before, after):
                    self.assertGreaterEqual(snapshot['refunded'], 0)
                    self.assertGreaterEqual(snapshot['reserved'], 0)
                    self.assertLessEqual(snapshot['refunded'] + snapshot['reserved'], snapshot['paid'])
                if case['event'] == 'success':
                    self.assertEqual(after['refunded'], before['refunded'] + case['amount'])
                    self.assertEqual(after['reserved'], before['reserved'] - case['amount'])
                elif case['event'] == 'failure':
                    self.assertEqual(after['refunded'], before['refunded'])
                    self.assertEqual(after['reserved'], before['reserved'] - case['amount'])
                else:
                    self.assertEqual(after, before, 'unknown or duplicate must not change ledger')


if __name__ == '__main__':
    unittest.main()
