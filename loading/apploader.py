import sys
import imp


class AppLoader(object):

    package = "".join(__name__.split(".")[:-1])

    def __init__(self):
        super(AppLoader, self).__init__()
        self.__apps = None

    def register(self):
        sys.meta_path.append(self)

    def find_module(self, fullname, path):
        if fullname == self.package + '.apps':
            return self
        if fullname.startswith(self.package + '.apps'):
            return self

    def load_module(self, fullname):
        if fullname == self.package + '.apps':
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
            mod.__file__ = '<not-from-file>'
            mod.__loader__ = self
            mod.__path__ = []
            mod.__package__ = fullname
            return mod
        else:
            app_name = fullname.split('.')[2]
            app_path = self.get_app_path(app_name)
            import_path = '.'.join([app_path] + fullname.split('.')[3:])
            __import__(import_path)
            sys.modules[fullname] = sys.modules[import_path]
            return sys.modules[import_path]

    def get_app_path(self, name):
        if self.__apps is None:
            from django.conf import settings
            self.__apps = {}
            for app_path in settings.INSTALLED_APPS:
                app_name = app_path.split('.')[-1]
                self.__apps[app_name] = app_path
        return self.__apps[name]
