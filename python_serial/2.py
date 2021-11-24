import serial  # pyserial
import threading
import time
DATA = ""  # 读取的数据
NOEND = True  # 是否读取结束


def read_data(ser):
    global DATA, NOEND

    # 循环接收数据（此为死循环，可用线程实现）
    while NOEND:
        if ser.in_waiting:
            DATA = ser.read(ser.in_waiting).decode("gbk")
            print("\n>> receive: ", DATA, "\n>>", end="")
            # print(">>", end="")
            if(DATA == "quit"):
                print("oppo seri has closen.\n>>", end="")


# 打开串口
def open_seri(portx, bps, timeout):
    ret = False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)

        # 判断是否成功打开
        if(ser.is_open):
            ret = True
            th = threading.Thread(
                target=read_data, args=(ser,))  # 创建一个子线程去等待读数据
            th.start()
    except Exception as e:
        print("error!", e)

    return ser, ret


# 关闭串口
def close_seri(ser):
    global NOEND
    NOEND = False
    ser.close()

# 写数据


def write_to_seri(ser, text):
    res = ser.write(text)  # 写
    return res

# 读数据


def read_from_seri():
    global DATA
    data = DATA
    DATA = ""  # 清空当次读取
    return data


if __name__ == "__main__":

    # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
    portx = "COM10"

    # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
    bps = 19200

    # 超时设置，None：永远等待操作；
    #         0：立即返回请求结果；
    #        其他：等待超时时间（单位为秒）
    timex = 5

    # 打开串口，并得到串口对象
    ser, ret = open_seri(portx, bps, timex)

    # 写数据
    data = b'\x00\x66'
    # 0.5v
    result = write_to_seri(ser, data)
    print("写总字节数：", result)

    data = b'\x00\xcc'
    # 1v
    result = write_to_seri(ser, data)
    print("写总字节数：", result)

    ser.close()  # 关闭串口
    # 100*100/s
