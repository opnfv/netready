#
# Copyright (c) 2016 Ericsson and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
#
# http://www.apache.org/licenses/LICENSE-2.0
#

#
# What this is: Configuration file for OPNFV NetReady requirements
# documentation based on the configuration file used by the Copper project.
#
import datetime
import sys
import os
import subprocess

try:
    __import__('imp').find_module('sphinx.ext.numfig')
    extensions = ['sphinx.ext.numfig']
except ImportError:
    # 'pip install sphinx_numfig'
    extensions = ['sphinx_numfig']

try:
    __import__('imp').find_module('sphinxcontrib-fulltoc')
except ImportError:
    subprocess.call("pip install sphinxcontrib-fulltoc", shell=True)
extensions.append('sphinxcontrib-fulltoc')

# numfig:
number_figures = True
figure_caption_prefix = "Fig."

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_use_index = True
html_theme = 'sphinx_rtd_theme'

pdf_documents = [('index', u'OPNFV', u'OPNFV NetReady Project', u'OPNFV')]
pdf_fit_mode = "shrink"
pdf_stylesheets = ['sphinx','kerning','a4']
#latex_domain_indices = False
#latex_use_modindex = False

latex_elements = {
    'printindex': '',
}
