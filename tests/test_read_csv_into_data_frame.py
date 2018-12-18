import src

HOME_FOLDER  = '/home/folmez/Dropbox/Research1/fun-experiments/TFF-data-handling/'
TEST_MATCH_FILENAME = HOME_FOLDER + 'tests/sample_files/sample_matches_1000_1010.csv'
TEST_REFEREE_FILENAME = HOME_FOLDER + 'tests/sample_files/sample_HAKEMLER.csv'

REFEREE_NAMES = ['ENGİN ÇALIŞ', 'RIZA EGE', 'HAYRİ TOPBAŞ', \
                    'UĞUR CENAN', 'ABDİL İBİŞ', 'EMRE KOÇYİĞİT']

def test_read_match_archive_data_types():
    df = src.read_matches(TEST_MATCH_FILENAME)

    assert df['TFF Match ID'].dtype == 'int64'
    assert df['Deplasman skor'].dtype == 'int64'
    assert df['Tarih'].dtype == 'datetime64[ns]'

def test_read_referee_archive_data_types():
    df = src.read_referees(TEST_REFEREE_FILENAME)
    assert list(df['Name'].unique()) == REFEREE_NAMES
