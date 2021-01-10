from datetime import datetime
import time

tic = datetime.now()
time.sleep(5)
toc = datetime.now()
delta = toc-tic
print(delta.seconds)