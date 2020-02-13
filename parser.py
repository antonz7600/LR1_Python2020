import argparse
import first
import fib
import second
import third
import fourth

"""
Parser for LR1
input like:
    python parser.py [module_name] [path_to_file.txt]
    
List of modules:
    1. first - sorts text by most-often used words
    2. second - makes 10-words sentence from most-used words in given text
    3. third - quick sort of list of numbers
    4. fourth - merge sort of list of numbers
    5. fib - calculating fibonacci numbers from 1 to number, which is given in input file

"""

parser = argparse.ArgumentParser()
parser.add_argument('module_name', type=str, help='Input module name')
parser.add_argument('input_file', type=str, help='Input file location')
args = parser.parse_args()
if args.module_name == "first":
    first.first(args.input_file)
elif args.module_name == "second":
    second.second(args.input_file)
elif args.module_name == "third":
    third.third(args.input_file)
elif args.module_name == "fourth":
    fourth.fourth(args.input_file)
elif args.module_name == "fib":
    fib.fib(args.input_file)
