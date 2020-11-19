.. image:: https://github.com/ome/scc/workflows/Tox/badge.svg
    :target: https://github.com/ome/scc/actions

.. image:: https://badge.fury.io/py/scc.svg
    :target: https://badge.fury.io/py/scc

SCC
===

Introduction
------------

The scc command provides tools for simplifying the Git(Hub) workflow.

Dependencies
------------

Direct dependencies of scc are:

- `PyGithub`_

Installation
------------

To install ``scc``, run::

 $ python setup.py install

or using pip, run::

 $ pip install scc

To upgrade your pip installation, run::

 $ pip install -U scc

Usage
-----

The list of available commands can be listed with::

  $ scc -h

For each subcommand, additional help can be queried, e.g.::

  $ scc merge -h

Contributing
------------

PyGithub follows `PEP 8`_, the Style Guide for Python Code. Please check your
code with pep8_ or flake8_, the Python style guide checkers, by running
``flake8 -v .`` or ``pep8 -v .``.

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/


Running tests
-------------

The tests are located under the `test` directory. To run all the tests, use
the `test` target of `setup.py`::

  python setup.py test

Unit tests
^^^^^^^^^^

Unit tests are stored under the `test/unit` folder and can be run by calling::

  python setup.py test -t test/unit

Unit tests are also run by the Travis_ build on every Pull Request opened
against the main repository.

Integration tests
^^^^^^^^^^^^^^^^^

Integration tests are stored under `test/integration`. Many integration tests
use snoopys-sandbox_ and snoopys-sandbox-2_ as sandbox repositories to test the
scc commands.

Running the integration test suite requires:

- a GitHub account
- a token-based GitHub connection, i.e. a ``github.token`` stored under
  the local Git configuration file (a global token is ignored)::

    $ git config github.token xxxx

- the user authenticated by the token defined above needs to own forks of
  snoopys-sandbox_ and snoopys-sandbox-2_

Once this is set up, the integration tests can be run by calling::

  python setupy.py test -s test/integration


License
-------

scc is released under the GPL.

Copyright
---------

2012-2019, The Open Microscopy Environment

.. _PyGithub: https://github.com/PyGithub/PyGithub
.. _pep8: https://pypi.python.org/pypi/pep8
.. _flake8: https://pypi.python.org/pypi/flake8
.. _snoopys-sandbox: https://github.com/ome/snoopys-sandbox
.. _snoopys-sandbox-2: https://github.com/ome/snoopys-sandbox-2
.. _Travis: https://travis-ci.org/ome/scc

