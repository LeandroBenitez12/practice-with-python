### Dates ###

# Modules
from datetime import datetime# Nos trae la fecha, hora, tiempo
import time

for i in range(0,61):
    now = datetime.now()
    print(f' La hora es : {now.hour} : {now.minute} : {now.second}')
    time.sleep(1)