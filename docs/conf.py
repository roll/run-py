import os
import sphinx
import sphinx_rtd_theme
from box.sphinx import Settings
from box.importlib import import_file
metadata = import_file(os.path.join(os.path.dirname(__file__), 'metadata.py'))


class Settings(Settings):

    # Documentation:
    # http://sphinx-doc.org/config.html

    # General

    extensions = ['sphinx.ext.autodoc']
    master_doc = 'index'
    pygments_style = 'sphinx'

    # Project

    project = metadata.name
    version = metadata.version

    # HTML

    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_show_copyright = False

    # Autodoc

    autodoc_member_order = 'bysource'
    autodoc_default_flags = ['members', 'special-members', 'private-members']
    autodoc_skip_members = ['__weakref__']


locals().update(Settings(sphinx=sphinx))
