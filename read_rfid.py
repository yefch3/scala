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

# import csv
# import scalalib as sl
# import scalatools as st

# # filename = r"D:\Study\scala\trigger_video_with_RFID\rfid.csv";

# scala5 = True
# log = sl.get_logger(scala=1, level='error')
# svars = sl.sharedvars()

# # filename = svars.signal_file
# # filename = r"C:\Users\yfc\Desktop\test0529\rfid.csv"
# temp = []
# with open(filename.Value, "r") as f:
# 	reader = csv.reader(f, quoting=csv.QUOTE_NONE)
# 	for i in reader:
# 		temp.append(i[0])

# item.Value = tuple(temp)





# txt
import os
import time

while 1:
	file_object = open(filename.Value)  
	try:  
			item.Value= file_object.read()  
	finally:  
			file_object.close()   
	time.sleep(1.0)






# csv
# import csv
# import time

# while 1:
# 	with open(filename.Value, "r") as f:
# 		reader = csv.reader(f)
# 		for i in reader:
# 			item.Value = i[0]

# 	time.sleep(2.0)