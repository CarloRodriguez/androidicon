#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess
from itertools import izip

img = ''
resFolder = ''
iconType = ''
baselineAsset = 0
iconFileName = ''

instructions = 'Create Android icons\n'
instructions += 'android-icon.py [icon type] [image input] [res folder]\n\n'
instructions += 'Icon type options:\n'
instructions += 'launcher    -> Launcher icons\n'
instructions += 'stat_notify -> Status bar icons\n'
instructions += 'menu        -> Menu icons and Action Bar icons\n'
instructions += 'dialog      -> Dialog icons\n'
instructions += 'generic     -> Generic icons (can specify baseline)\n'
instructions += '\nThe recommended image input size is at least 512x512'

if len(sys.argv) == 1:
    print instructions
    exit()
elif len(sys.argv) > 4:
    print 'Invalid argument\n'
    print instructions
    exit()
else:
    iconType = sys.argv[1]
    img = sys.argv[2]
    resFolder = sys.argv[3]

command = 'convert --version'
output = subprocess.call(command, shell=True)
if output != 0:
    print 'Please install ImageMagick'
    exit()


def getFileName(prefix):
    global iconName
    global iconFileName
    iconName = raw_input('Icon name (avoid prefix and file extension): ')
    iconFileName = prefix + '_' + iconName + '.png'

if iconType == 'launcher':
    folder = [resFolder + '/mipmap-ldpi/',
              resFolder + '/mipmap-mdpi/',
              resFolder + '/mipmap-hdpi/',
              resFolder + '/mipmap-xhdpi/',
              resFolder + '/mipmap-xxhdpi/',
              resFolder + '/mipmap-xxxhdpi/']
    baselineAsset = 48
    iconFileName = 'ic_launcher.png'
elif iconType == 'stat_notify':
    folder = [resFolder + '/drawable-ldpi/',
              resFolder + '/drawable-mdpi/',
              resFolder + '/drawable-hdpi/',
              resFolder + '/drawable-xhdpi/',
              resFolder + '/drawable-xxhdpi/',
              resFolder + '/drawable-xxxhdpi/']
    baselineAsset = 24
    getFileName('ic_stat_notify')
elif iconType == 'menu':
    folder = [resFolder + '/drawable-ldpi/',
              resFolder + '/drawable-mdpi/',
              resFolder + '/drawable-hdpi/',
              resFolder + '/drawable-xhdpi/',
              resFolder + '/drawable-xxhdpi/',
              resFolder + '/drawable-xxxhdpi/']
    baselineAsset = 32
    getFileName('ic_menu')
else:
    print '\nIcon type not available'
    exit()

for s in folder:
    command = 'mkdir -p %s' % s
    output = subprocess.call(command, shell=True)
    if output != 0:
        print 'Somenthig went wrong'
        exit()

size = [str(baselineAsset * 0.75) + 'x' + str(baselineAsset * 0.75),
        str(baselineAsset * 1) + 'x' + str(baselineAsset * 1),
        str(baselineAsset * 1.5) + 'x' + str(baselineAsset * 1.5),
        str(baselineAsset * 2) + 'x' + str(baselineAsset * 2),
        str(baselineAsset * 3) + 'x' + str(baselineAsset * 3),
        str(baselineAsset * 4) + 'x' + str(baselineAsset * 4)]

for x, y in izip(size, folder):
    command = 'convert %s -resize %s %s' % (img, x,
                                            y + iconFileName)
    output = subprocess.call(command, shell=True)
    if output != 0:
        print 'Somenthig went wrong'
        exit()

print 'Complete'
