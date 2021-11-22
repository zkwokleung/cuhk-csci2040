import argparse
import re


def read_file(file_name, output, include_file_name=False):
    # process a single file
    try:
        c = w = l = d = 0
        with open(file_name, 'r') as file:
            for line in file:
                c += len(re.findall('[a-zA-Z]', line))
                w += len(re.findall('[a-zA-Z]+', line))
                l += 1
                d += len(re.findall('[0-9]', line))

        if include_file_name:
            output.write(f"Name of file: {file_name}\n")
        output.write(f"Number of characters: {c}\n")
        output.write(f"Number of words: {w}\n")
        output.write(f"Number of lines: {l}\n")
        output.write(f"Number of digits: {d}\n")
    except IOError:
        print("Opening file", file_name, "failed!")


parser = argparse.ArgumentParser(
    description="Counter characters inside a file")
parser.add_argument('input_file', type=str,
                    help="The file to be processed.", nargs='+')
parser.add_argument('output_file', type=str,
                    help="The file where the result are stored.")
args = parser.parse_args()

if all(list(map(lambda s: '?' in s or '*' in s, args.input_file))):
    print("No matching!")
else:
    with open(args.output_file, 'w') as opt:
        for i in args.input_file:
            read_file(i, opt, len(args.input_file) > 1)
