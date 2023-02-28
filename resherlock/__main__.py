import sys
import pytermcolor

check = sys.version_info >= (3,)    #check for python3
if check:
    try:
        import argparse
        from argparse import ArgumentParser
        from resherlock import ReSherlock
        from modules.sort import *


        def convert(s):
            new = ""
            for x in s:
                new += x
            return new

        parser = ArgumentParser(exit_on_error=True)
        parser.add_argument("-o", "--output", help="Write the Output in a text File", nargs='*', type=list)
        parser.add_argument("-s", "--supported", action="store_true", help="Get all supported Sites")
        parser.add_argument("-S", "--sort", action="store_true", help=argparse.SUPPRESS) #Option to sort te Site List
        parser.add_argument("-md", "--genmd", action="store_true", help=argparse.SUPPRESS) #Option to generate the md of supported Sites
        parser.add_argument("-a", "--print_all", action="store_true", help="Get all results(successfull, failed and so on)")
        parser.add_argument("--nsfw", action="store_true", help="Get NSFW results too")
        parser.add_argument("-t", "--target",nargs='+', type=list, help="Set the Target(s)")
        args = parser.parse_args()

        if args.output!=None:
            for file in args.output:
                args.output.append(convert(args.output[0]))
                args.output.pop(0)

        if args.target != None:
            for target in args.target:
                args.target.append(convert(args.target[0]))
                args.target.pop(0)

            if args.output!=None:
                if len(args.output)!=len(args.target):
                    pytermcolor.cprint("\nTargets and Output files must have the same length",color="red")
                    sys.exit(1)

            output = ReSherlock(args).run()
            if args.output!=None:
                for file in args.output:
                    print(f"Write {file}")
                    for service in output:
                        print(service)
                    print("\n\n")
            else:
                for service in output:
                    print(service)
                print("\n\n")

        elif args.sort:
            print(sort_json())

        elif args.supported:
            print(supported())

        elif args.genmd:
            print(genmd())
    except KeyboardInterrupt:
        pass
else:
    print("Please use python3")
