# -*- coding: utf-8 -*-
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import datetime

# -- Project information -----------------------------------------------------

project = 'Prog2@UniMI'
copyright = '2018, Massimo Santini'
author = 'Massimo Santini'

version = ''
release = ''

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']

master_doc = 'index'

language = 'it'

exclude_patterns = ['**.ipynb_checkpoints']

smartquotes = False

# -- Options for HTML output -------------------------------------------------

html_theme = 'basic'

html_experimental_html5_writer = True

html_theme_options = {
    'nosidebar': True,
}

html_static_path = ['_static']

#html_sidebars = { '**': [], }

html_last_updated_fmt = '%-d/%-m/%y'

html_context = {
    'iso_now': datetime.datetime.utcnow().isoformat()
}

# -- Options for todo extension ----------------------------------------------

todo_include_todos = False
