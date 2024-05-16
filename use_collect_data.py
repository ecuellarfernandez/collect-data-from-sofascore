#using collect_fata_... method
#parameter url, season

from functions.collect_data_from_all_rounds_of_a_season import collect_data_from_all_rounds_of_a_season

url_base = "https://www.sofascore.com/api/v1/unique-tournament/8/season/24127/events/round/"
csv_destination = "results_rounds/19_20/rounds"

collect_data_from_all_rounds_of_a_season(url_base, csv_destination)