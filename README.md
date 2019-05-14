# acleanhome
Console utility to help you identify unused folders in your system (to clean your Linux $HOME, for example).

## Usage

`python3 acleanhome.py [folder1] [folder2] [folder3] [...]`

For example. the following invocation will help you identify old configuration files in your home folder:

`python3 acleanhome.py ~/.[^.]*/`

The script will then look into each of the given folders and determine which file inside it has been most recently accessed. The output of the program will be a list of each folder, proceeded by that date.

Assuming a configuration file in your system hasn't been accessed for a long time (months or years), it is probably safe to delete them. Proceed at your own risk though, it is advised your should understand what you are doing.

## Rationale

Old configuration files are harmless to your system and usually take very little space compaed to modern hard drive capabilities. However, since so many of them sit at your Linux $HOME directory, after years of using the same system installation, those junk files can start to pile up enough that opening the directory itself can become noticiably slow, due to so many of them being there - and it being your home folder, it means you're using it a lot and that slow down is affecting you every single time. Once that point is reached, a cleaning is probably in order.

Many users would prefer to just start a brand-new install of their operating system, with a clean home folder to boot into - but for those lazy, busy or otherwise relutanct to do it for any reason, A Clean Home can help where existing cleaning solutions either fail to address this particular problem or are over engineered to the point of not being worth the trouble.

Although this script is originally intended for Linux and its home directories, it works on any operating system that can run Python and any other scenario where recursively checking most-recent access dates is required.

## TODO

Would be nice to move old files to the system trash folder automatically or prompt for removal on a case-by-case basis, however Python doesn't seem to officialy support Trash capabilities at the current moment. Feel free to contribute with this or other improvements!
