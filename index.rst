Welcome to the Sound Field Synthesis Toolbox
============================================

.. image:: img/header.png
    :align: center
 
Sound field synthesis (SFS) includes methods that try to generate a defined
sound field in an extended area that is surrounded by loudspeakers. This project
focuses on those methods that provide analytical solutions to the underlying
mathematical problem, namely |WFS|, |NFC-HOA|, and the |SDM|.

The SFS Toolbox project is structured in the following three sub-projects.

Overview and Theory:
    http://sfstoolbox.org (current page)

SFS Toolbox for Matlab/Octave:
    http://matlab.sfstoolbox.org

SFS Toolbox for Python:
    http://python.sfstoolbox.org

The Toolboxes provide you with the implementation of the underlying mathematics.
You can make numerical simulations of the resulting sound fields and can even
create binaural simulations of the same sound fields. This enables you to listen
to large loudspeaker arrays, even if you don’t have one in your laboratory or at
home. In addition, you can easily plug-in your own algorithms in order to test
or compare them.

Most of the figures in the :ref:`theory section <theory>` are directly created
by the SFS Toolbox for Python. All of them display the corresponding code for
creating them directly before the actual figure. In order to recreate them, you
have to execute the following code first:

.. Common plotting settings
.. plot::
    :context: reset

    import numpy as np
    import matplotlib.pyplot as plt
    import sfs
    plt.rcParams['figure.figsize'] = 8, 4.5  # inch

The image at the top of the page is extracted from :cite:`Zotter2013`.

----

The following presentation of the theory is based on Chap. 2 from
:cite:`Wierstorf2014`.

.. _theory:

.. toctree::
    :maxdepth: 3
    :caption: Theory

    defs/index
    problem/index
    nfchoa/index
    wfs/index
    dims/index
    sources/index
    d_nfchoa/index
    d_wfs/index
    d_lsfs/index
    refs/index
    
.. vim: filetype=rst spell:
