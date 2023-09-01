import time
import psutil

f = None
try:
    f = open("time_tracker.txt", "r+")
except:
    print("Initializing and creating a new file to write to with time: 0 hours")
    f = open("time_tracker.txt", "x")
    f.write("0")
    f = open("time_tracker.txt", "r+")
    
original_time = int(f.readline())
open("time_tracker.txt", "w")
start_time = 0  
has_been_accessed = 0
while True:

    time.sleep(.5)
    if ("League of Legends.exe" in (i.name() for i in psutil.process_iter())):
        if (has_been_accessed == 0):
            start_time = time.time()
            print("i got here!!")
            print(start_time)
            has_been_accessed = 1
    else:
        if (start_time != 0):
            print("Im here")
            end_time = time.time()
            start_time = start_time / 60 / 60
            end_time = end_time / 60 / 60
            actual_time = start_time - end_time
            original_time = original_time + actual_time
            f.write(str(original_time))
            start_time = 0
            has_been_accessed = 0