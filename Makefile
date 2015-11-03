# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build
VERSION       = $(shell python version.py)

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don not have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest coverage gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  latexpdfja to make LaTeX files and run them through platex/dvipdfmx"
	@echo "  man        to make manual pages"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  spelling   to run a spell check on your docs"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html -A web=0 $(ALLSPHINXOPTS) $(BUILDDIR)/html/$(VERSION)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html/$(VERSION)."

dirhtml:
	$(SPHINXBUILD) -b dirhtml -A web=1 $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml/$(VERSION)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml/$(VERSION)."

singlehtml:
	$(SPHINXBUILD) -b singlehtml -A web=0 $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml/$(VERSION)
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml/$(VERSION)."

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub/$(VERSION)
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub/$(VERSION)."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex/$(VERSION)
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex/$(VERSION)."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex/$(VERSION)
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex/$(VERSION) all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex/$(VERSION)."

latexpdfja:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex/$(VERSION)
	@echo "Running LaTeX files through platex and dvipdfmx..."
	$(MAKE) -C $(BUILDDIR)/latex/$(VERSION) all-pdf-ja
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex/$(VERSION)."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man/$(VERSION)
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man/$(VERSION)."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes/$(VERSION)
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes/$(VERSION)."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

spelling:
	$(SPHINXBUILD) -b spelling $(ALLSPHINXOPTS) $(BUILDDIR)/spelling
	@echo
	@echo "Check finished. Wrong words can be found in " \
		"$(BUILDDIR)/spelling/output.txt."
