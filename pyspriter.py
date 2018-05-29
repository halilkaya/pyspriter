"""
Command line sprite generator module for Python
"""
#!/usr/bin/env python
#-*-coding: utf-8-*-
__name__ = "pyspriter"
__description__ = "Command line sprite generator module for Python"
__author__ = "Halil Kaya <halil@halilkaya.net>"
__version__ = "0.1"
__license__ = "MPL 2.0"

from PIL import Image
from os import listdir
from os.path import isfile, join

class Sprite:

	folder = None
	extension = None
	background = None
	direction = None

	def __init__(self, folder="images/", extension="jpg", background="white", direction="right"):
		"""
		Sprite output initialization
		"""
		self.folder = folder
		self.extension = extension
		self.background = background
		self.direction = direction
		self.images = [ f for f in listdir(folder) if isfile(join(folder,f)) ]
		self.count = len(self.images)
		self._create()

	def _loop_values(self):
		"""
		Gets beginning and finish values of loop for sprite direction
		"""
		d = self.direction
		c = self.count
		if d == 'right' or d == 'down' or d == 'square':
			return 1, c+1, 1
		if d == 'left' or d == 'up':
			return c, 0, -1

	def _size(self):
		"""
		Gets width and height of sprite
		"""
		width = 0
		height = 0
		d = self.direction
		b,f,i = self._loop_values()
                maxWidth = 0
                maxY = 0
		for i in range(b, f, i):
			img = Image.open(self.folder + str(i) + '.' + self.extension)
			x, y = img.size
                        if d == 'square':
                                width += x
                                if width > maxWidth:
                                    maxWidth = width
                                if y > maxY:
                                    maxY = y
                                if i % self._isqrt(self.count) == 0:
                                    width = 0
                                    height += maxY
                                    maxY = 0
			elif d == 'right' or d == 'left':
				width += x
				if y > height:
					height = y
			elif d == 'up' or d == 'down':
				height += y
				if x > width:
					width = x
                if maxWidth >= width:
                    width = maxWidth
                    height += maxY
		return width, height

	def generate(self):
		"""
		Generates the sprite with given images
		"""
		try:
			left = 0
                        lefty = 0
			d = self.direction
			b,f,i = self._loop_values()
			for i in range(b, f, i):
				img = Image.open(self.folder + str(i) + '.' + self.extension)
				x, y = img.size
                                if d == 'square':
                                        self.sprite.paste(img, (left, lefty))
                                        left += x
                                        if left >= self._size()[0]:
                                            left = 0
                                            lefty += y
				elif d == 'right' or d == 'left':
					self.sprite.paste(img, (left, 0))
					left += x
				elif d == 'up' or d == 'down':
					self.sprite.paste(img, (0, left))
					left += y
		except Exception as e:
			return None
		return self.sprite

	def check_output(self, output):
		if output:
			return True
		return False

	def _create(self):
		self.sprite = Image.new("RGBA", self._size())

        def _isqrt(self, n):
            x = n
            y = (x + 1) // 2
            while y < x:
                x = y
                y = (x + n //x) //2
            return x
