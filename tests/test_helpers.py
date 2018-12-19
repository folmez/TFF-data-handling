from variables import DF_matches, DF_refs
import projects

def test_get_unique_AR_list():
    assert set(projects.get_unique_AR_list(DF_matches)) == set([17774,20747, \
                                                                19963,20144, \
                                                                18958,20887, \
                                                                20565,19158, \
                                                                19521,20442, \
                                                                19973,20799, \
                                                                19630,20865, \
                                                                19761,20458, \
                                                                1064323,20660])

def test_drop_out_of_area_referees():
    hakem_IDs = [1081344,1081353,1376258,1376267,19541,1376271]
    area_set = ['YALOVA', 'KONYA']
    area_refs = [1081344,1081353,1376258,1376271]
    assert set(projects.drop_out_of_area_referees(hakem_IDs, DF_refs, area_set)) == \
                set(area_refs)

def test_get_AR_mac_count():
    assert projects.get_AR_mac_count(17774, DF_matches, \
                        'Lig B Kademe (Profesyonel Takım)') == 1
    assert projects.get_AR_mac_count(17774, DF_matches, \
                        'Türk Telekom Lig A (Profesyonel Takım)') == 0
