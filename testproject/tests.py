import os
import unittest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")


class DjangoLoading(unittest.TestCase):

    def test_0010_import_loading(self):
        import loading
        assert(loading)

    def test_0020_import_loading(self):
        import loading.apps
        assert(loading.apps)

    def test_0030_import_normal(self):
        import testproject.apps.app1 as m1
        assert(m1)

    def test_0040_import_app_module(self):
        import testproject.apps.app1 as m1
        import loading.apps.app1 as m2
        self.assertIs(m1, m2)

    def test_0050_import_app_models(self):
        import testproject.apps.app1.models as m1
        import loading.apps.app1.models as m2
        self.assertIs(m1, m2)

    def test_0060_import_app_models_from(self):
        import testproject.apps.app1.models as m1
        from loading.apps.app1 import models as m2
        self.assertIs(m1, m2)

    def test_0070_import_app_model(self):
        from testproject.apps.app1.models import TestModel as m1
        from loading.apps.app1.models import TestModel as m2
        self.assertIs(m1, m2)
