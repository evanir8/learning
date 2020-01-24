import sys
import time
str = sys.argv[1] if len(sys.argv) > 1 else "Hello World Python"
starts = 0
ends  = len(str)
try:
    while True:
        sys.stdout.write("{0} {1}\r".format(str[starts:ends], str[0:starts]))
        sys.stdout.flush()
        starts += 1
        if starts > ends: starts = 0
        time.sleep(0.5)
except KeyboardInterrupt:
    print('interrupted!')
