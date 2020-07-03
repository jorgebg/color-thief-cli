#!/usr/bin/env python3
import argparse

from colorthief import ColorThief
from colr import color


parser = argparse.ArgumentParser(description='Grab the color palette from an image')
parser.add_argument('path', help='image path')
parser.add_argument('counts', metavar='N', type=int, nargs='+',
                    help='Number of colors')
# parser.add_argument('--count', type=int, default=6, help='number of colors (6 by default)')

args = parser.parse_args()


color_thief = ColorThief(args.path)
hexpattern = ' #%02x%02x%02x '

for count in args.counts:
    # dominant color + palette
    palette = [color_thief.get_color(quality=1)] + color_thief.get_palette(color_count=count)
    print(''.join([color(' ' * len(' #000000 '), back=rgb) for rgb in palette]))
    print(''.join([color(hexpattern % rgb) for rgb in palette]))
