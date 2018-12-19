from variables import DF_matches, DF_refs

def test_read_match_archive_data_types():

    assert DF_matches['TFF Match ID'].dtype == 'int64'
    assert DF_matches['Deplasman skor'].dtype == 'int64'
    assert DF_matches['Tarih'].dtype == 'datetime64[ns]'

def test_read_referee_archive_data_types():
    assert list(DF_refs['Name'].unique()) == ['ENGİN ÇALIŞ', 'RIZA EGE', \
                                                'HAYRİ TOPBAŞ', 'UĞUR CENAN', \
                                                'ABDİL İBİŞ', 'EMRE KOÇYİĞİT']
