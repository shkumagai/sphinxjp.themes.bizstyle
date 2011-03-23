# -*- coding: utf-8 -*-
#
# -- General configuration -----------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'sphinx theme for R-Style'
copyright = u'2011, Rakuten Inc.'

version = '0.1.0'

# -- Options for HTML output ---------------------------------------------------

extensions = ['sphinxjp.themecore']
html_theme = 'rstyle'

html_theme_options = {
    'rightsidebar': False,
}

