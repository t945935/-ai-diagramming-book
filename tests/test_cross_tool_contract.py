"""Fixture-specific shared call topology, not a general D2 parser/converter."""
import os
from pathlib import Path
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(os.environ.get('BOOK_SOURCE_ROOT', Path(__file__).resolve().parents[1]))


class CrossToolContractTests(unittest.TestCase):
    def test_d2_drawio_share_the_declared_call_endpoints(self):
        expected = {('browser', 'web'), ('web', 'order_api'),
                    ('order_api', 'external_payment'), ('order_api', 'order_store')}
        d2_ids = {'client': 'browser', 'platform.web': 'web',
                  'platform.orders': 'order_api', 'external.payment': 'external_payment',
                  'platform.db': 'order_store'}
        drawio_ids = {'client': 'browser', 'web': 'web', 'orders': 'order_api',
                      'payment': 'external_payment', 'db': 'order_store'}
        source = (ROOT / 'examples/d2/order-platform/order-platform.d2').read_text(encoding='utf-8')
        d2_edges = []
        for line in source.splitlines():
            if '->' not in line:
                continue
            match = re.fullmatch(r'\s*([\w.]+)\s*->\s*([\w.]+)\s*:\s*(.+)', line)
            self.assertIsNotNone(match, 'Unsupported fixture connection syntax: ' + line)
            d2_edges.append((d2_ids[match[1]], d2_ids[match[2]]))
        model = ET.parse(ROOT / 'examples/drawio/order-platform/order-platform.drawio')
        cells = model.findall('.//mxCell')
        vertices = {c.get('id') for c in cells if c.get('vertex') == '1'}
        drawio_edges = []
        for cell in cells:
            if cell.get('edge') == '1':
                self.assertIn(cell.get('source'), vertices)
                self.assertIn(cell.get('target'), vertices)
                drawio_edges.append((drawio_ids[cell.get('source')], drawio_ids[cell.get('target')]))
        self.assertEqual(len(d2_edges), len(expected), 'D2 edge count differs')
        self.assertEqual(len(drawio_edges), len(expected), 'draw.io edge count differs')
        self.assertEqual(set(d2_edges), expected, 'D2 topology differs from contract')
        self.assertEqual(set(drawio_edges), expected, 'draw.io topology differs from contract')


if __name__ == '__main__':
    unittest.main()
