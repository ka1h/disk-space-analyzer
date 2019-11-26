import os
import numpy
import csv

def get_size_dirs(start_path):
	total_size_list = []
	total_size = 0
	total_len = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size_list.append(os.path.getsize(fp)/1000000)
			# skip if it is symbolic link
			if not os.path.islink(fp):
				total_size += os.path.getsize(fp)
				total_len += 1
	return round(total_size/1000000, 2), round(numpy.mean(total_size_list), 2), round(numpy.median(total_size_list), 2), round(numpy.quantile(total_size_list, 0.25), 2), round(numpy.quantile(total_size_list, 0.75), 2)

def get_fp_size(start_path):
	total_size_list = []
	total_size = 0
	total_len = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			
			# skip if it is symbolic link
			if not os.path.islink(fp):
				total_size += os.path.getsize(fp)
				total_len += 1
				total_size_list.append(os.path.getsize(fp)/1000000)
	return [round(total_size/1000000, 2), round(numpy.mean(total_size_list), 2), round(numpy.median(total_size_list), 2), round(numpy.quantile(total_size_list, 0.25), 2), round(numpy.quantile(total_size_list, 0.75), 2)]

with open('stats.csv', mode='w', newline='', encoding='utf-8') as csv_file:
	writer = csv.writer(csv_file, delimiter=';')
	writer.writerow(['Fach', 'Gesamtgröße (MB)', 'Durchschnittsgröße (MB)', 'Median (MB)', 'Unteres Quartil (25%)', 'Oberes Quartil (75%)'])
	writer.writerow(get_fp_size('YOUR_FILEPATH'))
