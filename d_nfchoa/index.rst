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
    array = sfs.array.circular(200, R0)
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    d, selection, secondary_source = \
        sfs.fd.nfchoa.plane_25d(omega, array.x, R0, nk)
    twin = sfs.tapering.none(selection)
    p = sfs.fd.synthesize(d, twin, array, secondary_source, grid=grid)
    sfs.plot.soundfield(p, grid)
    sfs.plot.secondarysource_2d(array.x, array.n, grid)

.. plot::
    :context:
    :include-source: false
    :nofigs:

    save_fig('nfchoa-25d-plane-wave')

.. _fig-nfchoa-25d-plane-wave:

.. figure:: nfchoa-25d-plane-wave.*
    :align: center

    Sound pressure for a monochromatic plane wave synthesized with 2.5D
    |NFC-HOA| :eq:`fd-nfchoa-plane-25d`.  Parameters:
    :math:`\n_k = (0, -1, 0)`, :math:`\xref = (0, 0, 0)`, :math:`f = 1` kHz.

For a spherical secondary source distribution with radius :math:`R_0` the
spherical expansion coefficients of a plane
wave :eq:`plane-spherical-coefficients` and of the Green’s function for a
point source :eq:`fd-greens-function-spherical` are inserted
into :eq:`fd-drivingfunction-spherical` and yield :cite:`Schultz2014`,
eq. (A3)

.. math::
    :label: fd-nfchoa-plane-3d

    D_\text{spherical}(\theta_0,\phi_0,\w) = -A(\w)
        \frac{4\pi}{R_0^{\,2}} \sum_{n=0}^\infty \sum_{m=-n}^n
        \frac{\i^{-n} Y_n^{-m}(\theta_k,\phi_k)}
        {\i\wc \hankel{2}{n}{\wc R_0}}
        Y_n^m(\theta_0,\phi_0).

For a circular secondary source distribution with radius :math:`R_0` the
circular expansion coefficients of a plane
wave :eq:`plane-circular-coefficients` and of the Green’s function for a
line source :eq:`fd-greens-function-circular` are inserted
into :eq:`fd-drivingfunction-circular` and yield :cite:`Ahrens2009a`, eq. (16)

.. math::
    :label: fd-nfchoa-plane-2d

    D_\text{circular}(\phi_0,\w) = -A(\w) \frac{2\i}{\pi R_0}
        \sum_{m=-\infty}^\infty \frac{\i^{-m}\Phi_{-m}(\phi_k)}
        {\Hankel{2}{m}{\wc R_0}} \Phi_m(\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and point
source as Green’s function the 2.5D driving function is given by inserting the
spherical expansion coefficients for a plane
wave :eq:`plane-spherical-coefficients` and a point
source :eq:`point-spherical-coefficients`
into :eq:`fd-drivingfunction-circular-25d` as

.. math::
    :label: fd-nfchoa-plane-25d

    D_{\text{circular},\,\text{2.5D}}(\phi_0,\w) = -A(\w)
        \frac{2}{R_0} \sum_{m=-\infty}^\infty
        \frac{\i^{-|m|} \Phi_{-m}(\phi_k)}
        {\i\wc \hankel{2}{|m|}{\wc R_0}} \Phi_m(\phi_0).

For an infinite linear secondary source distribution located on the
:math:`x`-axis the 2.5D driving function is given by inserting the linear
expansion coefficients for a point source as Green’s
function :eq:`point-linear-coefficients` and a plane
wave :eq:`plane-linear-coefficients`
into :eq:`fd-drivingfunction-linear-25d` and exploiting the fact that
:math:`(\wc )^2 - k_{x_\text{s}}` is constant.  Assuming :math:`0 \le
|k_{x_\text{s}}| \le |\wc |` this results in :cite:`Ahrens2010`, eq. (17)

.. math::
    :label: fd-sdm-plane-25d

    D_{\text{linear},\,\text{2.5D}}(x_0,\w) = A(\w)
        \frac{4\i\chi(k_y,y_\text{ref})}
        {\Hankel{2}{0}{k_y y_\text{ref}}} \chi(k_x,x_0).

Transferred to the temporal domain this results in :cite:`Ahrens2010`, eq. (18)

.. math::
    :label: td-sdm-plane-25d

    d_{\text{linear},\,\text{2.5D}}(x_0,t) = h(t) *
        a\left(t-\frac{x_0}{c}\sin\phi_k-\frac{y_\text{ref}}{c}\sin\phi_k\right),

where :math:`\phi_k` denotes the azimuth direction of the plane wave and

.. math::
    :label: td-sdm-prefilter

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
    array = sfs.array.circular(200, R0)
    grid = sfs.util.xyz_grid([-1.75, 1.75], [-1.75, 1.75], 0, spacing=0.02)
    d, selection, secondary_source = \
        sfs.fd.nfchoa.point_25d(omega, array.x, R0, xs)
    twin = sfs.tapering.none(selection)
    p = sfs.fd.synthesize(d, twin, array, secondary_source, grid=grid)
    normalization = 20
    sfs.plot.soundfield(normalization * p, grid)
    sfs.plot.secondarysource_2d(array.x, array.n, grid)

.. plot::
    :context:
    :include-source: false
    :nofigs:

    save_fig('nfchoa-25d-point-source')

.. _fig-nfchoa-25d-point-source:

.. figure:: nfchoa-25d-point-source.*
    :align: center

    Sound pressure for a monochromatic point source synthesized with 2.5D
    |NFC-HOA| :eq:`fd-nfchoa-point-25d`.  Parameters:
    :math:`\xs = (0, 2.5, 0)` m, :math:`\xref = (0, 0, 0)`, :math:`f = 1` kHz.

For a spherical secondary source distribution with radius :math:`R_0` the
spherical coefficients of a point
source :eq:`point-spherical-coefficients` and of the Green’s
function :eq:`fd-greens-function-spherical` are inserted
into :eq:`fd-drivingfunction-spherical` and yield :cite:`Ahrens2012`,
eq. (5.7) [#F1]_

.. math::
    :label: fd-nfchoa-point-3d

    D_\text{spherical}(\theta_0,\phi_0,\w) =
        A(\w) \frac{1}{R_0^{\,2}} \sum_{n=0}^\infty \sum_{m=-n}^n
        \frac{\hankel{2}{n}{\wc r_\text{s}}
        Y_n^{-m}(\theta_\text{s},\phi_\text{s})}
        {\hankel{2}{n}{\wc R_0}} Y_n^m (\theta_0,\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and point
source as secondary sources the 2.5D driving function is given by inserting the
spherical coefficients :eq:`point-spherical-coefficients`
and :eq:`fd-greens-function-spherical` into
:eq:`fd-drivingfunction-circular-25d`. This results in :cite:`Ahrens2012`,
eq. (5.8)

.. math::
    :label: fd-nfchoa-point-25d

    D_{\text{circular},\,\text{2.5D}}(\phi_0,\w) =
        A(\w) \frac{1}{2\pi R_0} \sum_{m=-\infty}^{\infty}
        \frac{\hankel{2}{|m|}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s})}
        {\hankel{2}{|m|}{\wc R_0}} \Phi_m(\phi_0).

For an infinite linear secondary source distribution located on the
:math:`x`-axis and point sources as secondary sources the 2.5D driving function
for a point source is given by inserting the corresponding linear expansion
coefficients :eq:`point-linear-coefficients`
and :eq:`fd-greens-function-linear` into
:eq:`fd-drivingfunction-linear-25d`. Assuming :math:`0 \le |k_x| < |\wc |`
this results in :cite:`Ahrens2012`, eq. (4.53)

.. math::
    :label: fd-sdm-point-25d

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

For a spherical secondary source distribution with radius :math:`R_0` the
spherical coefficients of a line source :eq:`line-spherical-coefficients` and of
the Green's function :eq:`fd-greens-function-spherical` are inserted into
:eq:`fd-drivingfunction-spherical` and yield :cite:`Hahn2015`, eq. (20)

.. math::
    :label: fd-nfchoa-line-3d

    D_{\text{spherical}}(\theta_0,\phi_0,\w) = A(\w) \frac{1}{2 R_0^2}
        \sum_{n=0}^{\infty} \sum_{m=-n}^{n}
        \frac{\i^{m-n} \Hankel{2}{m}{\wc r_\text{s}}
        Y_n^{-m}(0,\phi_\text{s})}
        {\wc \hankel{2}{n}{\wc R_0}}
        Y_n^m(\theta_0,\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and line
sources as secondary sources the driving function is given by inserting the
circular coefficients :eq:`line-circular-coefficients`
and :eq:`fd-greens-function-circular` into
:eq:`fd-drivingfunction-circular` as

.. math::
    :label: fd-nfchoa-line-2d

    D_{\text{circular}}(\phi_0,\w) = A(\w) \frac{1}{2\pi R_0}
        \sum_{m=-\infty}^{\infty}
        \frac{\Hankel{2}{m}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s})} {\Hankel{2}{m}{\wc R_0}}
        \Phi_m(\phi_0).

For a circular secondary source distribution with radius :math:`R_0` and point
sources as secondary sources the 2.5D driving function is given by inserting the
spherical coefficients :eq:`line-spherical-coefficients`
and :eq:`fd-greens-function-spherical` into
:eq:`fd-drivingfunction-circular-25d` after :cite:`Hahn2015`, eq. (23) as

.. math::
    :label: fd-nfchoa-line-25d

    D_{\text{circular},\,\text{2.5D}}(\phi_0,\w) =
        A(\w) \frac{1}{2 R_0} \sum_{m=-\infty}^{\infty}
        \frac{\i^{m-|m|} \Hankel{2}{m}{\wc r_\text{s}}
        \Phi_{-m}(\phi_\text{s})}
        {\wc \hankel{2}{|m|}{\wc R_0}}
        \Phi_m(\phi_0).

For an infinite linear secondary source distribution located on the
:math:`x`-axis and line sources as secondary sources the driving function is
given by inserting the linear coefficients :eq:`line-linear-coefficients`
and :eq:`fd-greens-function-linear` into :eq:`fd-drivingfunction-linear` as

.. math::
    :label: fd-sdm-line-2d

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
