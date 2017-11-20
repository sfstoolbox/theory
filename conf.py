# -*- coding: utf-8 -*-

import sys
import os
import subprocess
import sphinx_rtd_theme
# Allow import/extensions from current path
sys.path.insert(0, os.path.abspath('.'))
from definitions import acronyms     # This includes things like |HRTF|
from definitions import latexmacros  # Math definitions like \x


# -- GENERAL -------------------------------------------------------------

project = 'SFS Toolbox'
copyright = '2016-2017, SFS Toolbox Developers'
author = 'SFS Toolbox Developers'

needs_sphinx = '1.3'  # minimal sphinx version
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'mathjax',  # Modified version to include clickable eq numbers and
                    # avoid the ugly looking standard result. There is also
                    # a pull request for this:
                    # https://github.com/rtfd/sphinx_rtd_theme/pull/383
        #'sphinx.ext.mathjax',
        'matplotlib.sphinxext.plot_directive'
]
master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['_build']
# The full version, including alpha/beta/rc tags.
#release = version
try:
    release = subprocess.check_output(
            ('git', 'describe', '--tags', '--always'))
    release = release.decode().strip()
except Exception:
    release = '<unknown>'


# -- FIGURES AND CODE ----------------------------------------------------

# Enable numbering of figures and tables
numfig = True
math_numfig = True
# Plot settings for matplot
plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ['png']
plot_rcparams = {'figure.figsize': [8, 4.5]}
# Code syntax highlighting style
pygments_style = 'trac'


# -- ACRONYMS AND MATH ---------------------------------------------------

def rst2tex(rst_macros):
    """Converts a rst math definition to a LaTeX preamble"""
    macros = [line.lstrip() for line in rst_macros.split('\n')[3:-2]]
    macros = '\n'.join(macros) + '\n'
    return macros

# Append acronyms at the end of every pag
rst_epilog = acronyms
# Append at the beginning of every page ofr mathjax
# This is a workaround as there is now mathjax preamble yet:
# https://github.com/sphinx-doc/sphinx/issues/726
rst_prolog = latexmacros
LATEX_PREAMBLE = rst2tex(latexmacros)  # for LaTeX preamble, see bottom


# -- HTML ----------------------------------------------------------------

def setup(app):
    """Include custom theme files to sphinx HTML header"""
    app.add_stylesheet('css/abbr.css')

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {'display_version': False}
html_title = "SFS Toolbox"
html_short_title = ""
html_show_sphinx = False
htmlhelp_basename = 'sfs-doc'


# -- LATEX ---------------------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': LATEX_PREAMBLE,  # command definitions
    'figure_align': 'htbp',
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
