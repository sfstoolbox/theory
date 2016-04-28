#  === Makefile for SFS Toolbox documentation ===
#  
#  The documentation is compiled with Sphinx (http://www.sphinx-doc.org/).
#  It is splitted in four different parts that can be compiled independently
#  from each other:
#  
#  	theory 		- mathematical fundamentals of sound field synthesis
#  	matlab 		- documentation for the Matlab/Octave version of the SFS Toolbox
#  	python 		- documentation for the Python version of the SFS Toolbox
#  	code_references - explöanation of links in the code to the theory
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
SOURCEDIR     = .
BUILDDIR      = ./_build
VERSION       = $(shell python ./_include/version.py)

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don not have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS)

.PHONY: help clean html html-preview latex latexpdf linkcheck

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean         to delete previous builds"
	@echo "  html          to make web page ready files"
	@echo "  html-preview  to make HTML files for better preview on localhost"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  linkcheck  to check all external links for integrity"

clean:
	rm -rf $(BUILDDIR)/*

html-preview:
	$(SPHINXBUILD) -b html -A web=0 $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html-preview/$(VERSION)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html-preview/$(VERSION)."

html:
	$(SPHINXBUILD) -b dirhtml -A web=1 $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html/$(VERSION)
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html/$(VERSION)."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/latex/$(VERSION)
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex/$(VERSION)."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/latex/$(VERSION)
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex/$(VERSION) all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex/$(VERSION)."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

