#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from itertools import izip
import argparse
from argparse import RawTextHelpFormatter
import os

description = 'Create Android icons\n'
description += 'android-icon [icon type] [image input] [res folder]\n\n'
description += 'Icon type options:\n'
description += 'launcher    -> Launcher icons\n'
description += 'stat_notify -> Status bar icons\n'
description += 'menu        -> Menu icons and Action Bar icons\n'
description += 'dialog      -> Dialog icons\n'
description += 'generic     -> Generic icons (can specify baseline)\n'
description += '\nThe recommended image input size is at least 512x512'

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=RawTextHelpFormatter)
parser.add_argument("type",
                    choices=["launcher", "stat_notify", "menu", "dialog",
                             "generic"],
                    help="Icon type")
parser.add_argument("image",
                    help="Image input")
parser.add_argument("directory",
                    help="res/ directory",
                    action="store")
args = parser.parse_args()

iconType = args.type
img = args.image
resDir = os.path.join(args.directory, '')

drawableFolders = [resDir + 'drawable-ldpi/',
                   resDir + 'drawable-mdpi/',
                   resDir + 'drawable-hdpi/',
                   resDir + 'drawable-xhdpi/',
                   resDir + 'drawable-xxhdpi/',
                   resDir + 'drawable-xxxhdpi/']

mipmapFolders = [resDir + 'mipmap-ldpi/',
                 resDir + 'mipmap-mdpi/',
                 resDir + 'mipmap-hdpi/',
                 resDir + 'mipmap-xhdpi/',
                 resDir + 'mipmap-xxhdpi/',
                 resDir + 'mipmap-xxxhdpi/']

baselineAsset = 0
iconFileName = ''

output = subprocess.call('convert --version', shell=True)
if output != 0:
    print 'Please install ImageMagick'
    exit()


def getFileName(prefix):
    global iconFileName
    iconName = raw_input('Icon name (avoid prefix and file extension): ')
    iconFileName = prefix + '_' + iconName + '.png'


def getBaselineAsset():
    global baselineAsset
    while True:
        try:
            baselineAsset = int(raw_input('Desired baseline (e.g. 48): '))
            break
        except ValueError:
            print "Oops! That was no valid number. Try again..."

folders = drawableFolders

if iconType == 'launcher':
    folders = mipmapFolders
    baselineAsset = 48
    iconFileName = 'ic_launcher.png'
elif iconType == 'stat_notify':
    baselineAsset = 24
    getFileName('ic_stat_notify')
elif iconType == 'menu':
    baselineAsset = 32
    getFileName('ic_menu')
elif iconType == 'dialog':
    baselineAsset = 32
    getFileName('ic_dialog')
elif iconType == 'generic':
    getBaselineAsset()
    getFileName('ic')
else:
    print '\nIcon type not available'
    exit()

for folder in folders:
    command = 'mkdir -p %s' % folder
    output = subprocess.call(command, shell=True)
    if output != 0:
        print "Something went wrong: can't create directories."
        exit()

size = [str(baselineAsset * 0.75) + 'x' + str(baselineAsset * 0.75),
        str(baselineAsset * 1) + 'x' + str(baselineAsset * 1),
        str(baselineAsset * 1.5) + 'x' + str(baselineAsset * 1.5),
        str(baselineAsset * 2) + 'x' + str(baselineAsset * 2),
        str(baselineAsset * 3) + 'x' + str(baselineAsset * 3),
        str(baselineAsset * 4) + 'x' + str(baselineAsset * 4)]

for x, y in izip(size, folders):
    command = 'convert %s -resize %s %s' % (img, x,
                                            y + iconFileName)
    output = subprocess.call(command, shell=True)
    if output != 0:
        print "Something went wrong: can't resize images."
        exit()

print 'Complete!'
