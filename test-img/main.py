import sys
from time import sleep

count = 0

while(True):
    print("Heartbeat: ", count, file=sys.stderr)
    count += 1
    sleep(1)
