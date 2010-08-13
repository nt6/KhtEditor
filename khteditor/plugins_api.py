import sys
import os

class Plugin(object):
    capabilities = []

    def __repr__(self):
        return '<%s %r>' % (
            self.__class__.__name__,
            self.capabilities
        )

def get_plugins_by_capability(capability):
    result = []
    for plugin in Plugin.__subclasses__():
        if capability in plugin.capabilities:
            result.append(plugin)
    return result

def load_plugins(plugins):
    for plugin in plugins:
        __import__(plugin, None, None, [''])


def init_plugin_system(cfg):
    for path in cfg['plugin_path']:
        if not path in sys.path:
            sys.path.insert(0, path)
            print 'added to sys path',path
    load_plugins(cfg['plugins'])


def find_plugins():
    return Plugin.__subclasses__()