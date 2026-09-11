"""Generate a dependency overview and reverse-reachable impact graph.

Edges mean consumer -> dependency. Impact means potential review scope,
not proof of a runtime failure. Uses only the Python standard library.
"""
import argparse
import json
from pathlib import Path


def dot_text(nodes, edges, changed=None):
    quote = lambda value: json.dumps(value, ensure_ascii=False)
    lines = ['digraph dependencies {', '  graph [rankdir=LR, pad=0.3, nodesep=0.5, ranksep=0.8, fontname="Noto Sans CJK TC", fontsize=14, labelloc=b, label="A → B：A 依賴 B；影響分析反向追蹤。\\n潛在檢查範圍，不代表必然故障。"];',
             '  node [shape=box, style="rounded,filled", fillcolor="#e8f0fe", fontname="Noto Sans CJK TC", fontsize=16];',
             '  edge [color="#566573"];']
    for node in sorted(nodes):
        label = nodes[node] + ('（變更起點）' if node == changed else '')
        color = ', fillcolor="#ffe0b2"' if node == changed else ''
        lines.append(f'  {quote(node)} [label={quote(label)}{color}];')
    for source, target in sorted(edges):
        lines.append(f'  {quote(source)} -> {quote(target)};')
    return '\n'.join(lines + ['}', ''])


def generate(data, changed, out):
    if not isinstance(data, dict) or not isinstance(data.get('nodes'), dict) or not isinstance(data.get('edges'), list):
        raise ValueError('expected nodes mapping and edges list')
    nodes = data['nodes']
    if not nodes or any(not isinstance(k, str) or not k or not isinstance(v, str) or not v for k, v in nodes.items()):
        raise ValueError('node IDs and labels must be non-empty strings')
    if changed not in nodes:
        raise ValueError('changed node does not exist')
    for edge in data['edges']:
        if not isinstance(edge, list) or len(edge) != 2 or any(not isinstance(n, str) or n not in nodes for n in edge):
            raise ValueError('each edge must name two existing nodes')
    edges = sorted(set(tuple(edge) for edge in data['edges']))
    affected = {changed}
    pending = [changed]
    reverse = {node: [] for node in nodes}
    for source, target in edges:
        reverse[target].append(source)
    while pending:
        for consumer in reverse[pending.pop()]:
            if consumer not in affected:
                affected.add(consumer)
                pending.append(consumer)
    selected = [(a, b) for a, b in edges if a in affected and b in affected]
    out.mkdir(parents=True, exist_ok=True)
    (out / 'overview.dot').write_text(dot_text(nodes, edges), encoding='utf-8')
    (out / 'impact.dot').write_text(dot_text({n: nodes[n] for n in affected}, selected, changed), encoding='utf-8')
    report = {'changed': changed, 'affected': sorted(affected), 'edges': selected}
    (out / 'impact.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--changed', required=True)
    args = parser.parse_args()
    try:
        generate(json.loads(args.input.read_text(encoding='utf-8')), args.changed, args.output)
    except (ValueError, OSError) as error:
        parser.error(f'invalid input: {error}')


if __name__ == '__main__':
    main()
