# -*- coding: utf-8 -*-

import sys
import os
import sphinx_rtd_theme
import subprocess

import sphinxcontrib.katex as katex

# Allow import/extensions from current path
sys.path.insert(0, os.path.abspath('.'))
from definitions import acronyms      # This includes things like |HRTF|
from definitions import latex_macros  # Math definitions like \x


# -- GENERAL -------------------------------------------------------------

project = 'Sound Field Synthesis'
copyright = '2016-2017, SFS Toolbox Developers'
author = 'SFS Toolbox Developers'

needs_sphinx = '1.3'   # minimal sphinx version
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinxcontrib.katex',
        'matplotlib.sphinxext.plot_directive'
]
master_doc = 'contents'
source_suffix = '.rst'
exclude_patterns = ['_build']

# The full version, including alpha/beta/rc tags.
#release = version
try:
    release = subprocess.check_output(
            ['git', 'describe', '--tags', '--always'])
    release = release.decode().strip()
except Exception:
    release = '<unknown>'


# -- FIGURES AND CODE ----------------------------------------------------

# Enable numbering of figures and tables
numfig = True
# Plot settings for matplot
plot_include_source = True
plot_html_show_source_link = False
plot_html_show_formats = False
plot_formats = ['png']
plot_rcparams = {'figure.figsize': [8, 4.5]}

# Code syntax highlighting style
pygments_style = 'trac'


# -- ACRONYMS AND MATH ---------------------------------------------------
rst_epilog = acronyms  # append acronyms to every page
katex_macros = katex.latex_defs_to_katex_macros(latex_macros)


# -- HTML ----------------------------------------------------------------

def setup(app):
    """Include custom theme files to sphinx HTML header"""
    app.add_stylesheet('css/abbr.css')
    app.add_stylesheet('css/math.css')

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {'display_version': True}
html_title = "SFS Toolbox"
html_short_title = ""
htmlhelp_basename = 'sfs-doc'


# -- LATEX ---------------------------------------------------------------

latex_elements = {
        'papersize': 'a4paper',
        'pointsize': '10pt',
        'preamble': latex_macros,  # command definitions
        'figure_align': 'htbp',
        'sphinxsetup': 'TitleColor={rgb}{0,0,0}, verbatimwithframe=false, VerbatimColor={rgb}{.96,.96,.96}',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc,
   'sfs-toolbox-documentation.tex',
   u'Theory of Sound Field Synthesis',
   u'SFS Toolbox Developers',
   'manual',
   True),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None
