.. _sec-driving-functions-local-sfs:

Driving functions for |LSFS|
----------------------------

The reproduction accuracy of |WFS| is limited due to practical aspects.  For the
audible frequency range the desired sound field can not be synthesized
aliasing-free over an extended listening area, which is surrounded by a discrete
ensemble of individually driven loudspeakers.  However, it is suitable for
certain applications to increase reproduction accuracy inside a smaller (local)
listening region while stronger artifacts outside are permitted. The implemented
Local Wave Field Synthesis method utilizes focused sources as a distribution of
virtual loudspeakers which are placed more densely around the local listening
area. These virtual loudspeakers can be driven by conventional SFS techniques,
like e.g. |WFS| or |NFC-HOA|. The results are similar to band-limited |NFC-HOA|, with
the difference that the form and position of the enhanced area can freely be
chosen within the listening area.

The set of focused sources is treated as a virtual loudspeaker distribution and
their positions :math:`{\x_\text{fs}}` are subsumed under
:math:`\mathcal{X}_{\mathrm{fs}}`. Therefore, each focused source is driven
individually by :math:`D_\text{l}({\x_\text{fs}}, \w)`, which in principle
can be any driving function for real loudspeakers mentioned in previous
sections. At the moment however, only |WFS| and |NFC-HOA| driving functions are
supported. The resulting driving function for a loudspeaker located at
:math:`\x_0` reads

.. math::
    :label: D.localwfs

    D(\x_0,\w) = \sum_{{\x_\text{fs}}\in \mathcal{X}_{\mathrm{fs}}}
        D_{\mathrm l}({\x_\text{fs}}, \w)
        D_{\mathrm{fs}}(\x_0,{\x_\text{fs}},\w),

which is superposition of the driving function
:math:`D_{\mathrm{fs}}(\x_0,{\x_\text{fs}},\w)` reproducing a single focused
source at :math:`{\x_\text{fs}}` weighted by :math:`D_\text{l}({\x_\text{fs}},
\w)`.  Former is derived by replacing :math:`\xs` with
:math:`{\x_\text{fs}}` in the |WFS| driving functions and for focused sources.
This yields

.. math::
    :label: D.localwfs.fs

    D_{\mathrm{fs}}(\x_0,{\x_\text{fs}},\w) =
        \frac{1}{2\pi} A(\w) w(\x_0) \i\wc 
        \frac{\scalarprod{\x_0-\x_\text{fs}}{\n_{\x_0}}}
        {|\x_0-{\x_\text{fs}}|^{\frac{3}{2}}}
        \e{\i\wc |\x_0-{\x_\text{fs}}|}

and

.. math::
    :label: D.localwfs.fs.2.5D

    D_{\mathrm{fs,2.5D}}(\x_0,{\x_\text{fs}},\w) = 
       \frac{g_0}{2\pi} A(\w) w(\x_0) \sqrt{\i\wc }
       \frac{\scalarprod{\x_0-\xs}{\n_{\x_0}}}{|\x_0-\xs|^{\frac{3}{2}}}
       \e{\i\wc |\x_0-\xs|}

for the 2.5D case. For the temporal domain, inverse Fourier transform yields the
driving signals

.. math::
    :label: d.localwfs

    d(\x_0,t) = \sum_{{\x_\text{fs}}\in \mathcal{X}_{\mathrm{fs}}} 
        d_{\mathrm l}({\x_\text{fs}}, t) * 
        d_{\mathrm{fs}}(\x_0,{\x_\text{fs}}, t),

while :math:`d_{\mathrm{fs}}(\x_0,{\x_\text{fs}}, t)` is derived analogously to
from or . At the moment :math:`d_{\mathrm l}({\x_\text{fs}}, t)` does only
support driving functions from |WFS|.


.. vim: filetype=rst spell:
