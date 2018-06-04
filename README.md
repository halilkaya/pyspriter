# pyspriter
![travis](https://travis-ci.org/halilkaya/pyspriter.svg?branch=master)

Command line sprite generator module for Python

### Download
```$ sudo pip install pyspriter```

...or clone the repository.

### Usage
```python
from pyspriter import Sprite
sprite = Sprite("images/", "png", "transparent", "right")
output = sprite.generate()
output.save("sprites/my_sprite.png")
```

```
Sprite(folder, extension, background, direction)
```
**folder:** Images folder to generate sprite.

**extension:** Extension of images.

**background:** Background color of sprite.

**direction:** Sprite direction. (It's linear) ```square, right, left, up or down```

#### Command Line Interface
The pyspriter can also be called from the command line.  
Calling `python pyspriter_cli.py -h` prints the help message below.
```
usage: pyspriter_cli.py [-h] --in TARGET_FOLDER [--ext TARGET_EXTENSION] --out
                        OUTPUT [--dir DIRECTION] [--bkg BACKGROUND]

Command line sprite generator module for Python

optional arguments:
  -h, --help            show this help message and exit
  --in TARGET_FOLDER    path with the target images in it. images must be
                        named like 1.png, 2.png, ...
  --ext TARGET_EXTENSION
                        extension of target images. (default = jpg)
  --out OUTPUT          path and name of output file
  --dir DIRECTION       direction of the sprite orientation
  --bkg BACKGROUND      background type for the generated sprite
```

### Notes
  - This module generates sprite with the image names. Names must be like ```1.png, 2.png, 3.png, ...```.
