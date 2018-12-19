from variables import DF_refs
import src

def test_tff_hakem_id_to_name():
    assert src.tff_hakem_id_to_name(1081353, DF_refs) == 'RIZA EGE'

def test_tff_hakem_id_to_area():
    assert src.tff_hakem_id_to_area(1081353, DF_refs) == 'YALOVA'
