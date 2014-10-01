******
azcat
******

.. image:: https://drone.io/github.com/nuta/azcat/status.png
    :alt: Build Status

.. image:: https://badge.fury.io/py/azcat.svg
    :target: http://badge.fury.io/py/azcat

azcat is a alternaive to ``cat(1)``; specialized for printing. It prints files with syntax
highlighting and formatting.

.. image:: https://raw.githubusercontent.com/nuta/azcat/master/demo.gif

============
Installation
============
.. code-block:: bash

    $ pip install azcat

=====
Usage
=====
.. code-block:: bash

    $ az --help # manual
    $ az /usr/local/bin/az
    $ az README.md
    $ az --with-formatter timetable.csv | az # pretty printing
    $ curl example.com/api/foo.json | az

=======
License
=======
azcat is a public domain software.

============
Contributors
============
- `Seiya Nuta <https://github.com/nuta>`_: Author
- `Alessandro Pisa <https://github.com/ale-rt>`_: PR `#3 <https://github.com/nuta/azcat/pull/3>`_
- `Simeon Visser <https://github.com/svisser>`_: PR `#7 <https://github.com/nuta/azcat/pull/7>`_

============
Contributing
============
Please send a Pull Request on GitHub. I will be very happy whatever the PR does :)
