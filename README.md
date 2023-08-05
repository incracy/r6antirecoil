# Rainbow Six Siege Lua Script Installer for Logitech GHub

![Rainbow Six Siege Logo](https://cdn.akamai.steamstatic.com/steam/apps/359550/capsule_616x353.jpg?t=1690498575)

## Description

This program is a Lua script installer designed to work with Logitech GHub for the game Rainbow Six Siege. It allows users to easily switch between different versions of Anti-Recoil scripts for Logitech gaming devices based on their preferences.

These scripts were released publicly inside of a Discord server, where you can install a zip but that contains just the Lua file. The correct way to mass-install scripts in GHub is using programs like mine. With this installer, users can conveniently select and install specific versions of the Lua scripts they want to use in Logitech GHub.

## Features

- Easy installation of new or old versions of anti-recoil Lua scripts for Rainbow Six Siege.
- Able to perform a clean install for scripts
- And of course, anti-recoil in Rainbow Six Siege.

## Installation

1. Download the latest release of the installer from the [Releases](https://github.com/incracy/r6antirecoil/releases/tag/r6) section.
2. Run the installer executable and follow the on-screen instructions.
3. Once it's done, you can press Enter to exit the installer, relaunch GHub and the scripts will be there (if you already have a profile set for anti-recoil)

## Compiling yourself
1. First install all the requirements
```
pip install psutil
pip install pyinstaller
```
2. Run this code:
```
pyinstaller --onefile installer.py --add-data "resources;resources"
```
This will compile the Python script into a singular file with all of the scripts compiled inside of the executable.

## How to use after installation
1. After it's done installing, you can re-run Logitech GHub (as Administrator) if you already have a profile for it.
If you don't already have a profile for it then re-run Logitech GHub and when it loads up go to manage profiles, and in the Games & Applications section scroll until you find Rainbow Six Siege. Look down and press Add Profile for the Selected App. Name it whatever and then click Details. In this menu all you have to do is click "Set as Persistent"
2. Once you've done all of that go back to the manage profiles section and that profile you just made, click the icon to the right of details. At the top it says Active Lua Script choose any operator you want, then when your Caps Lock is on you can just hold Right Click on your mouse and whenever you old down Left Click it will start working!
