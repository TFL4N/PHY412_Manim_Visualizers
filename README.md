# PHY412 Manim Visualizers

This project has been superseded by an interactive version [PHY412_PyQtGraph_Visualizers](https://github.com/TFL4N/PHY412_PyQtGraph_Visualizers)
___

While taking Electrodynamics taught by Professor Richard Kirian at Arizona State University, I shared my recently created [Lissajous Figure Generator](https://github.com/TFL4N/Lissajous-HTML5) with the class.  Lissajous figures are created from two orthogonal sinusoids.

Always trying to make class material more intuitive and understandable, Professor Kirian ask if I could help create visualizers for various concepts, in particular, the polarization of light that results from two orthogonal electromagnetic waves.  This repo contains the results of this collaboration 

This gif is an example of right circular polarization:
![Gif of Polarization](/examples/images/readme/circular_right_full_800x450.gif)

## Installation

installs manim deps in new env 'manim'

!! Note: if using Latex, that needs to be installed separately.  See https://docs.manim.community/en/stable/installation/macos.html#optional-dependencies

```
conda env create --file environment.yml
conda activate manim
```


## manim General Advice
### Generating output

```
# example
manim -pql manim_demo.py

-ql/qm/qh == quality flags: low, medium, high
-p == auto open movie in default player
--disable_caching == render without using cached data from previous renders
```

### Troubleshooting
- Output video not changing/updating
  - Close Quicktime window of old video before opening (happens when new video replaces old video on disk)
  - is manim using cached data when rendering (this info should print in console)
    - use the command flag '--disable_caching'
