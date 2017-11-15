# -*- coding: utf-8 -*-

import sys
import os
import shlex
import sphinx_rtd_theme
#import subprocess

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))  # temporary, for plot_directive

from definitions import acronyms # This includes things like |HRTF| etc.
from definitions import latexmacros
rst_prolog = latexmacros # Append at the beginning of every page
rst_epilog = acronyms # Append at the end of every page

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['sphinx.ext.autodoc','nbsphinx','sphinx.ext.mathjax']
extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.viewcode',
        'mathjax', # modified version to include clickable eq numbers
        #'sphinx.ext.mathjax',
        'matplotlib.sphinxext.plot_directive'
]

# Enable numbering of figures and tables
numfig = True
math_numfig = True

# Plot settings for matplot
plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ['png']
plot_rcparams = {'figure.figsize' : [8, 4.5] }

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project. (substitutions)
project = 'Sound Field Synthesis'
copyright = '2016, SFS Toolbox Developers'
author = 'SFS Toolbox Developers'

# The full version, including alpha/beta/rc tags.
#release = version
try:
    release = check_output(['git', 'describe', '--tags', '--always'])
    release = release.decode().strip()
except Exception:
    release = '<unknown>'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
pygments_style = 'trac'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "SFS Toolbox"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = ""

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'sfs-doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'sfs-toolbox-documentation.tex', u'SFS Toolbox -- Theory',
   u'SFS Toolbox team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


