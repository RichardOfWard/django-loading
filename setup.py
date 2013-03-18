from setuptools import setup, find_packages
import loading

setup(
    name='django-loading',
    version=loading.__version__,
    packages=['loading'],
    license='BSD',
    description='Load your django apps by app name rather than module path.',
    long_description=open('README.rst').read(),
    author='Richard Ward',
    author_email='richard@richard.ward.name',
    url='https://github.com/RichardOfWard/django-loading',
    test_suite='testproject.tests',
    tests_require=['django'],
    include_package_data=True,
    zip_safe=False,
) 
