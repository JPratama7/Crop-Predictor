import argparse
import pathlib
import sys

import numpy as np
import pandas as pd
from result import Result, Ok, Err


def write_to_syserr(err):
    sys.stderr.write(err)
    sys.exit(1)


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


def open_pandas(input_file: str, file_type: str) -> Result[pd.DataFrame, str]:
    match file_type:
        case 'csv':
            return Ok(pd.read_csv(input_file))
        case 'excel':
            return Ok(pd.read_excel(input_file))
        case _:
            return Err("Invalid file type")


def write_pandas(df: pd.DataFrame, output: str, file_type: str) -> Result[str, str]:
    if not pathlib.Path(output).parent.is_dir():
        return Err("path error")

    match file_type:
        case 'csv':
            df.to_csv(output)
            return Ok("")
        case 'excel':
            df.to_excel(output)
            return Ok("")
        case _:
            return Err("Invalid file type")


def argument_parser():
    parser = argparse.ArgumentParser(description='Proses input dan output file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path ke file input')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path ke file output')
    if len(sys.argv) < 1:
        write_to_syserr(parser.print_help())
    args = parser.parse_args()
    return args


# Membuat function change data type
def clean_data(value):
    if not isinstance(value, str):
        if isinstance(value, int):
            return float(value)
        if isinstance(value, float):
            return value
        return np.nan
    if value == '-':
        return np.nan

    rb = value.replace(" ", "").split(",", 1)
    if len(rb) > 1:
        value = rb[0] + "." + rb[1]
    elif len(rb) == 1:
        value = rb[0]
    return float(value.replace(',', '.').strip())
