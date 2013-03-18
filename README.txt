===========
django-loading
===========

django-loading allows you to load your django apps by their app name rather
than by the module path. This is particularly useful if you don't know where
modules will be installed or if you plan to allow overriding of your apps (eg
a user replaces your ``foo.bar`` app with ``myfoo.bar``).


Usage
=====

If you have a django app called ``bar`` in a package called ``foo`` (such that
you would add ``foo.bar`` to your INSTALLED_APPS) then you can get hold of
``bar`` without knowing its full module path::

    import loading
    foo = loading.apps.bar

    # load a model:
    MyModel = foo.models.MyModel

Your app names in a django project should all be unqiue, django-loading won't
work if they are not (but django won't like that either).


Installation
============

Use your favorite install method, for example:

    $ pip install django-loading

You do not need to add django-loading to your INSTALLED_APPS.
