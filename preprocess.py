import helper
from helper import open_pandas, write_pandas, argument_parser


def main():
    args = argument_parser()

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

    df['Luas Panen'] = df['Luas Panen'].apply(helper.clean_data)
    df['Hasil Panen'] = df['Hasil Panen'].apply(helper.clean_data)
    df['Produktivitas'] = df['Produktivitas'].apply(helper.clean_data)

    write_pandas(df, output=output[0], file_type=output[1])


if __name__ == "__main__":
    main()
