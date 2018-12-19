import src

HOME_FOLDER  = '/home/folmez/Dropbox/Research1/fun-experiments/TFF-data-handling/'
TEST_MATCH_FILENAME = HOME_FOLDER + 'tests/sample_files/sample_matches_1000_1010.csv'
DF_matches = src.read_matches(TEST_MATCH_FILENAME, silent=True)

def test_leagues():
    src.leagues(df=DF_matches)
    assert set(src.leagues(df=DF_matches)) == set([\
                                    'Türk Telekom Lig A (Profesyonel Takım)', \
                                    'Lig B Kademe (Profesyonel Takım)', \
                                    'TFF 3. Lig (Profesyonel Takım)'])
