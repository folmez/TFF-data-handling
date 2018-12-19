import src

HOME_FOLDER  = '/home/folmez/Dropbox/Research1/fun-experiments/TFF-data-handling/'
TEST_REFEREE_FILENAME = HOME_FOLDER + 'tests/sample_files/sample_HAKEMLER.csv'
DF_refs = src.read_referees(TEST_REFEREE_FILENAME, silent=True)

def test_tff_hakem_id_to_name():
    assert src.tff_hakem_id_to_name(1081353, DF_refs) == 'RIZA EGE'

def test_tff_hakem_id_to_area():
    assert src.tff_hakem_id_to_area(1081353, DF_refs) == 'YALOVA'
