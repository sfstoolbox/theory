# Definitions of all acronyms used in the document
acronyms = """
.. |BRIR|            replace:: :abbr:`BRIR (Binaural Room Impulse Response)`
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
latexmacros = """
.. rst-class:: hidden
.. math::
    \\newcommand{\\i}{\\mathrm{i}}
    \\newcommand{\\e}[1]{\\mathrm{e}^{#1}}
    \\newcommand{\\w}{\\omega}
    \\newcommand{\\wc}{\\frac{\\w}{c}}
    \\renewcommand{\\vec}[1]{\\mathbf{#1}}
    \\newcommand{\\x}{\\vec{x}}
    \\newcommand{\\xs}{\\x_\\text{s}}
    \\newcommand{\\xref}{\\x_\\text{ref}}
    \\newcommand{\\k}{\\vec{k}}
    \\newcommand{\\n}{\\vec{n}}
    \\newcommand{\\d}{\\operatorname{d\\!}{}}
    \\newcommand{\\dirac}[1]{\\operatorname{\\delta}\\left(#1\\right)}
    \\newcommand{\\scalarprod}[2]{\\left\\langle#1,#2\\right\\rangle}
    \\newcommand{\\Hankel}[3]{\\mathop{{}H_{#2}^{(#1)}}\\!\\left(#3\\right)}
    \\newcommand{\\hankel}[3]{\\mathop{{}h_{#2}^{(#1)}}\\!\\left(#3\\right)}

"""

# vim: textwidth=300:
