Installation:

# installs manim deps in new env 'manim'
# !! Note: if using Latex, that needs to be installed separately
#          See https://docs.manim.community/en/stable/installation/macos.html#optional-dependencies
conda env create --file environment.yml
conda activate manim


Generating output:

# example
manim -pql manim_demo.py

-ql/qm/qh == quality flags: low, medium, high
-p == auto open movie in default player
