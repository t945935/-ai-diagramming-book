PYTHON ?= python3

.PHONY: check-core check-full audit-npm

# No external renderers or Python packages required.
check-core:
	$(PYTHON) -m unittest discover -s tests -p 'test_graphviz_generator.py' -v
	$(PYTHON) -m unittest discover -s tests -p 'test_cross_tool_contract.py' -v
	$(PYTHON) -m unittest discover -s tests -p 'test_refund_change.py' -v

# Requires Graphviz, Mermaid CLI and a working Chromium setup.
check-full:
	$(PYTHON) -m unittest discover -s tests -v

# Network-backed dependency advisory check; not a source/secret scan.
audit-npm:
	npm audit
