#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from itertools import izip
import argparse
from argparse import RawTextHelpFormatter
import os


class androidicon:
    'Create Android Icons'
    def __init__(self):
        self.description = 'Create Android icons\n'
        self.description += ('androidicon [icon type] [image input] '
                             '[res directory]\n\n')
        self.description += 'Icon type options:\n'
        self.description += 'launcher    -> Launcher icons\n'
        self.description += 'stat_notify -> Status bar icons\n'
        self.description += 'menu        -> Menu icons and Action Bar icons\n'
        self.description += 'dialog      -> Dialog icons\n'
        self.description += ('generic     -> Generic icons '
                             '(can specify baseline)\n')
        self.description += ('\nThe recommended image input size is at least '
                             '512x512')
        parser = argparse.ArgumentParser(description=self.description,
                                         formatter_class=RawTextHelpFormatter)
        parser.add_argument("type",
                            choices=["launcher", "stat_notify", "menu",
                                     "dialog", "generic"],
                            help="Icon type")
        parser.add_argument("image",
                            help="Image input")
        parser.add_argument("directory",
                            help="res/ directory",
                            action="store")
        args = parser.parse_args()
        self.iconType = args.type
        self.img = args.image
        self.resDir = os.path.join(args.directory, '')
        self.drawableFolders = [self.resDir + 'drawable-ldpi/',
                                self.resDir + 'drawable-mdpi/',
                                self.resDir + 'drawable-hdpi/',
                                self.resDir + 'drawable-xhdpi/',
                                self.resDir + 'drawable-xxhdpi/',
                                self.resDir + 'drawable-xxxhdpi/']
        self.mipmapFolders = [self.resDir + 'mipmap-ldpi/',
                              self.resDir + 'mipmap-mdpi/',
                              self.resDir + 'mipmap-hdpi/',
                              self.resDir + 'mipmap-xhdpi/',
                              self.resDir + 'mipmap-xxhdpi/',
                              self.resDir + 'mipmap-xxxhdpi/']
        self.folders = self.drawableFolders
        self.baselineAsset = 0
        self.iconFileName = ''
        self.createAndroidIcon()

    def createAndroidIcon(self):
        self.checkImageMagickInstallation()
        self.getIconInfo()
        self.createResDirectories()
        self.createIcons()

    def checkImageMagickInstallation(self):
        output = subprocess.call('convert --version', shell=True)
        if output != 0:
            print 'Please install ImageMagick'
            exit()

    def getIconInfo(self):
        if self.iconType == 'launcher':
            self.folders = self.mipmapFolders
            self.baselineAsset = 48
            self.iconFileName = 'ic_launcher.png'
        elif self.iconType == 'stat_notify':
            self.baselineAsset = 24
            self.getFileName('ic_stat_notify')
        elif self.iconType == 'menu':
            self.baselineAsset = 32
            self.getFileName('ic_menu')
        elif self.iconType == 'dialog':
            self.baselineAsset = 32
            self.getFileName('ic_dialog')
        elif self.iconType == 'generic':
            self.getBaselineAsset()
            self.getFileName('ic')
        else:
            print '\nIcon type not available'
            exit()

    def getFileName(self, prefix):
        iconName = raw_input('Icon name (avoid prefix and file extension): ')
        self.iconFileName = prefix + '_' + iconName + '.png'

    def getBaselineAsset(self):
        while True:
            try:
                self.baselineAsset = int(
                    raw_input('Desired baseline (e.g. 48): ')
                )
                break
            except ValueError:
                print "Oops! That was no valid number. Try again..."

    def createResDirectories(self):
        for folder in self.folders:
            command = 'mkdir -p %s' % folder
            output = subprocess.call(command, shell=True)
            if output != 0:
                print "Something went wrong: can't create res directories."
                exit()

    def createIcons(self):
        size = [str(self.baselineAsset * 0.75) + 'x'
                + str(self.baselineAsset * 0.75),
                str(self.baselineAsset * 1) + 'x'
                + str(self.baselineAsset * 1),
                str(self.baselineAsset * 1.5) + 'x'
                + str(self.baselineAsset * 1.5),
                str(self.baselineAsset * 2) + 'x'
                + str(self.baselineAsset * 2),
                str(self.baselineAsset * 3) + 'x'
                + str(self.baselineAsset * 3),
                str(self.baselineAsset * 4) + 'x'
                + str(self.baselineAsset * 4)]
        for x, y in izip(size, self.folders):
            command = 'convert %s -resize %s %s' % (self.img, x,
                                                    y + self.iconFileName)
            output = subprocess.call(command, shell=True)
            if output != 0:
                print "Something went wrong: can't resize images."
                exit()

androidicon = androidicon()
