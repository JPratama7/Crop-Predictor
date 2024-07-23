import argparse
import sys

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
