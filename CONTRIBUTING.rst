.. _contributing:

Contributing
------------

If you find errors, omissions, inconsistencies or other things that need
improvement, please create an issue or a pull request at
https://github.com/sfstoolbox/theory/.
Contributions are always welcome!


Installation of Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to build the theory section locally you should get the
newest development version from Github_ and install the needed dependencies
with::

   git clone https://github.com/sfstoolbox/theory.git
   cd theory
   python3 -m pip install --user -r requirements.txt

.. _Github: https://github.com/sfstoolbox/theory/

This way, your installation always stays up-to-date, even if you pull new
changes from the Github repository.


Building the Documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you make changes to the documentation, you can re-create the HTML and PDF
pages using Sphinx_.

To create the HTML pages, use::

   make html-preview

The generated files will be available in the directory
``_build/sphinx/html-preview/``.
To create the PDF pages, use::

    make latexpdf

The generated files will be available in the directory ``_build/sphinx/latex/``.

.. _Sphinx: http://sphinx-doc.org/


Creating a New Release
^^^^^^^^^^^^^^^^^^^^^^

New releases are made using the following steps:

#. Update ``NEWS.rst``
#. Commit those changes as "Release x.y.z"
#. Create an (annotated) tag with ``git tag -a x.y.z``
#. Push the commit and the tag to Github and `add release notes`_ containing
   the bullet points from ``NEWS.rst``
#. Check that the new release was built correctly on RTD_, and select the new
   release as default version

.. _add release notes: https://github.com/sfstoolbox/theory/releases/
.. _RTD: https://readthedocs.org/projects/sfs/builds/


Contributors
^^^^^^^^^^^^

The following individuals have contributed significantly to the Sound Field
Synthesis Toolbox. If you think more people should be listed here, feel free to
create a pull request.

=============== ============
Name            GitHub
=============== ============
Hagen Wierstorf `hagenw`_
Fiete Winter    `fietew`_
Matthias Geier  `mgeier`_
Frank Schultz   `fs446`_
Nara Hahn       `narahahn`_
Till Rettberg   `trettberg`_
Christoph Hold  `chris-hld`_
Vera Erbes      `VeraE`_
Sascha Spors    `spors`_
=============== ============

Furthermore, all github contributions can be found on the specific project
pages:

* https://github.com/sfstoolbox/theory/graphs/contributors
* https://github.com/sfstoolbox/sfs-matlab/graphs/contributors
* https://github.com/sfstoolbox/sfs-python/graphs/contributors


.. _hagenw: https://github.com/hagenw
.. _fietew: https://github.com/fietew
.. _mgeier: https://github.com/mgeier
.. _fs446: https://github.com/fs446
.. _narahahn: https://github.com/narahahn
.. _trettberg: https://github.com/trettberg
.. _chris-hld: https://github.com/chris-hld
.. _VeraE: https://github.com/VeraE
.. _spors: https://github.com/spors
