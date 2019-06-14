# python

# import csv

# filename = r"D:\Study\scala\trigger_video_with_RFID\rfid.csv";

# temp = []
# with open(filename, "r") as f:
# 	reader = csv.reader(f, quoting=csv.QUOTE_NONE)
# 	for i in reader:
# 		temp.append(i[0])

# item = tuple(temp)
# print(item)
# print(temp)




# scala

import csv
import scalalib as sl
import scalatools as st

# filename = r"D:\Study\scala\trigger_video_with_RFID\rfid.csv";

scala5 = True
log = sl.get_logger(scala=1, level='error')
svars = sl.sharedvars()

# filename = svars.signal_file
# filename = r"C:\Users\yfc\Desktop\test0529\rfid.csv"
temp = []
with open(filename.Value, "r") as f:
	reader = csv.reader(f, quoting=csv.QUOTE_NONE)
	for i in reader:
		temp.append(i[0])

item.Value = tuple(temp)
