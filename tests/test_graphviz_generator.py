import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'graphviz_dependencies.py'


class DependencyTests(unittest.TestCase):
    def run_generator(self, data, target):
        with tempfile.TemporaryDirectory() as temp:
            src = Path(temp) / 'input.json'
            out = Path(temp) / 'output'
            src.write_text(json.dumps(data), encoding='utf-8')
            result = subprocess.run([sys.executable, str(SCRIPT), str(src), str(out), '--changed', target], capture_output=True, text=True)
            generated = {p.name: p.read_text(encoding='utf-8') for p in out.glob('*')} if out.exists() else {}
            return result, generated

    def test_reverse_transitive_impact_terminates_on_cycle(self):
        data = {'nodes': {'web': '前端', 'order': '訂單', 'payment': '支付', 'sdk': 'SDK', 'other': '其他'},
                'edges': [['web', 'order'], ['order', 'payment'], ['payment', 'order'], ['payment', 'sdk']]}
        result, outputs = self.run_generator(data, 'payment')
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(outputs['impact.json'])
        self.assertEqual(report['affected'], ['order', 'payment', 'web'])
        self.assertEqual(report['edges'], [['order', 'payment'], ['payment', 'order'], ['web', 'order']])
        self.assertNotIn('"sdk"', outputs['impact.dot'])
        self.assertIn('"sdk"', outputs['overview.dot'])

    def test_standalone_graphs_explain_arrow_semantics(self):
        result, outputs = self.run_generator({'nodes': {'a': 'A'}, 'edges': []}, 'a')
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ['overview.dot', 'impact.dot']:
            self.assertIn('A → B：A 依賴 B', outputs[name])
            self.assertIn('潛在檢查範圍，不代表必然故障', outputs[name])
        self.assertEqual(json.loads(outputs['impact.json'])['affected'], ['a'])

    def test_rejects_invalid_input_before_creating_outputs(self):
        cases = [
            ({'nodes': {'a': 'A'}, 'edges': [['missing', 'a']]}, 'a'),
            ({'nodes': {'a': 'A'}, 'edges': []}, 'missing'),
            ({'nodes': {'a': 'A'}, 'edges': [['a']]}, 'a'),
            ({'nodes': {'a': 7}, 'edges': []}, 'a'),
        ]
        for data, target in cases:
            with self.subTest(data=data, target=target):
                result, outputs = self.run_generator(data, target)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('invalid input:', result.stderr)
                self.assertEqual(outputs, {})


if __name__ == '__main__':
    unittest.main()
