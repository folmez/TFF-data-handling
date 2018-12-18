import src

ARCHIVE_FILENAME = src.DEFAULT_REFEREE_ARCHIVE
DF = src.read_referees(ARCHIVE_FILENAME, silent=True)

def name_to_tff_hakem_id(name, df=DF):
    return df.loc[df['Name'] == name, 'TFF Hakem ID'].tolist()

def name_to_area(name, df=DF):
    area_list = df.loc[df['Name'] == name, 'Area'].tolist()
    if len(area_list) > 1:
        raise Exception('more than one area for {}'.format(name))
    [area] = df.loc[df['Name'] == name, 'Area'].tolist()
    return df.loc[df['Name'] == name, 'Area'].tolist()

def tff_hakem_id_to_name(tff_hakem_id, df=DF):
    return df.loc[df['TFF Hakem ID'] == tff_hakem_id, 'Name'].tolist()

def tff_hakem_id_to_area(tff_hakem_id, df=DF):
    return df.loc[df['TFF Hakem ID'] == tff_hakem_id, 'Area'].tolist()
