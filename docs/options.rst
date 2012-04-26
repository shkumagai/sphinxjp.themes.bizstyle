================
 conf.py sample
================

Sample
======

.. code-block:: python

    # -*- coding: utf-8 -*-
    source_suffix = '.rst'
    master_doc = 'index'
    
    project = u'Business style theme sample'
    version = release = '0.1.0'
    copyright = u'2011, FooBar inc.'
    
    ################################################################
    # Extension and Theme setting
    # You need to install `easy_install sphinxjp.themes.bizstyle`
    
    extensions = ['sphinxjp.themecore']
    html_theme = 'bizstyle'
    
    ################################################################
    # HTML theme optinos for `bizstyle` theme
    
    html_theme_options = {
        'rightsidebar': False,
    }


HTML theme options
==================

:rightsidebar:
    Put the sidebar on the right side. Defaults to false.
