#!/usr/bin/env python

from unittest import TestCase, main
from pyspriter import Sprite

class PyspriterTest(TestCase):

    def test_generate(self):
        sprite = Sprite("test_images/", "png", "transparent", "right")
        output = sprite.generate()
        result = sprite.check_output(output)
        self.assertEqual(result, True)

if __name__ == '__main__':
    main()
