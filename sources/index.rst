.. _model-based-rendering:

Model-Based Rendering
---------------------

Knowing the pressure field of the desired source :math:`S(\x,\w)` is required in
order to derive the driving signal for the secondary source distribution. It can
either be measured, i.e. recorded, or modeled. While the former is known as
*data-based rendering*, the latter is known as *model-based rendering*.  For
data-based rendering, the problem of how to capture a complete sound field still
has to be solved. Avni et al. :cite:`Avni2013` discuss some influences of the
recording limitations on the perception of the reproduced sound field.  This
document will consider only model-based rendering.

Frequently applied models in model-based rendering are plane waves, point
sources, or sources with a prescribed complex directivity. In the following the
models used within the SFS Toolbox are presented.

.. plot::
    :context: reset
    :include-source: false

    import numpy as np
    import matplotlib.pyplot as plt
    import sfs
    plt.rcParams['figure.figsize'] = 8, 4.5  # inch


.. _sec-plane-wave:

Plane Wave
~~~~~~~~~~

.. plot::
    :context: close-figs

    nk = sfs.util.direction_vector(np.radians(45))  # direction of plane wave
    xs = 0, 0, 0  # center of plane wave
    omega = 2 * np.pi * 800  # frequency
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    p = sfs.mono.source.plane(omega, xs, nk, grid)
    sfs.plot.soundfield(p, grid);

.. _fig-plane-wave:

.. figure:: ../img/placeholder.png
    :align: center

    Sound pressure for a monochromatic plane wave :eq:`S.pw` going into the direction
    :math:`(1, 1, 0)`. Parameters: :math:`f = 800` Hz.

The source model for a plane wave is given after :cite:`Williams1999`,
eq. (2.24) [#F1]_ as

.. math::
    :label: S.pw

    S(\x,\w) = A(\w) \e{-\i\wc \scalarprod{\n_k}{\x}},

where :math:`A(\w)` denotes the frequency spectrum of the source and
:math:`\n_k` a unit vector pointing into the direction of the plane wave.

Transformed in the temporal domain this becomes

.. math::
    :label: s.pw

    s(\x,t) = a(t) * \dirac{t -\frac{\scalarprod{\n_k}{\x}}{c}},

where :math:`a(t)` is the Fourier transformation of the frequency spectrum
:math:`A(\w)`.

The expansion coefficients for spherical basis functions are given after
:cite:`Ahrens2012`, eq. (2.38) as

.. math::
    :label: plane-wave-spherical-coefficients

    \breve{S}_n^m(\theta_k,\phi_k,\w) = 4\pi\i^{-n}
        Y_n^{-m}(\theta_k,\phi_k),

where :math:`(\phi_k,\theta_k)` is the radiating direction of the plane wave.

In a similar manner the expansion coefficients for circular basis functions are
given as

.. math::
    :label: plane-wave-circular-coefficients

    \breve{S}_m(\phi_\text{s},\w) = \i^{-n}
        \Phi_{-m}(\phi_\text{s}).

The expansion coefficients for linear basis functions are given after
:cite:`Ahrens2012`, eq. (C.5) as

.. math::
    :label: plane-wave-linear-coefficients

    \breve{S}(k_x,y,\w) = 2\pi\dirac{k_x-k_{x,\text{s}}}
        \chi(k_{y,\text{s}},y),

where :math:`(k_{x,\text{s}},k_{y,\text{s}})` points into the radiating
direction of the plane wave.


.. _sec-point-source:

Point Source
~~~~~~~~~~~~

.. plot::
    :context: close-figs

    xs = 0, 0, 0  # position of source
    omega = 2 * np.pi * 800  # frequency
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    p = sfs.mono.source.point(omega, xs, [], grid)
    normalization = 4 * np.pi
    sfs.plot.soundfield(normalization * p, grid);

.. _fig-point-source:

.. figure:: ../img/placeholder.png
    :align: center

    Sound pressure for a monochromatic point source :eq:`S.ps` placed at :math:`(0, 0, 0)`.
    Parameters: :math:`f = 800` Hz.

The source model for a point source is given by the three dimensional Green’s
function after :cite:`Williams1999`, eq. (6.73) as

.. math::
    :label: S.ps

    S(\x,\w) = A(\w) \frac{1}{4\pi} \frac{\e{-\i
        \wc |\x-\xs|}}{|\x-\xs|},

where :math:`\xs` describes the position of the point source.

Transformed to the temporal domain this becomes

.. math::
    :label: s.ps

    s(\x,t) = a(t) * \frac{1}{4\pi} \frac{1}{|\x-\xs|}
        \dirac{t - \frac{|\x-\xs|}{c}}.

The expansion coefficients for spherical basis functions are given
after :cite:`Ahrens2012`, eq. (2.37) as

.. math::
    :label: point-source-spherical-coefficients

    \breve{S}_n^m(\theta_\text{s},\phi_\text{s},r_\text{s},\w) =
        -\i\wc
        \hankel{2}{n}{\wc r_\text{s}}
        Y_n^{-m}(\theta_\text{s},\phi_\text{s}),

where :math:`(\phi_\text{s},\theta_\text{s},r_\text{s})` describes the position
of the point source.

The expansion coefficients for linear basis functions are given after
:cite:`Ahrens2012`, eq. (C.10) as

.. math::
    :label: point-source-linear-coefficients

    \breve{S}(k_x,y,\w) =
        -\frac{\i}{4}
        \Hankel{2}{0}{\sqrt{(\tfrac{\w}{c})^2-k_x^2} \; |y-y_\text{s}|}
        \chi(-k_x,x_\text{s}),

for :math:`|k_x|<|\wc |` and with :math:`(x_\text{s},y_\text{s})`
describing the position of the point source.


.. _sec-dipole-point-source:

Dipole Point Source
~~~~~~~~~~~~~~~~~~~

.. plot::
    :context: close-figs

    xs = 0, 0, 0  # position of source
    ns = sfs.util.direction_vector(0)  # direction of source
    omega = 2 * np.pi * 800  # frequency
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    p = sfs.mono.source.point_dipole(omega, xs, ns, grid)
    sfs.plot.soundfield(p, grid);

.. _fig-dipole-point-source:

.. figure:: ../img/placeholder.png
    :align: center

    Sound pressure for a monochromatic dipole point source :eq:`S.dps` placed at
    :math:`(0, 0, 0)` and pointing towards :math:`(1, 0, 0)`.  Parameters:
    :math:`f = 800` Hz.

The source model for a three dimensional dipole source is given by the
directional derivative of the three dimensional Green’s function with respect to
:math:`{\n_\text{s}}` defining the orientation of the dipole source.

.. math::
    :label: S.dps

    \begin{aligned}
        S(\x,\w) &= A(\w) \frac{1}{4\pi}
            \scalarprod{\nabla_{\xs} \frac{\e{-\i
            \wc |\x-\xs|}}{|\x-\xs|}}{\n_\text{s}} \\
        &=
            A(\w) \frac{1}{4\pi}
            \left( \frac{1}{|\x-\xs|} + \i\wc \right)
            \frac{\scalarprod{\x-\xs}{\n_\text{s}}}{|\x-\xs|^2}
            \e{-\i\wc |\x-\xs|}. \\
    \end{aligned}

Transformed to the temporal domain this becomes

.. math::
    :label: s.dps

    s(\x,t) = a(t) *
        \left( \frac{1}{|\x-\xs|} + {\mathcal{F}^{-1}\left\{
        \frac{\i\w}{c} \right\}} \right) *
        \frac{\scalarprod{\x-\xs}{\n_\text{s}}}{4\pi|\x-\xs|^2}
        \dirac{t - \frac{|\x-\xs|}{c}}.


.. _sec-line-source:

Line Source
~~~~~~~~~~~

.. plot::
    :context: close-figs

    xs = 0, 0, 0  # position of source
    omega = 2 * np.pi * 800  # frequency
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    p = sfs.mono.source.line(omega, xs, None, grid)
    normalization = np.sqrt(8 * np.pi * omega / sfs.defs.c) * np.exp(1j * np.pi / 4)
    sfs.plot.soundfield(normalization * p, grid);

.. _fig-line-source:

.. figure:: ../img/placeholder.png
    :align: center

    Sound pressure for a monochromatic line source :eq:`S.ls` placed at :math:`(0, 0, 0)`.
    Parameters: :math:`f = 800` Hz.

The source model for a line source is given by the two dimensional Green’s
function after :cite:`Williams1999`, eq. (8.47) as

.. math::
    :label: S.ls

    S(\x,\w) = -A(\w) \frac{\i}{4} \Hankel{2}{0}{\wc |\x-\xs|}.

Applying the large argument approximation of the Hankel function
:cite:`Williams1999`, eq. (4.23) and transformed to the temporal domain this
becomes

.. math::
    :label: s.ls

    s(\x,t) = a(t) * \mathcal{F}^{-1}\left\{\sqrt{
        \frac{c}{\i\w}}\right\} * \sqrt{\frac{1}{8\pi}}
        \frac{1}{\sqrt{|\x-\xs|}}
        \dirac{t - \frac{|\x-\xs|}{c}}.

The expansion coefficients for spherical basis functions are given
after :cite:`Hahn2015`, eq. (15) as

.. math::
    :label: line-source-spherical-coefficients

    \breve{S}_n^m(\phi_\text{s},r_\text{s},\w) =
        -\pi \i^{m-n+1}
        \Hankel{2}{m}{\wc r_\text{s}}
        Y_n^{-m}(0,\phi_\text{s}).

The expansion coefficients for circular basis functions are given as

.. math::
    :label: line-source-circular-coefficients

    \breve{S}_m(\phi_\text{s},r_\text{s},\w) = -\frac{\i}{4}
        \Hankel{2}{m}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s}).

The expansion coefficients for linear basis functions are given as

.. math::
    :label: line-source-linear-coefficients

    \breve{S}(k_x,y_\text{s},\w) = -\frac{\i}{2}
        \frac{1}{\sqrt{(\wc )^2-k_x^2}}
        \chi(k_y,y_\text{s}).


.. [#F1]
    Note that :cite:`Williams1999` defines the Fourier transform with transposed signs
    as :math:`F(\w) = \int f(t) \e{\i\w t}`. This leads also to changed signs in
    his definitions of the Green’s functions and field expansions.

.. vim: filetype=rst spell:
