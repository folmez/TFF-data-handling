import pandas as pd
import csv

NR_OF_EXPECTED_FIELDS_IN_MATCH_ARCHIVE = 19
NR_OF_EXPECTED_FIELDS_IN_REF_ARCHIVE = 6

def read_referees(filename, silent=False, number_of_lines = 10):
    # Check whether csv file contains any faulty rows
    check_number_of_fields(filename, NR_OF_EXPECTED_FIELDS_IN_REF_ARCHIVE)

    # Load the csv file
    df = pd.read_csv(filename, quoting = csv.QUOTE_NONE)

    # Fix the first and the last entries, they both have an extra quote
    df['TFF Hakem ID'] = df['TFF Hakem ID'].apply(lambda x: int(x[1:]))
    df['Area'] = df['Area'].apply(lambda x: x[:-1])

    # Convert Lisans numbers into integer
    df['Lisans'] = df['Lisans'].apply(lambda x: int(x))

    if not silent:
        print(df.head(number_of_lines))

    return df

def read_matches(filename, silent=False, number_of_lines = 10):
    # Check whether csv file contains any faulty rows
    check_number_of_fields(filename, NR_OF_EXPECTED_FIELDS_IN_MATCH_ARCHIVE)

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

def check_number_of_fields(filename, expected_number):
    # Number of fields should be exactly one more than the number of commas
    # This check was added because match ID 47373 contains a referee whose name
    # contains a comma
    with open(filename) as f:
        for row in f:
            if row.count(',') is not expected_number-1:
                print(row)
            assert row.count(',') is expected_number-1
