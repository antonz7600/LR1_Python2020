import argparse
import most_words
import fib
import stc_most_words
import qck_sort
import mrg_sort
import fib_gen

"""
Parser for LR1
input like:
    python parser.py [module_name] [path_to_file.txt]
    
List of modules:
    1. most_words - sorts text by most-often used words
    2. stc_most_words - makes 10-words sentence from most-used words in given text
    3. qck_sort - quick sort of list of numbers
    4. mrg_sort - mergesort of list of numbers
    5. fib - calculating fibonacci with help of summing prev elements. Starts with 1,1
    6. fib_gen - calculating fibonacci with a help of golden ring. Starts with 0,1

"""
parser = argparse.ArgumentParser()
parser.add_argument('module_name', type=str, help='Input module name')
parser.add_argument('input_file', type=str, help='Input file location')
args = parser.parse_args()
if args.module_name == "most_words":
    most_words.most_words(args.input_file)
elif args.module_name == "stc_most_words":
    stc_most_words.stc_most_words(args.input_file)
elif args.module_name == "qck_sort":
    qck_sort.qck_sort(args.input_file)
elif args.module_name == "mrg_sort":
    mrg_sort.mrg_sort(args.input_file)
elif args.module_name == "fib":
    fib.fib(args.input_file)
elif args.module_name == "fib_gen":
    fib_gen.fib_gen(args.input_file)
else:
    print("Incorrect module name")
    exit(-1)
