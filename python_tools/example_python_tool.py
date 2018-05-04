import argparse


def make_a_file(output_filename):
    print "This will be printed to stdout and the log"

    with open(output_filename, 'w') as f:
        f.write('HELLO EXAMPLE OUTPUT')


def do_stuff(args):
    make_a_file(args.output_file)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help="picard interval list", required=True)
    # Sometimes we want the names of the output files to be provided as inputs
    # That makes it easer to reference them from the CWL files:
    # parser.add_argument("-o", "--output_file", help="output bed file", required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    do_fingerprint(args)
