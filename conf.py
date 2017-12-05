# -*- coding: utf-8 -*-

import sys
import os
import re
import subprocess

import sphinx_rtd_theme

# Allow import/extensions from current path
sys.path.insert(0, os.path.abspath('.'))
from definitions import acronyms     # This includes things like |HRTF|
from definitions import latexmacros  # Math definitions like \x


# -- GENERAL -------------------------------------------------------------

project = 'Sound Field Synthesis Toolbox'
copyright = '2016-2017, SFS Toolbox Developers'
author = 'SFS Toolbox Developers'

needs_sphinx = '1.3'  # minimal sphinx version
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinxcontrib.katex',  # Modified version to include clickable eq numbers and
                    # avoid the ugly looking standard result. There is also
                    # a pull request for this:
                    # https://github.com/rtfd/sphinx_rtd_theme/pull/383
        #'sphinx.ext.mathjax',
        'matplotlib.sphinxext.plot_directive',
        'sphinxcontrib.bibtex'
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
plot_formats = ['png', 'pdf']
plot_rcparams = {'figure.figsize': [8, 4.5]}
# Code syntax highlighting style
pygments_style = 'trac'


# -- ACRONYMS AND MATH ---------------------------------------------------

def latex_to_katex(macros):
    "Converts LaTeX \def statements to KaTeX macros"
    # Remove empty lines
    macros = macros.strip()
    tmp = []
    for line in macros.splitlines():
        # Remove spaces from every line
        line = line.strip()
        # Remove "\def" at the beginning of line
        line = re.sub(r'^\\def[ ]?', '', line)
        # Remove parameter before {} command definition
        line = re.sub(r'(#[0-9])+', '', line, 1)
        # Remove outer {} command brackets with ""
        line = re.sub(r'( {)|(}$)', '"', line)
        # Add "": to the new command
        line = re.sub(r'(^\\[A-Za-z]+)', r'"\1":', line, 1)
        # Add , at end of line
        line = re.sub(r'$', ',', line, 1)
        # Duplicate all \
        line = re.sub(r'\\', r'\\\\', line)
        tmp.append(line)
    macros = '\n'.join(tmp)
    return macros


# Append acronyms at the end of every pag
rst_epilog = acronyms

katex_macros = latex_to_katex(latexmacros)


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
html_show_sphinx = False
htmlhelp_basename = 'sfs-doc'


# -- LATEX ---------------------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': latexmacros,  # command definitions
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
