import pandas as pd

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Proses input dan output file.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path ke file input')
    parser.add_argument('-o', '--output', type=str, required=True, help='Path ke file output')

    if len(sys.argv) < 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    df = pd.read_excel(args.input)

    # Normalize Kabupaten
    df['Kabupaten'] = df['Kabupaten'].str.replace('Kab. ', '')
    df['Kabupaten'] = df['Kabupaten'].str.replace('Kabupaten ', '')

    print(df.isnull().sum())
    print(df.isna().sum())

if __name__ == "__main__":
    main()
