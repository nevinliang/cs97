#!/usr/bin/python

import random, sys
from argparse import ArgumentParser

class genspelldata:
    def __init__(self, args):
        try:
            f = open(args.file[0], 'r')
            self.bad = f.readlines()
            f.close()
        except FileNotFoundError:
            sys.stdout.write("FILE NOT FOUND. PROGRAM TERMINATED.\n")
            return
        try:
            f = open("/usr/share/dict/linux.words", 'r')
            self.good = f.readlines()
            f.close()
        except FileNotFoundError:
            sys.stdout.write("FILE NOT FOUND. PROGRAM TERMINATED.\n")
            return

        for i in range(0, args.reps):
            ans = ""
            for j in range(0, args.bad):
                ans += random.choice(self.bad)
            for j in range(0, args.good):
                ans += random.choice(self.good)
            sys.stdout.write(ans)
            sys.stdout.write("\n")
        return

def main():
    parser = ArgumentParser(description="generates spell data!")
    parser.add_argument("reps")
    parser.add_argument("good")
    parser.add_argument("bad")
    parser.add_argument("file", nargs="*", default="")
    args = parser.parse_args()

    try:
        generator = genspelldata(args)
    except IOError as err:
        parser.error('I/O error({0}): {1}'.format(err.errno, err.strerror))

if __name__ == "__main__":
    main()
