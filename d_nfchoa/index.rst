.. _sec-driving-functions-nfchoa-sdm:

Driving functions for NFC-HOA and SDM
-------------------------------------

In the following, driving functions for |NFC-HOA| and |SDM| are derived
for spherical, circular, and linear secondary source distributions. Among the
possible combinations of methods and secondary sources not all are meaningful.
Hence, only the relevant ones will be presented. The same holds for the
introduced source models of plane waves, point sources, line sources and focused
sources. Ahrens and Spors :cite:`Ahrens2010` in addition have considered |SDM|
driving functions for planar secondary source distributions.

For |NFC-HOA|, temporal-domain implementations for the
2.5D cases are available for a plane wave and a point source as source models. The
derivation of the implementation is not explicitly shown here, but is described
in :cite:`Spors2011`.


.. _sec-driving-functions-nfchoa-sdm-plane-wave:

Plane Wave
~~~~~~~~~~

.. plot::
    :context: close-figs
    :nofigs:

    nk = 0, -1, 0  # direction of plane wave
    omega = 2 * np.pi * 1000  # frequency
    R0 = 1.5  # radius of secondary sources
    x0, n0, a0 = sfs.array.circular(200, R0)
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    d = sfs.mono.drivingfunction.nfchoa_25d_plane(omega, x0, R0, nk)
    p = sfs.mono.synthesized.generic(omega, x0, n0, d * a0 , grid,
        source=sfs.mono.source.point)
    normalization = 0.05
    sfs.plot.soundfield(normalization * p, grid)
    sfs.plot.secondarysource_2d(x0, n0, grid)

.. plot::
    :context:
    :include-source: false
    :nofigs:

    save_fig('nfchoa-25d-plane-wave')

.. _fig-nfchoa-25d-plane-wave:

.. figure:: nfchoa-25d-plane-wave.*
    :align: center

    Sound pressure for a monochromatic plane wave synthesized with 2.5D
    |NFC-HOA| :eq:`d-nfchoa-plane-wave-25d-frequency-domain`.  Parameters:
    :math:`\n_k = (0, -1, 0)`, :math:`\xref = (0, 0, 0)`, :math:`f = 1` kHz.

For a spherical secondary source distribution with radius :math:`R_0` the
spherical expansion coefficients of a plane
wave :eq:`plane-wave-spherical-coefficients` and of the Green’s function for a
point source :eq:`g-spherical-frequency-domain` are inserted
into :eq:`d-spherical-frequency-domain` and yield :cite:`Schultz2014`, eq. (A3)

.. math::
    :label: d-nfchoa-plane-wave-3d-frequency-domain

    D_\text{spherical}(\theta_0,\phi_0,\w) = -A(\w)
        \frac{4\pi}{R_0^{\,2}} \sum_{n=0}^\infty \sum_{m=-n}^n
        \frac{\i^{-n} Y_n^{-m}(\theta_k,\phi_k)}
        {\i\wc \hankel{2}{n}{\wc R_0}}
        Y_n^m(\theta_0,\phi_0).

For a circular secondary source distribution with radius :math:`R_0` the
circular expansion coefficients of a plane
wave :eq:`plane-wave-circular-coefficients` and of the Green’s function for a
line source :eq:`g-circular-frequency-domain` are inserted
into :eq:`d-circular-frequency-domain` and yield :cite:`Ahrens2009a`, eq. (16)

.. math::
    :label: d-nfchoa-plane-wave-2d-frequency-domain

    D_\text{circular}(\phi_0,\w) = -A(\w) \frac{2\i}{\pi R_0}
        \sum_{m=-\infty}^\infty \frac{\i^{-m}\Phi_{-m}(\phi_k)}
        {\Hankel{2}{m}{\wc R_0}} \Phi_m(\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and point
source as Green’s function the 2.5D driving function is given by inserting the
spherical expansion coefficients for a plane
wave :eq:`plane-wave-spherical-coefficients` and a point
source :eq:`point-source-spherical-coefficients`
into :eq:`d-circular-25d-frequency-domain` as

.. math::
    :label: d-nfchoa-plane-wave-25d-frequency-domain

    D_{\text{circular},\,\text{2.5D}}(\phi_0,\w) = -A(\w)
        \frac{2}{R_0} \sum_{m=-\infty}^\infty
        \frac{\i^{-|m|} \Phi_{-m}(\phi_k)}
        {\i\wc \hankel{2}{|m|}{\wc R_0}} \Phi_m(\phi_0).

For an infinite linear secondary source distribution located on the
:math:`x`-axis the 2.5D driving function is given by inserting the linear
expansion coefficients for a point source as Green’s
function :eq:`point-source-linear-coefficients` and a plane
wave :eq:`plane-wave-linear-coefficients`
into :eq:`d-linear-25d-frequency-domain` and exploiting the fact that
:math:`(\wc )^2 - k_{x_\text{s}}` is constant.  Assuming :math:`0 \le
|k_{x_\text{s}}| \le |\wc |` this results in :cite:`Ahrens2010`, eq. (17)

.. math::
    :label: d-sdm-plane-wave-25d-frequency-domain

    D_{\text{linear},\,\text{2.5D}}(x_0,\w) = A(\w)
        \frac{4\i\chi(k_y,y_\text{ref})}
        {\Hankel{2}{0}{k_y y_\text{ref}}} \chi(k_x,x_0).

Transferred to the temporal domain this results in :cite:`Ahrens2010`, eq. (18)

.. math::
    :label: d-sdm-plane-wave-25d-time-domain

    d_{\text{linear},\,\text{2.5D}}(x_0,t) = h(t) *
        a\left(t-\frac{x_0}{c}\sin\phi_k-\frac{y_\text{ref}}{c}\sin\phi_k\right),

where :math:`\phi_k` denotes the azimuth direction of the plane wave and

.. math::
    :label: h-sdm

    h(t) = {\mathcal{F}^{-1}\left\{\frac{4\i}
        {\Hankel{2}{0}{k_y y_\text{ref}}}\right\}}.

The advantage of this result is that it can be implemented by a simple weighting
and delaying of the signal, plus one convolution with :math:`h(t)`. The same
holds for the driving functions of |WFS| as presented in the next section.


.. _sec-driving-functions-nfchoa-sdm-point-source:

Point Source
~~~~~~~~~~~~

.. plot::
    :context: close-figs
    :nofigs:

    xs = 0, 2.5, 0  # position of source
    omega = 2 * np.pi * 1000  # frequency
    R0 = 1.5  # radius of secondary sources
    x0, n0, a0 = sfs.array.circular(200, R0)
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    d = sfs.mono.drivingfunction.nfchoa_25d_point(omega, x0, R0, xs)
    p = sfs.mono.synthesized.generic(omega, x0, n0, d * a0 , grid,
        source=sfs.mono.source.point)
    normalization = 20
    sfs.plot.soundfield(normalization * p, grid)
    sfs.plot.secondarysource_2d(x0, n0, grid)

.. plot::
    :context:
    :include-source: false
    :nofigs:

    save_fig('nfchoa-25d-point-source')

.. _fig-nfchoa-25d-point-source:

.. figure:: nfchoa-25d-point-source.*
    :align: center

    Sound pressure for a monochromatic point source synthesized with 2.5D
    |NFC-HOA| :eq:`d-nfchoa-point-source-25d-frequency-domain`.  Parameters:
    :math:`\xs = (0, 2.5, 0)` m, :math:`\xref = (0, 0, 0)`, :math:`f = 1` kHz.

For a spherical secondary source distribution with radius :math:`R_0` the
spherical coefficients of a point
source :eq:`point-source-spherical-coefficients` and of the Green’s
function :eq:`g-spherical-frequency-domain` are inserted
into :eq:`d-spherical-frequency-domain` and yield :cite:`Ahrens2012`, eq. (5.7)
[#F1]_

.. math::
    :label: d-nfchoa-point-source-3d-frequency-domain

    D_\text{spherical}(\theta_0,\phi_0,\w) =
        A(\w) \frac{1}{R_0^{\,2}} \sum_{n=0}^\infty \sum_{m=-n}^n
        \frac{\hankel{2}{n}{\wc r_\text{s}}
        Y_n^{-m}(\theta_\text{s},\phi_\text{s})}
        {\hankel{2}{n}{\wc R_0}} Y_n^m (\theta_0,\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and point
source as secondary sources the 2.5D driving function is given by inserting the
spherical coefficients :eq:`point-source-spherical-coefficients`
and :eq:`g-spherical-frequency-domain`
into :eq:`d-circular-25d-frequency-domain`. This results in :cite:`Ahrens2012`,
eq. (5.8)

.. math::
    :label: d-nfchoa-point-source-25d-frequency-domain

    D_{\text{circular},\,\text{2.5D}}(\phi_0,\w) =
        A(\w) \frac{1}{2\pi R_0} \sum_{m=-\infty}^{\infty}
        \frac{\hankel{2}{|m|}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s})}
        {\hankel{2}{|m|}{\wc R_0}} \Phi_m(\phi_0).

For an infinite linear secondary source distribution located on the
:math:`x`-axis and point sources as secondary sources the 2.5D driving function
for a point source is given by inserting the corresponding linear expansion
coefficients :eq:`point-source-linear-coefficients`
and :eq:`g-linear-frequency-domain` into :eq:`d-linear-25d-frequency-domain`.
Assuming :math:`0 \le |k_x| < |\wc |` this results in :cite:`Ahrens2012`, eq.
(4.53)

.. math::
    :label: d-sdm-point-source-25d-frequency-domain

    \begin{aligned}
        D_{\text{linear},\,\text{2.5D}}(x_0,\w) =&
            A(\w) \int_{-\infty}^\infty
            \frac{\Hankel{2}{0}{\sqrt{(\wc )^2-k_x^2} \;
            (y_\text{ref}-y_\text{s})} \chi(-k_x,x_\text{s})}
            {\Hankel{2}{0}{\sqrt{(\wc )^2-k_x^2} \; y_\text{ref}}} \\
            &\cdot \chi(k_x,x_0) \d k_x.
    \end{aligned}


.. _sec-driving-functions-nfchoa-sdm-line-source:

Line Source
~~~~~~~~~~~

For a spherical secondary source distribution with radius :math:`R_0` the spherical
coefficients of a line source :eq:`line-source-spherical-coefficients` and of
the Green's function :eq:`g-spherical-frequency-domain` are inserted into
:eq:`d-spherical-frequency-domain` and yield :cite:`Hahn2015`, eq. (20)

.. math::
    :label: d-nfchoa-line-source-3d-frequency-domain

    D_{\text{spherical}}(\theta_0,\phi_0,\w) = A(\w) \frac{1}{2 R_0^2}
        \sum_{n=0}^{\infty} \sum_{m=-n}^{n}
        \frac{\i^{m-n} \Hankel{2}{m}{\wc r_\text{s}}
        Y_n^{-m}(0,\phi_\text{s})}
        {\wc \hankel{2}{n}{\wc R_0}}
        Y_n^m(\theta_0,\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and line
sources as secondary sources the driving function is given by inserting the
circular coefficients :eq:`line-source-circular-coefficients`
and :eq:`g-circular-frequency-domain` into :eq:`d-circular-frequency-domain` as

.. math::
    :label: d-nfchoa-line-source-2d-frequency-domain

    D_{\text{circular}}(\phi_0,\w) = A(\w) \frac{1}{2\pi R_0}
        \sum_{m=-\infty}^{\infty}
        \frac{\Hankel{2}{m}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s})} {\Hankel{2}{m}{\wc R_0}}
        \Phi_m(\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and point
sources as secondary sources the 2.5D driving function is given by inserting the
spherical coefficients :eq:`line-source-spherical-coefficients`
and :eq:`g-spherical-frequency-domain` into
:eq:`d-circular-25d-frequency-domain` after :cite:`Hahn2015`, eq. (23) as

.. math::
    :label: d-nfchoa-line-source-25d-frequency-domain

    D_{\text{circular},\,\text{2.5D}}(\phi_0,\w) =
        A(\w) \frac{1}{2 R_0} \sum_{m=-\infty}^{\infty}
        \frac{\i^{m-|m|} \Hankel{2}{m}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s})}
        {\wc \hankel{2}{|m|}{\wc R_0}}
        \Phi_m(\phi_0).

For an infinite linear secondary source distribution located on the
:math:`x`-axis and line sources as secondary sources the driving function is
given by inserting the linear coefficients :eq:`line-source-linear-coefficients`
and :eq:`g-linear-frequency-domain` into :eq:`d-linear-frequency-domain` as

.. math::
    :label: d-sdm-line-source-2d-frequency-domain

    D_\text{linear}(x_0,\w) = A(\w) \frac{1}{2\pi}
        \int_{-\infty}^\infty \chi(k_y,y_s) \chi(k_x,x_0) \d k_x.


.. _sec-driving-functions-nfchoa-sdm-focused-source:

Focused Source
~~~~~~~~~~~~~~

Focused sources mimic point or line sources that are located inside the audience
area. For the single-layer potential the assumption is that the audience area is
free from sources and sinks. However, a focused source is neither of them. It
represents a sound field that converges towards a focal point and diverges
afterwards. This can be achieved by reversing the driving function of a point or
line source in time which is known as time reversal focusing :cite:`Yon2003`.

Nonetheless, the single-layer potential should not be solved for focused sources
without any approximation. In the near field of a source, evanescent waves
appear for spatial frequencies :math:`k_x > |\wc |` :cite:`Williams1999`, eq.
(24). They decay exponentially with the distance from the source.  An exact
solution for a focused source is supposed to include these evanescent waves
around the focal point. That is only possible by applying very large amplitudes
to the secondary sources, compare Fig. 2a in :cite:`Spors2010`. Since the
evanescent waves decay rapidly and are hence not influencing the perception,
they can easily be omitted. For corresponding driving functions for focused
sources without the evanescent part of the sound field see :cite:`Spors2010` for
|SDM| and :cite:`Ahrens2009b` for |NFC-HOA|.

In the SFS Toolbox only focused sources in |WFS| are considered at the moment.


.. [#F1]
    Note the :math:`\frac{1}{2\pi}` term is wrong in :cite:`Ahrens2012`, eq.
    (3.21) and eq. (5.7) and omitted here, compare the `errata
    <http://www.soundfieldsynthesis.org/errata/>`_ and :cite:`Schultz2014`, eq.
    (24).

.. vim: filetype=rst spell:
