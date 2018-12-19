START_YEAR = 1900
END_YEAR = 2100

from pathlib import Path
HOME = str(Path.home())
DEFAULT_MATCH_ARCHIVE = HOME + \
    '/Dropbox/Documents/WWW/not_public/matches_1_300k_Dec14_2018.csv'
DEFAULT_REFEREE_ARCHIVE = HOME + \
    '/Dropbox/Documents/WWW/not_public/matches_1_300k_Dec14_2018_HAKEMLER.csv'
TEST_MATCH_ARCHIVE = HOME + \
    '/Dropbox/Research1/fun-experiments/TFF-data-handling/tests/sample_files/sample_matches_1000_1010.csv'
TEST_REFEREE_ARCHIVE = HOME + \
    '/Dropbox/Research1/fun-experiments/TFF-data-handling/tests/sample_files/sample_HAKEMLER.csv'

from .read_csv_into_df import read_matches
from .read_csv_into_df import read_referees
from .search_ref_archive import tff_hakem_id_to_name
from .search_ref_archive import tff_hakem_id_to_area
from .seasons import get_season_info
from .search_match_archive import leagues
