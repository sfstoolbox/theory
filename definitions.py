# Definitions of all acronyms used in the document
acronyms = """
.. |BRIR|            replace:: :abbr:`BRIR (Binaural Room Impulse Response)`
.. |DOI|             replace:: :abbr:`DOI (Digital Object Identifier)`
.. |FFT|             replace:: :abbr:`FFT (Fast Fourier Transform)`
.. |HOA|             replace:: :abbr:`HOA (Higher Order Ambisonics)`
.. |HRIR|            replace:: :abbr:`HRIR (Head-Related Impulse Response)`
.. |HRTF|            replace:: :abbr:`HRTF (Head-Related Transfer Function)`
.. |KEMAR|           replace:: :abbr:`KEMAR (Knowles Electronics Manikin for Acoustic Research)`
.. |LSFS|            replace:: :abbr:`LSFS (Local Sound Field Synthesis)`
.. |NFC-HOA|         replace:: :abbr:`NFC-HOA (Near-Field Compensated Higher Order Ambisonics)`
.. |SDM|             replace:: :abbr:`SDM (Spectral Division Method)`
.. |SOFA|            replace:: :abbr:`SOFA (Spatially Oriented Format for Acoustics)`
.. |SSR|             replace:: :abbr:`SSR (SoundScape Renderer)`
.. |WFS|             replace:: :abbr:`WFS (Wave Field Synthesis)`
"""

# Definitions of LaTeX macros used in the document
latex_macros = r"""
    \def \i                {\mathrm{i}}
    \def \e              #1{\mathrm{e}^{#1}}
    \def \w                {\omega}
    \def \wc               {\frac{\w}{c}}
    \def \vec            #1{\mathbf{#1}}
    \def \x                {\vec{x}}
    \def \xs               {\x_\text{s}}
    \def \xref             {\x_\text{ref}}
    \def \k                {\vec{k}}
    \def \n                {\vec{n}}
    \def \d                {\operatorname{d}\!}
    \def \dirac          #1{\operatorname{\delta}\left(#1\right)}
    \def \scalarprod   #1#2{\left\langle#1,#2\right\rangle}
    \def \Hankel     #1#2#3{\mathop{{}H_{#2}^{(#1)}}\!\left(#3\right)}
    \def \hankel     #1#2#3{\mathop{{}h_{#2}^{(#1)}}\!\left(#3\right)}
"""

# vim: textwidth=300:
