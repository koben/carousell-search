import processing
import time
from myconfigurations import ITEMS, PAUSE_INTERVAL

if __name__ == "__main__":
    while True:
        try:
            for i in ITEMS:
                processing.find_stuff(i)
        except KeyboardInterrupt:
            print ("Interrupt")
            sys.exit(1)
        time.sleep(PAUSE_INTERVAL)
