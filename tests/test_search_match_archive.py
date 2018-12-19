import src

from variables import DF_matches

def test_leagues():
    src.leagues(df=DF_matches)
    assert set(src.leagues(df=DF_matches)) == set([\
                                    'Türk Telekom Lig A (Profesyonel Takım)', \
                                    'Lig B Kademe (Profesyonel Takım)', \
                                    'TFF 3. Lig (Profesyonel Takım)'])
