import datetime as dt, time
def funct():
    for i in range(5):
        currentTime = dt.datetime.now()
        print(currentTime.strftime("%H:%M:%S"))
        time.sleep(1)
if __name__ == '__main__':
    funct()