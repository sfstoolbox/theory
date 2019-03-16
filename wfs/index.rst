.. _sec-wfs:

High Frequency Approximation: WFS
---------------------------------

The single-layer potential :eq:`single-layer` satisfies the homogeneous
Helmholtz equation both in the interior and exterior regions :math:`V` and
:math:`V^* {\mathrel{\!\mathop:}=}{\mathbb{R}}^n \setminus (V \cup \partial V)\,`.
If :math:`D(\x_0,\w)` is continuous, the pressure :math:`P(\x,\w)` is
continuous when approaching the surface :math:`\partial V` from the inside and
outside. Due to the presence of the secondary sources at the surface
:math:`\partial V`, the gradient of :math:`P(\x,\w)` is discontinuous when
approaching the surface.  The strength of the secondary sources is then given by
the differences of the gradients approaching :math:`\partial V` from both sides
after :cite:`Fazi2013` as

.. math::
    :label: fd-drivingfunction-gradient

    D(\x_0,\w) = \partial_\n P(\x_0,\w) +
        \partial_{-\n} P(\x_0,\w),

where :math:`\partial_\n{\mathrel{\mathop:}=}\scalarprod{\nabla}{\n}` is
the directional gradient in direction :math:`\n` – see :numref:`fig-geometry`.
Due to the symmetry of the problem the solution for an infinite planar boundary
:math:`\partial V` is given as

.. math::
    :label: fd-drivingfunction-wfs

    D(\x_0,\w) = -2 \partial_\n S(\x_0,\w),

where the pressure in the outside region is the mirrored interior pressure given
by the source model :math:`S(\x,\w)` for :math:`\x\in V`. The integral equation
resulting from introducing :eq:`fd-drivingfunction-wfs`
into :eq:`single-layer` for a planar boundary :math:`\partial V` is known as
*Rayleigh’s first integral equation*. This solution is identical to the explicit
solution for planar geometries :eq:`fd-drivingfunction-planar` in
:math:`{\mathbb{R}}^3` and for linear
geometries :eq:`fd-drivingfunction-linear` in :math:`{\mathbb{R}}^2`.

A solution of :eq:`fd-drivingfunction-gradient` for arbitrary boundaries can
be found by applying the *Kirchhoff* or *physical optics approximation*
:cite:`Colton1983`, p. 53–54.  In acoustics this is also known as *determining
the visible elements* for the high frequency boundary element method
:cite:`Herrin2003`.  Here, it is assumed that a bent surface can be approximated
by a set of small planar surfaces for which :eq:`fd-drivingfunction-wfs` holds
locally.  In general, this will be the case if the wave length is much smaller
than the size of a planar surface patch and the position of the listener is far
away from the secondary sources. [#F1]_ Additionally, only one part of the
surface is active: the area that is illuminated from the incident field of the
source model.

The outlined approximation can be formulated by introducing a window function
:math:`w(\x_0)` for the selection of the active secondary sources
into :eq:`fd-drivingfunction-wfs` as

.. math::
    :label: fd-wfs

    P(\x,\w) \approx \oint_{\partial V} \!\!  G(\x|\x_0,\w) \,
        \underbrace{-2 w(\x_0) \partial_\n S(\x_0,\w)}_{D(\x_0,\w)}
        \d A(\x_0).

In the SFS Toolbox we assume convex secondary source distributions, which
allows to formulate the window function by a scalar product with the normal
vector of the secondary source distribution.  In general, also non-convex
secondary source distributions can be used with |WFS| – compare the appendix in
:cite:`Lax1947` [#F2]_.

One of the advantages of the applied approximation is that due to its local
character the solution of the driving function :eq:`fd-drivingfunction-wfs`
does not depend on the geometry of the secondary sources. This dependency
applies to the direct solutions presented in :ref:`sec-nfchoa`.

.. [#F1]
    Compare the assumptions made before (15) in :cite:`Spors2013`, which lead
    to the derivation of the same window function in a more explicit way.

.. [#F2]
    The solution mentioned by :cite:`Lax1947` assumes that the listener is
    far away from the radiator and that the radiator is a physical source not a
    notional one as the secondary sources. In this case the selection criterion
    has to be chosen more carefully, incorporating the exact position of the
    listener and the virtual source. See also the `related discussion
    <https://github.com/sfstoolbox/sfs-documentation/issues/8>`_.

.. vim: filetype=rst spell:
