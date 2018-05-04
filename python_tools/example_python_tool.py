import argparse


def make_fingerprint(output_filename):
    print "This will be printed to stdout and the log"

    with open(output_filename, 'w') as f:
        f.write('HELLO FINGERPRINT')


def do_fingerprint(args):
    make_fingerprint(args.output_file)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help="picard interval list", required=True)
    # parser.add_argument("-o", "--output_file", help="output bed file", required=True)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    do_fingerprint(args)
