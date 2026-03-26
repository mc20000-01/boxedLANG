from bx_rs import BoxedRS as bxrs
import pathlib as file
import os.path
from colorama import Fore, Back, Style
import time
import sys
import argparse

parser = argparse.ArgumentParser(description="boxedLANG interpreter")
parser.add_argument("file", help="path to the boxedLANG source file to run")
args = parser.parse_args()

def main():
    rs = bxrs()
    CODE = str(file.Path(os.path.expanduser(args.file)).read_text())
    rs.start(CODE, args.file)
    test = 7
    while test != {"end": "script"}:
        cur = rs.recv()
        match cur["cmd"]:
            case "say":
                print(cur["say"])
                time.sleep(int("0" + cur["time"]))

            case "ask":
                rs.send(input(cur["ask"] + ": "))

            case "end":
                exit()
            

if __name__ == "__main__":
    main()
