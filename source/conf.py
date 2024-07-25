# conf.py
import furo

project = 'CrossGL'
author = 'CrossGL Team'
release = '0.0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]


html_logo = '_static/logo.png' 
html_theme = 'furo'

html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]

templates_path = ['_templates']
exclude_patterns = []


html_theme_options = {
    "sidebar_hide_name": False, 
    "navigation_with_keys": True,  
    "hide_toc": False
}