"""扫描标签的时候直接读取字符串传入scala，如果在5秒内读取到的字符串是和原来一样的，不重新播放，如果5秒后或者扫瞄到了其他的标签，立即更新播放"""

from time import time
import serial

ser = serial.Serial('COM4', 115200, timeout=None)
ser.close()
ser.open()
data = ser.read(39)
cur_time = time()
cur = repr(data)[17:-1]
print(cur)
# item.Value = tuple(cur)

# for i in range(30):
#     ser.close()
#     ser.open()
#     data = ser.read(39)
#     pre_time = time()
#     pre = repr(data)[17:-1]
#     if pre == cur and (pre_time - cur_time) <= 5:


    # with open('data.txt','a') as f:
    #     f.add(current)
    # print(type(current))