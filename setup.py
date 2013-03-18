from distutils.core import setup
import loading

setup(
    name='django-loading',
    version=__loading__,
    packages=['loading'],
    license='BSD',
    long_description=open('README.txt').read(),
)
