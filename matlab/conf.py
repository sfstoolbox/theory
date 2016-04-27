# -*- coding: utf-8 -*-

import sys
import os
import shlex
import sphinx_rtd_theme
#import subprocess

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../_include'))

from acronyms import rst_epilog # This includes things like |HRTF| etc.
import version

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = ['sphinx.ext.autodoc','nbsphinx','sphinx.ext.mathjax']
extensions = [
	'sphinx.ext.autodoc',
        'mathjax',
	'sphinx.ext.viewcode',
	'matplotlib.sphinxext.only_directives',
	'matplotlib.sphinxext.plot_directive',
]

# Enable numbering of figures and tables
numfig = True

# Plot settings ofr matplot
plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ['png']
plot_rcparams = {'figure.figsize' : [8, 4.5] }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_theme/sfs/static/libweb']

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if 'spelling' in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = 'en_GB'

# Location of word list.
spelling_word_list_filename = 'spelling_wordlist'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project. (substitutions)
project = 'SFS Toolbox'
copyright = '2016, SFS Toolbox Team'
author = 'SFS Toolbox Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = version.get_version()

# The full version, including alpha/beta/rc tags.
release = version

html_context = {'versions': [('1.0', '1.0/'), ('latest', 'latest/')],
                'downloads': [('PDF', '/sfs-toolbox_matlab.pdf')],
                'home_url': 'http://sfstoolbox.org/doc/'}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
pygments_style = 'trac'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sfs"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["../_theme",sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "SFS Toolbox"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = ""

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "sfs2.ico"

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'sfs-doc'

# Appended to every page
rst_epilog = rst_epilog + """
.. |SFS Toolbox|     replace:: SFS Tooblox
"""

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
  (master_doc, 'sfs-toolbox_master.tex', u'SFS Toolbox',
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
