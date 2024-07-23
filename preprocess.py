import argparse
import sys

import helper
from helper import open_pandas, write_pandas


def main():
    parser = argparse.ArgumentParser(description='Proses input dan output file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path ke file input')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path ke file output')

    if len(sys.argv) < 1:
        helper.write_to_syserr(parser.print_help())

    args = parser.parse_args()

    file_input = helper.name_and_file_type(args, 'input')
    output = helper.name_and_file_type(args, 'output')

    if file_input.is_err():
        helper.write_to_syserr(file_input.unwrap_err())

    if output.is_err():
        helper.write_to_syserr(file_input.unwrap_err())

    file_input = file_input.unwrap()
    output = output.unwrap()

    df = (open_pandas(file_input[0], file_input[1])
          .unwrap_or_raise("Error when opening dataset"))

    write_pandas(df, output=output[0], file_type=output[1])


if __name__ == "__main__":
    main()
