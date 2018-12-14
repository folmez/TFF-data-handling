import pandas as pd
import csv

NUMBER_OF_EXPECTED_FIELDS = 19

def read(filename, silent=False, number_of_lines = 10):
    # Check whether csv file contains any faulty rows
    check_number_of_fields(filename)

    # Load the csv file
    # 1) Dort ID and Stad ID are sometimes inputted as [], pandas doesn't
    # recognize this.
    df = pd.read_csv(filename, dtype={'Dort ID': object, 'Stad ID': object},\
                                                    quoting = csv.QUOTE_NONE)

    # Replace [] with -1 in the Dort ID and Stad ID columns
    df['Dort ID'] = df['Dort ID'].replace({"[]":"-1"})
    df['Stad ID'] = df['Stad ID'].replace({"[]":"-1"})
    df['Dort ID'] = df['Dort ID'].apply(lambda x: int(x))
    df['Stad ID'] = df['Stad ID'].apply(lambda x: int(x))

    # Fix the first and the last entries, they both have an extra quote
    df['TFF Match ID'] = df['TFF Match ID'].apply(lambda x: int(x[1:]))
    df['Deplasman skor'] = df['Deplasman skor'].apply(lambda x: int(x[:-1]))

    # Convert dates to datetime format
    df['Tarih'] = pd.to_datetime(df['Tarih'], format='%Y-%m-%d %H:%M:%S')

    if not silent:
        print(df.head(number_of_lines))

    return df

def check_number_of_fields(filename):
    # Number of fields should be exactly one more than the number of commas
    # This check was added because match ID 47373 contains a referee whose name
    # contains a comma
    with open(filename) as f:
        for row in f:
            if row.count(',') is not NUMBER_OF_EXPECTED_FIELDS-1:
                print(row)
            assert row.count(',') is NUMBER_OF_EXPECTED_FIELDS-1
