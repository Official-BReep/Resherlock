import argparse
from sys import version_info
from argparse import ArgumentParser
from resherlock import ReSherlock
from sort import *


def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

    # return string
    return new

parser = ArgumentParser(prog="Resherlock",exit_on_error=True)
parser.add_argument("-o", "--output", help="Write the Output in a text File")
parser.add_argument("-s", "--supported", action="store_true", help="Get all supported Sites")
parser.add_argument("-S", "--sort", action="store_true", help=argparse.SUPPRESS) #Option to sort te Site List
parser.add_argument("-md", "--genmd", action="store_true", help=argparse.SUPPRESS) #Option to generate the md of supported Sites
parser.add_argument("-a", "--print_all", action="store_true", help="Get all results(successfull, failed and so on)")
parser.add_argument("--nsfw", action="store_true", help="Get NSFW results too")
parser.add_argument("-t", "--target",nargs='+', type=list, help="Set the Target(s)")
args = parser.parse_args()
check = version_info >= (3,)

if check:
    if args.target != None:
        for n,i in enumerate(args.target):
            args.target.pop(0)
            args.target.append(convert(i))
            resherlock = ReSherlock(args)
            output = resherlock.run()
            for service in output:
                print(service)

    if args.sort:
        print(sort_json())

    if args.supported:
        print(supported())

    if args.genmd:
        print(genmd())
