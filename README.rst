================================
NeuroVault Collection Downloader
================================


.. image:: https://img.shields.io/pypi/v/neurovault_collection_downloader.svg
        :target: https://pypi.python.org/pypi/neurovault_collection_downloader

.. image:: https://img.shields.io/travis/chrisfilo/neurovault_collection_downloader.svg
        :target: https://travis-ci.org/chrisfilo/neurovault_collection_downloader

.. image:: https://readthedocs.org/projects/neurovault-collection-downloader/badge/?version=latest
        :target: https://neurovault-collection-downloader.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




CLI tool for bulk downloads of NeuroVault data.


* Free software: Apache Software License 2.0
* Documentation: https://neurovault-collection-downloader.readthedocs.io.


Installation
------------

```
pip install git+https://github.com/NeuroVault/neurovault_collection_downloader.git
```

Usage
-----

1. Create a text file with one collection ID (a number or string of capital letters in case of private collection) per line.
2. `neurovault_collection_downloader collections.txt /output_directory

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
