import pandas as pd

import argparse
import sys

import helper

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


    df = pd.DataFrame()

    match file_input.unwrap():
        case "csv":
            df = pd.read_csv(file_input.unwrap())
        case "excel":
            df = pd.read_excel(file_input.unwrap())


    print(df)

if __name__ == "__main__":
    main()
