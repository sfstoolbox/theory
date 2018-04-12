.. _sec-nfchoa:

Special Geometries: NFC-HOA and SDM
-----------------------------------

The integral equation :eq:`single-layer` states a Fredholm equation of first
kind with a Green’s function as kernel. This type of equation can be solved in a
straightforward manner for geometries that have a complete set of orthogonal
basis functions.  Then the involved functions are expanded into the basis
functions :math:`\psi_n` after :cite:`Morse1981`, p. (940) as

.. math::
    :label: freq-greens-function-expansion

    G(\x-\x_0, \w) = \sum_{n} \tilde{G}_n(\w) \psi_n^*(\x_0) \psi_n(\x)

.. math::
    :label: freq-drivingfunction-expansion

    D(\x_0, \w) = \sum_n \tilde{D}_n(\w) \psi_n(\x_0)

.. math::
    :label: freq-source-expansion

    S(\x, \w) = \sum_n \tilde{S}_n(\w) \psi_n(\x),

where :math:`\tilde{G}_n, \tilde{D}_n, \tilde{S}_n` denote the series expansion
coefficients, :math:`n \in \mathbb{Z}`, and \ :math:`\langle\psi_n,
\psi_{n'}\rangle = 0\,` for :math:`n \ne n'`.
If the underlying space is not compact the equations will involve an integration
instead of a summation

.. math::
    :label: freq-greens-function-expansion-non-compact

    G(\x-\x_0, \w) = \int \tilde{G}(\mu, \w) \psi^*(\mu, \x_0)
        \psi(\mu, \x) \d\mu

.. math::
    :label: freq-drivingfunction-expansion-non-compact

    D(\x_0, \w) = \int \tilde{D}(\mu, \w) \psi(\mu, \x_0) \d\mu

.. math::
    :label: freq-source-expansion-non-compact

    S(\x, \w) = \int \tilde{S}(\mu, \w) \psi(\mu, \x) \d\mu,

where :math:`\d\mu` is the measure in the underlying space.
Introducing these equations into :eq:`single-layer` one gets

.. math::
    :label: freq-drivingfunction-hoa

    \tilde{D}_n(\w) =
        \frac{\tilde{S}_n(\w)}{\tilde{G}_n(\w)}.

This means that the Fredholm equation :eq:`single-layer` states a convolution.
For geometries where the required orthogonal basis functions exist,
:eq:`freq-drivingfunction-hoa` follows directly via the convolution theorem
:cite:`Arfken2005`, eq. (1013).  Due to the division of the desired sound field
by the spectrum of the Green’s function this kind of approach has been named
|SDM| :cite:`Ahrens2010`.  For circular and spherical geometries the term
|NFC-HOA| is more common due to the corresponding basis functions. “Near-field
compensated” highlights the usage of point sources as secondary sources in
contrast to Ambisonics and |HOA| that assume plane waves as secondary sources.

The challenge is to find a set of basis functions for a given geometry.
In the following paragraphs three simple geometries and their widely
known sets of basis functions will be discussed.


.. _sec-spherical-geometries:

Spherical Geometries
~~~~~~~~~~~~~~~~~~~~

The spherical harmonic functions constitute a basis for a spherical secondary
source distribution in :math:`{\mathbb{R}}^3` and can be defined after
:cite:`Gumerov2004`, eq. (12.153) [#F1]_ as

.. math::
    :label: spherical-harmonics

    \begin{gathered}
        Y_n^m(\theta,\phi) = (-1)^m \sqrt{\frac{(2n+1)(n-|m|)!}{4\pi(n+|m|)!}}
        P_n^{|m|}(\sin\theta) \e{\i m\phi} \; \\
        n = 0,1,2,... \;\;\;\;\;\; m = -n,...,n
    \end{gathered}

where :math:`P_n^{|m|}` are the associated Legendre functions. Note that
this function may also be defined in a slightly different way, omitting
the :math:`(-1)^m` factor, see for example :cite:`Williams1999`, eq. (6.20).

The complex conjugate of :math:`Y_n^m` is given by negating the degree
:math:`m` as

.. math::
    :label: spherical-harmonics-complex-conjugate

    Y_n^m(\theta,\phi)^* = Y_n^{-m}(\theta,\phi).

For a spherical secondary source distribution with a radius of :math:`R_0` the
sound field can be calculated by a convolution along the surface. The driving
function is then given by a simple division after :cite:`Ahrens2012`, eq. (3.21)
[#F2]_ as

.. math::
    :label: freq-drivingfunction-spherical

    \begin{gathered}
        D_\text{spherical}(\theta_0,\phi_0,\w) = \\
        \frac{1}{R_0^{\,2}}
        \sum_{n=0}^\infty \sum_{m=-n}^n \sqrt{\frac{2n+1}{4\pi}}
        \frac{\breve{S}_n^m(\theta_\text{s},\phi_\text{s},r_\text{s},\w)}
        {\breve{G}_n^0(\frac{\pi}{2},0,\w)} Y_n^m(\theta_0,\phi_0),
    \end{gathered}

where :math:`\breve{S}_n^m` denote the spherical expansion coefficients of the
source model, :math:`\theta_\text{s}`, :math:`\phi_\text{s}`, and
:math:`r_\text{s}` its directional dependency, and :math:`\breve{G}_n^0` the
spherical expansion coefficients of a secondary monopole source located at
the north pole of the sphere :math:`\x_0 = (\frac{\pi}{2},0,R_0)`. For a point
source this is given after :cite:`Schultz2014`, eq. (25) as

.. math::
    :label: freq-greens-function-spherical

    \breve{G}_n^0(\tfrac{\pi}{2},0,\w) =
        -\i\wc \sqrt{\frac{2n+1}{4\pi}}
        \hankel{2}{n}{\wc R_0},

where :math:`\hankel{2}{n}{}` describes the spherical Hankel function of
:math:`n`-th order and second kind.


.. _sec-circular-geometries:

Circular Geometries
~~~~~~~~~~~~~~~~~~~

The following functions build a basis in :math:`\mathbb{R}^2` for a circular
secondary source distribution, compare :cite:`Williams1999`

.. math::
    :label: circular-harmonics

    \Phi_m(\phi) = \e{\i m\phi}.

The complex conjugate of :math:`\Phi_m` is given by negating the degree
:math:`m` as

.. math::
    :label: circular-harmonics-complex-conjugate

    \Phi_m(\phi)^* = \Phi_{-m}(\phi).

For a circular secondary source distribution with a radius of :math:`R_0` the
driving function can be calculated by a convolution along the surface of the
circle as explicitly shown by :cite:`Ahrens2009a` and is then given as

.. math::
    :label: freq-drivingfunction-circular

    D_\text{circular}(\phi_0,\w) =
        \frac{1}{2\pi R_0} \sum_{m=-\infty}^\infty
        \frac{\breve{S}_m(\phi_\text{s},r_\text{s},\w)}
        {\breve{G}_m(0,\w)} \, \Phi_m(\phi_0),

where :math:`\breve{S}_m` denotes the circular expansion coefficients for the
source model, :math:`\phi_\text{s}`, and :math:`r_\text{s}` its directional
dependency, and :math:`\breve{G}_m` the circular expansion coefficients for a
secondary monopole source. For a line source located at :math:`\x_0 = (0,R_0)`
this is given as

.. math::
    :label: freq-greens-function-circular

    \breve{G}_m(0,\w) = -\frac{\i}{4}
        \Hankel{2}{m}{\wc R_0},

where :math:`\Hankel{2}{m}{}` describes the Hankel function of :math:`m`-th
order and second kind.


.. _sec-planar-goemetries:

Planar Geometries
~~~~~~~~~~~~~~~~~

The basis functions for a planar secondary source distribution located
on the :math:`xz`-plane in :math:`\mathbb{R}^3` are given as

.. math::
    :label: planar-harmonics

    \Lambda(k_x,k_z,x,z) = \e{-\i(k_x x + k_z z)},

where :math:`k_x`, :math:`k_z` are entries in the wave vector :math:`\k` with
:math:`k^2 = (\wc )^2`. The complex conjugate is given by negating
:math:`k_x` and :math:`k_z` as

.. math::
    :label: planar-harmonics-complex-conjugate

    \Lambda(k_x,k_z,x,z)^* = \Lambda(-k_x,-k_z,x,z).

For an infinitely long secondary source distribution located on the
:math:`xz`-plane the driving function can be calculated by a two-dimensional
convolution along the plane after :cite:`Ahrens2012`, eq. (3.65) as

.. math::
    :label: freq-drivingfunction-planar

    D_\text{planar}(x_0,y_0,\w) = \frac{1}{4{\pi}^2} \iint_{-\infty}^\infty
       \frac{\breve{S}(k_x,y_\text{s},k_z,\w)}{\breve{G}(k_x,0,k_z,\w)}
       \Lambda(k_x,x_0,k_z,z_0) \d k_x \d k_z,

where :math:`\breve{S}` denotes the planar expansion coefficients for the source
model, :math:`y_\text{s}` its positional dependency, and :math:`\breve{G}` the
planar expansion coefficients of a secondary point source after
:cite:`Schultz2014`, eq. (49) with

.. math::
    :label: freq-greens-function-planar

    \breve{G}(k_x,0,k_z,\w) = -\frac{\i}{2}
        \frac{1}{\sqrt{(\wc )^2-k_x^2-k_z^2}},

for :math:`(\wc )^2 > (k_x^2+k_z^2)`.

For the planar and the following linear geometries the Fredholm equation is
solved for a non compact space :math:`V`, which leads to an infinite and
non-denumerable number of basis functions as opposed to the denumerable case for
compact spaces :cite:`Schultz2014`.


.. _sec-linear_geometries:

Linear Geometries
~~~~~~~~~~~~~~~~~

The basis functions for a linear secondary source distribution located on the
:math:`x`-axis are given as

.. math::
    :label: linear-harmonics

    \chi(k_x,x) = \e{-\i k_x x}.

The complex conjugate is given by negating :math:`k_x` as

.. math::
    :label: linear-harmonics-complex-conjugate

    \chi(k_x,x)^* = \chi(-k_x,x).

For an infinitely long secondary source distribution located on the
:math:`x`-axis the driving function for :math:`{\mathbb{R}}^2` can be calculated
by a convolution along this axis after :cite:`Ahrens2012`, eq. (3.73) as

.. math::
    :label: freq-drivingfunction-linear

    D_\text{linear}(x_0,\w) = \frac{1}{2\pi} \int_{-\infty}^\infty
        \frac{\breve{S}(k_x,y_\text{s},\w)}{\breve{G}(k_x,0,\w)}
        \chi(k_x,x_0) \d k_x,

where :math:`\breve{S}` denotes the linear expansion coefficients for the source
model, :math:`y_\text{s}`, :math:`z_\text{s}` its positional dependency, and
:math:`\breve{G}` the linear expansion coefficients of a secondary line source
with

.. math::
    :label: freq-greens-function-linear

    \breve{G}(k_x,0,\w) = -\frac{\i}{2}
        \frac{1}{\sqrt{(\wc )^2-k_x^2}},

for :math:`0<|k_x|<|\wc |\,`.


.. [#F1]
    Note that :math:`\sin\theta` is used here instead of :math:`\cos\theta` due
    to the use of another coordinate system, compare Figure 2.1 from
    :cite:`Gumerov2004` and :numref:`fig-coordinate-system`.

.. [#F2]
    Note the :math:`\frac{1}{2\pi}` term is wrong in :cite:`Ahrens2012`, eq. (3.21)
    and eq. (5.7) and omitted here, compare the `errata
    <http://www.soundfieldsynthesis.org/errata/>`_ and :cite:`Schultz2014`,
    eq. (24).


.. vim: filetype=rst spell:
