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

## Games

- [Dr. Brain series](https://www.filfre.net/2018/02/dr-brain/)
- [The Fool's Errand](https://www.fools-errand.com/02-FE/index.htm) (download [Apple Silicon version of Mini vMac](https://www.gryphel.com/c/minivmac/b_dl_std.html))

## Links

- [Installing Microsoft Windows 3.1x in DOSBox-X](https://dosbox-x.com/wiki/Guide%3AInstalling-Windows-3.1x)
- [Windows 3.1](https://archive.org/details/windows-3.1_202103)
- [DOSBox resolution: full screen, window size, clear graphics](https://www.dosgamers.com/dos/dosbox-dos-emulator/screen-resolution)
