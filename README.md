# PHY412_Visualizers

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
