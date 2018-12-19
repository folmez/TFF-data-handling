START_YEAR = 1900
END_YEAR = 2100
DEFAULT_MATCH_ARCHIVE = '/home/folmez/Dropbox/Documents/WWW/not_public/matches_1_300k_Dec14_2018.csv'
DEFAULT_REFEREE_ARCHIVE = '/home/folmez/Dropbox/Documents/WWW/not_public/matches_1_300k_Dec14_2018_HAKEMLER.csv'

from .read_csv_into_df import read_matches
from .read_csv_into_df import read_referees
# from .search_ref_archive import name_to_tff_hakem_id
# from .search_ref_archive import name_to_area
from .search_ref_archive import tff_hakem_id_to_name
from .search_ref_archive import tff_hakem_id_to_area
from .seasons import get_season_info
from .search_match_archive import leagues
