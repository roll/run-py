from ..helpers import PluginImporter
importer = PluginImporter(virtual='run.plugins.', actual='run_')
importer.register()
del PluginImporter
del importer
