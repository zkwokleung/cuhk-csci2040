import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str)
parser.add_argument('output_file', type=str)
args = parser.parse_args()
try:
    with open(args.input_file) as file:
        pass
except:
    pass
