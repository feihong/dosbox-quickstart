# Feihong's DOSBox-X Quickstart

## Installation

Download ZIP file from https://dosbox-x.com/. Decompress ZIP file, copy the dosbox-x-sdl2/dosbox-x application into your Applications directory. Add this to your `~/.zshrc`:

    alias dosbox-x='/Applications/dosbox-x.app/Contents/MacOS/dosbox-x'

### Install Windows 3.1

First, copy all installation files into `~/gaming/install`.

    dosbox-x -conf win31-install.conf
    mount C ~/gaming
    C:
    cd install
    setup

Go through setup wizard, then exit to DOS. Type `exit` to quit DOSBox-X.

You can now start Windows 3.1 by running

    dosbox-x -conf win31.conf    

## Commands

tbd

## Links

- [Installing Microsoft Windows 3.1x in DOSBox-X](https://dosbox-x.com/wiki/Guide%3AInstalling-Windows-3.1x)
- [Windows 3.1](https://archive.org/details/windows-3.1_202103)
- [New Installers for Sierra Games](http://sierrahelp.com/Patches-Updates/NewSierraInstallers.html)
