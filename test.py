import mercury
import time

rd = mercury.Reader("tmr:///dev/ttyUSB0", baudrate=115200)
rd.set_region("JP")
# アンテナは1
rd.set_read_plan([1], "GEN2", bank=["epc"])

# 例外のキャッチ，エラー表示
rd.enable_exception_handler(lambda e: print(e))

read_time = int(input("何秒間実行しますか？ >> "))

rd.start_reading(lambda tag: print(tag.epc))
time.sleep(read_time)
rd.stop_reading()


"""
def func1(func):
	func()

def greeting():
	print("hello")

func1(greeting)


def func1(func):
	func()

func1(lambda: print("hello"))


"""