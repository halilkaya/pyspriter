# pyspriter
Command line sprite generator module for Python

### Download
```$ sudo pip install pyspriter```
...or clone the repository.

### Usage
```
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
**direction:** Sprite direction. (It's linear) ```right, left, up or down```

### Notes
  - This module generates sprite with the image names. Names must be like ```1.png, 2.png, 3.png, ...```.