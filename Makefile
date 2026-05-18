PYTHON ?= python3
SPHINXOPTS ?=
SOURCEDIR = docs/source
BUILDDIR = docs/_build

.PHONY: help doxygen html strict linkcheck clean

help:
	@$(PYTHON) -m sphinx.cmd.build -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

doxygen:
	./tools/build-doxygen.sh

html:
	$(PYTHON) -m sphinx.cmd.build -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

strict:
	$(PYTHON) -m sphinx.cmd.build -b html -W --keep-going "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

linkcheck:
	$(PYTHON) -m sphinx.cmd.build -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck" $(SPHINXOPTS)

clean:
	rm -rf "$(BUILDDIR)" docs/doxygen/build
