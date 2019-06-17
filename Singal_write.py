import serial


ser = serial.Serial('COM3', 115200, timeout=1)
# 实例化串口
i = 0
while True:
    i += 1
    print(i)
    ser.close()
    ser.open()
    re = ser.readlines()
    # 无标签拿起
    if len(re) == 2:
        file = open("rfid.txt", 'w')
        file.write("default")
        file.close()
        print("default")
    else:
        data = []
        for string in re:
            if "ID" in repr(string):
                temp = repr(string).split(':')[1][:-5]
                if temp not in data:
                    data.append(temp)
        # 多标签拿起
        if len(data) > 1 or len(data) == 0:
            file = open("rfid.txt", 'w')
            file.write("default")
            file.close()
            print("default")
        # 单标签拿起
        else:
            file = open("rfid.txt", 'w')
            file.write(data[0])
            file.close()
            print(data)
