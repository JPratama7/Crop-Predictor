import pandas as pd

import argparse
import sys

from result import Result, Err, Ok


def name_and_file_type(args: argparse.Namespace, key: str) -> Result[tuple[str, str], str]:
    arg = vars(args)

    if key not in arg:
        return Err("Key not found")

    arg_val = arg[key]

    if arg_val.endswith('.xlsx'):
        return Ok((arg_val, 'excel'))

    if arg_val.endswith('.csv'):
        return Ok((arg_val, 'csv'))

    return Err("data type not supported")

def main():
    parser = argparse.ArgumentParser(description='Proses input dan output file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path ke file input')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path ke file output')

    if len(sys.argv) < 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    file_input = name_and_file_type(args, 'input')
    output = name_and_file_type(args, 'output')

    if file_input.is_err():
        sys.stderr.write(file_input.unwrap_err())
        sys.exit(1)

    if output.is_err():
        sys.stderr.write(output.unwrap_err())
        sys.exit(1)

    df = pd.DataFrame()

    # Normalize Kabupaten
    df['Kabupaten'] = df['Kabupaten'].str.replace('Kab. ', '')
    df['Kabupaten'] = df['Kabupaten'].str.replace('Kabupaten ', '')


if __name__ == "__main__":
    main()
