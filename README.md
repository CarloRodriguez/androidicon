## Create Android Icons

Create Android icons simply.

It creates the resource directories needed if not exits, including
mipmap folders for launcher icons.

It resizes your icons accordingly to the corresponding resource
folder.

Choose an icon type to get default baseline or specify your own
baseline.

## Icon types

Choose your icon type and get the right baseline size for the icon purpose.

* launcher - Launcher icons
* stat_notify - Status bar icons
* menu - Menu icons and Action Bar icons
* dialog - Dialog icons
* fab - Floating action button icons
* generic - Generic icons (can specify baseline)

## Examples

**Example 1**

`androidicon launcher icon.png res/`

Result:

```
res/mipmap-ldpi/ic_launcher.png
res/mipmap-mdpi/ic_launcher.png
res/mipmap-hdpi/ic_launcher.png
res/mipmap-xhdpi/ic_launcher.png
res/mipmap-xxhdpi/ic_launcher.png
res/mipmap-xxxhdpi/ic_launcher.png
```

**Example 2**

`androidicon menu icon.png res/`

It will prompt for icon name, if I input `info` the result is:

```
res/drawable-ldpi/ic_menu_info.png
res/drawable-mdpi/ic_menu_info.png
res/drawable-hdpi/ic_menu_info.png
res/drawable-xhdpi/ic_menu_info.png
res/drawable-xxhdpi/ic_menu_info.png
res/drawable-xxxhdpi/ic_menu_info.png
```

**Example 3**

`androidicon generic icon.png res/`

It will prompt for icon name and baseline, if I input `info` and a
base line of 64 the result is:

```
res/drawable-ldpi/ic_info.png
res/drawable-mdpi/ic_info.png
res/drawable-hdpi/ic_info.png
res/drawable-xhdpi/ic_info.png
res/drawable-xxhdpi/ic_info.png
res/drawable-xxxhdpi/ic_info.png
```

## Installation

`pip install androidicon`

Run `androidicon -h` for help.
