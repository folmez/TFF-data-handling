import src

HOME_FOLDER  = '/home/folmez/Dropbox/Research1/fun-experiments/TFF-data-handling/'
TEST_MATCH_FILENAME = HOME_FOLDER + 'tests/sample_files/sample_matches_1000_1010.csv'
TEST_REFEREE_FILENAME = HOME_FOLDER + 'tests/sample_files/sample_HAKEMLER.csv'

REFEREE_NAMES = ['ENGİN ÇALIŞ', 'RIZA EGE', 'HAYRİ TOPBAŞ', \
                    'UĞUR CENAN', 'ABDİL İBİŞ', 'EMRE KOÇYİĞİT']

DF_matches = src.read_matches(TEST_MATCH_FILENAME)
DF_refs = src.read_referees(TEST_REFEREE_FILENAME)

def test_read_match_archive_data_types():

    assert DF_matches['TFF Match ID'].dtype == 'int64'
    assert DF_matches['Deplasman skor'].dtype == 'int64'
    assert DF_matches['Tarih'].dtype == 'datetime64[ns]'

def test_read_referee_archive_data_types():
    assert list(DF_refs['Name'].unique()) == REFEREE_NAMES
