import csv
import json

from pysocialwatcher import watcherAPI

if __name__ == '__main__':
	watcher = watcherAPI(api_version="12.0", sleep_time=8, outputname="dataframe_collected_finished_bogota_loc_dec.csv")
	watcher.load_credentials_file("credentials_sn.csv")
	df = watcher.run_data_collection("../Consultas JSON/bogota_localidades_expats_improved.json", remove_tmp_files=True)