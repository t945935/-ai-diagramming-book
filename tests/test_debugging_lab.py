"""Real-renderer regression fixtures; missing tools are errors, not skips.

Run from repository root. DOT and MMDC may be absolute executable paths.
PUPPETEER_CONFIG optionally points to a local Chromium configuration file.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / 'examples' / 'debugging'


class DebuggingLabTests(unittest.TestCase):
    def test_mermaid_missing_bracket_is_rejected(self):
        cli = os.environ.get('MMDC', str(ROOT / 'node_modules' / '.bin' / 'mmdc'))
        with tempfile.TemporaryDirectory() as temp:
            for stem in ('broken', 'fixed'):
                output = Path(temp) / (stem + '.svg')
                cmd = [cli, '-i', str(LAB / 'mermaid' / (stem + '.mmd')), '-o', str(output)]
                if os.environ.get('PUPPETEER_CONFIG'):
                    cmd += ['-p', os.environ['PUPPETEER_CONFIG']]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                if stem == 'broken':
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('Parse error', result.stderr)
                else:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    svg = ET.parse(output).getroot()
                    self.assertTrue(svg.tag.endswith('svg'))
                    self.assertIn('待確認', ''.join(svg.itertext()))

    def test_dot_missing_target_is_rejected(self):
        cli = os.environ.get('DOT', 'dot')
        with tempfile.TemporaryDirectory() as temp:
            for stem in ('broken', 'fixed'):
                output = Path(temp) / (stem + '.svg')
                result = subprocess.run([cli, '-Tsvg', str(LAB / 'dot' / (stem + '.dot')), '-o', str(output)], capture_output=True, text=True, timeout=30)
                if stem == 'broken':
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('syntax error', result.stderr)
                else:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertTrue(ET.parse(output).getroot().tag.endswith('svg'))

    def test_valid_json_can_encode_reversed_dependencies(self):
        expected = ['order', 'payment', 'web']
        with tempfile.TemporaryDirectory() as temp:
            for stem in ('broken', 'fixed'):
                output = Path(temp) / stem
                result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'graphviz_dependencies.py'), str(LAB / 'direction' / (stem + '.json')), str(output), '--changed', 'payment'], capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                actual = json.loads((output / 'impact.json').read_text())['affected']
                if stem == 'broken':
                    self.assertEqual(actual, ['payment'])
                    self.assertNotEqual(actual, expected)
                else:
                    self.assertEqual(actual, expected)

    def test_unknown_endpoint_is_rejected_before_output(self):
        with tempfile.TemporaryDirectory() as temp:
            for stem in ('broken', 'fixed'):
                output = Path(temp) / stem
                result = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'graphviz_dependencies.py'), str(LAB / 'endpoint' / (stem + '.json')), str(output), '--changed', 'payment'], capture_output=True, text=True, timeout=30)
                if stem == 'broken':
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('each edge must name two existing nodes', result.stderr)
                    self.assertFalse(output.exists())
                else:
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(json.loads((output / 'impact.json').read_text())['affected'], ['order', 'payment'])


if __name__ == '__main__':
    unittest.main()
