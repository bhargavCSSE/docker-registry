import sys
from time import sleep

count = 0

while(True):
    print("Heartbeat: ", count)
    count += 1
    sleep(1)