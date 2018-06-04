import argparse
from pyspriter import Sprite

TOOL_DESCRIPTION = """Command line sprite generator module for Python"""

def main():
    parser = argparse.ArgumentParser(description=TOOL_DESCRIPTION)
    parser.add_argument("--in", dest="folder", metavar="TARGET_FOLDER", required=True,
            help="path with the target images in it. images must be named like 1.png, 2.png, ...")
    parser.add_argument("--ext", dest="extension", metavar="TARGET_EXTENSION", default="jpg",
            help="extension of target images. (default = jpg)")
    parser.add_argument("--out", dest="output", metavar="OUTPUT", required=True,
            help="path and name of output file")
    parser.add_argument("--dir", dest="direction", metavar="DIRECTION", choices=['square','right','left','up','down'], default='right',
            help="direction of the sprite orientation")
    parser.add_argument("--bkg", dest="background", metavar="BACKGROUND", default="white",
            help="background type for the generated sprite")
    
    args = parser.parse_args()

    sprite = Sprite(args.folder, args.extension, args.background, args.direction)
    output = sprite.generate()
    output.save(args.output)

if __name__ == "__main__":
    main()
