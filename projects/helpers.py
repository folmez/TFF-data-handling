import src

def drop_out_of_organization_matches(df_matches, org_list):
    return df_matches[df_matches['Organizasyon'].isin(org_list)]

def drop_old_matches(df_matches, start, end):
    df_matches = df_matches.drop(df_matches[df_matches['Tarih'] < start].index)
    df_matches = df_matches.drop(df_matches[df_matches['Tarih'] > end  ].index)

    return df_matches

def get_unique_AR_list(df_matches):
    AR1_set = set(df_matches['AR1 ID'].unique())
    AR2_set = set(df_matches['AR2 ID'].unique())
    unique_AR_ID_list = list(AR1_set.union(AR2_set))
    return unique_AR_ID_list

def drop_out_of_area_referees(hakem_IDs, df_refs, area_set):
    return [id for id in hakem_IDs if src.tff_hakem_id_to_area(id, df_refs) in area_set]

def get_AR_mac_count(AR_id, df_matches, org, silent=True):
    df_matches = df_matches[ (df_matches['AR1 ID'] == AR_id) | \
                (df_matches['AR2 ID'] == AR_id) ]
    df_org = df_matches[ df_matches['Organizasyon'] == org]
    if not silent:
        print(df_org)
    return len(df_org.index)

def get_archive_as_dataframes():
    match_archive = src.DEFAULT_MATCH_ARCHIVE
    ref_archive = src.DEFAULT_REFEREE_ARCHIVE
    print('Match archive:', match_archive)
    print('Referee archive:', ref_archive)

    DF_matches = src.read_matches(match_archive, silent=True)
    DF_refs = src.read_referees(ref_archive, silent=True)

    return DF_matches, DF_refs
