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
    "hide_toc": False,
    "light_css_variables": {
        "color-brand-primary": "#3d94ff",  
        "color-brand-content": "#000000",
        "color-background-primary": "#3d94ff",  
        "color-background-secondary": "#1a1a1a",
        "color-foreground-primary": "#f8f8f2",
        "color-foreground-secondary": "#ccc",
        "color-foreground-muted": "#999",
        "color-link": "#1e90ff",
        "color-link--hover": "#ff4500",
        "color-background-hover": "#333",
        "color-background-border": "#444",
    },
    "dark_css_variables": {
        "color-brand-primary": "#3d94ff", 
        "color-brand-content": "#000000",
        "color-background-primary": "#3d94ff",  
        "color-background-secondary": "#1a1a1a",
        "color-foreground-primary": "#f8f8f2",
        "color-foreground-secondary": "#ccc",
        "color-foreground-muted": "#999",
        "color-link": "#1e90ff",
        "color-link--hover": "#ff4500",
        "color-background-hover": "#333",
        "color-background-border": "#444",
    },
}
