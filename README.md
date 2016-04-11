# HOW TO

## Install 

* copy repository, and unpack
* if You have folder with some usefull tools, and this folder is in system PATH, just copy dist/leadzero.exe (on WINDOWS) to this folder. If You don't have such folder I strongly recommend You to create one and add it to system PATH. 

## examples of use

```bash
> leadzero -h
usage: leadzero [-h] [-r] [-l LENGTH] [-t TYPE]

optional arguments:
  -h, --help            show this help message and exit
  -r, --remove          Remove lead zero
  -l LENGTH, --length LENGTH
                        How long should be name. Default 2 signs
  -t TYPE, --type TYPE  File type - default: jpg

>ls
1.jpg 2.jpg 1.png 2.png 10.jpg 10.png

>leadzero
>ls
01.jpg 02.jpg 1.png 2.png 10.jpg 10.png

>leadzero -r
>ls
1.jpg 2.jpg 1.png 2.png 10.jpg 10.png

>leadzero -t png
>ls
1.jpg 2.jpg 01.png 02.png 10.jpg 10.png

>leadzero -l 3
>ls
001.jpg 002.jpg 01.png 02.png 010.jpg 10.png

>leadzero -t png -r
001.jpg 002.jpg 01.png 2.png 010.jpg 10.png

>leadzero -r
01.jpg 02.jpg 01.png 2.png 10.jpg 10.png

```

