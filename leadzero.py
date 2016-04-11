# coding: utf-8
import os
import argparse


def main():
    """
    Remove or ad lead zero to files name.

    example:

    folder:
    1.jpg
    2.jpg
    10.jpg

    >>> leadzero.py
    folder:
    01.jpg
    02.jpg
    10.jpg

    >>> leadzero.py -l 3
    folder:
    001.jpg
    002.jpg
    010.jpg

    >>> leadzero.py -r
    folder:
    01.jpg
    02.jpg
    10.jpg

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--remove", help="Remove lead zero", action='store_true' )
    parser.add_argument("-l", "--length", help="How long should be name. Default 2 signs")
    parser.add_argument("-t", "--type", help="File type - default: jpg")
    args = parser.parse_args()

    length = 2
    ftype = "jpg"

    if args.length:
        try:
            length = int(args.length)
        except ValueError:
            raise ValueError("length should be a number")

        if length < 1:
            raise ValueError(u"length should be equla o greater than 1. If You wan't to remove zeros then You should use -r flag")            

    if args.type:
        ftype = args.type

    cur_dir = os.getcwd()
    
    files = [f for f in os.listdir(cur_dir) if (os.path.isfile(os.path.join(cur_dir, f)) and f.endswith(ftype))]

    for file in files:
        name = ""
        namelength = len(file.split(".")[0])
        if args.remove:
            if file.startswith("0"):
                name = file[1:]
                
        else:
            if length - namelength > 0:
                name = "0"*(length - namelength) + file
        
        if name:
            os.rename(file, name)

if __name__ == "__main__":
    main()