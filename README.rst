============
Easy Logging
============


.. image:: https://img.shields.io/pypi/v/easylogging.svg
        :target: https://pypi.python.org/pypi/easylogging

.. image:: https://img.shields.io/travis/vpoulailleau/easylogging.svg
        :target: https://travis-ci.org/vpoulailleau/easylogging

.. image:: https://readthedocs.org/projects/easylogging/badge/?version=latest
        :target: https://easylogging.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Logging made easy, no excuse for any print call.


* Free software: BSD license
* Documentation: https://easylogging.readthedocs.io.


Features
--------

* Easy logging setup
* Based on Python logging module

Example
-------

example_module.py
.................

.. code-block:: python
        import easylogging

        log = easylogging.get_logger()


        def log_some_messages():
        log.debug("## some debug ##")
        log.info("## some info ##")
        log.warning("## some warning ##")
        log.error("## some error ##")

main.py
.......

.. code-block:: python
        import easylogging
        import example_module

        # log = easylogging.get_logger(console_level=easylogging.DEBUG)
        # log = easylogging.get_logger(file_name="log.txt")
        log = easylogging.get_logger()

        a_variable = "a nice variable"
        another_variable = 42

        log.error("---- normal logging ----")
        log.debug("a debug message")
        log.info("an info")
        log.warning("a warning")
        log.error("%s and %d", a_variable, another_variable)

        log.error("---- example_module writes to the log ----")
        example_module.log_some_messages()

        log.error("---- reduced logging (bye debug and info messages) ----")
        easylogging.reduced_logging(log)
        log.debug("a debug message")
        log.info("an info")
        log.warning("a warning")
        log.error("an error")

        log.error("---- full logging (welcome back debug and info messages) ----")
        easylogging.full_logging(log)
        log.debug("a debug message")
        log.info("an info")
        log.warning("a warning")
        log.error("an error")


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
