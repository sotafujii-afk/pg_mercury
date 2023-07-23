import mercury
reader = mercury.Reader("tmr:///dev/ttyUSB0", baudrate = 115200)

reader.set_region("JP")
reader.set_read_plan([1], "GEN2")
print(reader.read(10000))