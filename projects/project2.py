# B klasman yardimci hakem bolge mac sayilari karsilastirmasi

import src
import helpers
import datetime
import pandas as pd

# TO-DO: filter out of klasman referees

KLASMAN = 'C Klasman Yardımcı Hakemi'
ORG = 'TFF 3. Lig (Profesyonel Takım)'

DF_matches, DF_refs = helpers.get_archive_as_dataframes()

START_DATETIME = datetime.datetime(2018,8,1,0,0,0)
END_DATETIME = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

# Drop out-of-range matches
DF_matches = helpers.drop_old_matches(DF_matches, START_DATETIME, END_DATETIME)

# Drop out-of-organization matches
DF_matches = helpers.drop_out_of_organization_matches(DF_matches, [ORG])

# Get unique assistant referee ID list
AR_list = helpers.get_unique_AR_list(DF_matches)

df_mac_count = pd.DataFrame()
for ar_id in AR_list:
    count = helpers.get_AR_mac_count(ar_id, DF_matches, ORG)
    df_mac_count = df_mac_count.append(\
        {'id': ar_id, 'name': src.tff_hakem_id_to_name(ar_id, DF_refs), \
        '#count': count, 'area': src.tff_hakem_id_to_area(ar_id, DF_refs)}, \
        ignore_index=True)

df_mac_count = df_mac_count.astype({'id': int, 'name': str, \
                                    '#count': int, 'area': str})

print(df_mac_count.sort_values(by=['#count']))

unique_area_list = df_mac_count['area'].unique()
df_area_avg = pd.DataFrame()
for area in unique_area_list:
    df_temp = df_mac_count[df_mac_count['area']==area]
    df_area_avg = df_area_avg.append(\
        {'area': area, 'avg': df_temp['#count'].mean(), \
        'std': df_temp['#count'].std()}, \
        ignore_index=True)

df_area_avg = df_area_avg.astype({'area': str, 'avg': float, 'std': float})

print(df_area_avg.sort_values(by=['avg']))
