import src

TEST_FILENAME = 'tests/sample_files/sample_matches_1000_1010.csv'

def test_read_csv_into_data_frame():
    df = src.read_csv_into_data_frame(TEST_FILENAME)

    assert df['TFF Match ID'].dtype == 'int64'
    assert df['Deplasman skor'].dtype == 'int64'
    assert df['Tarih'].dtype == 'datetime64[ns]'
