import os
import sphinx
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

    html_show_copyright = False

    @property
    def html_theme(self):
        if os.environ.get('READTHEDOCS', False):
            return 'default'
        return 'sphinx_rtd_theme'

    @property
    def html_theme_path(self):
        if os.environ.get('READTHEDOCS', False):
            return []
        import sphinx_rtd_theme
        return [sphinx_rtd_theme.get_html_theme_path()]

    # Autodoc

    autodoc_member_order = 'bysource'
    autodoc_default_flags = ['members', 'special-members', 'private-members']
    autodoc_skip_members = ['__weakref__']


locals().update(Settings(sphinx=sphinx))
