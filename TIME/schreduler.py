import datetime
from datetime import timedelta
import time


print('oui')

test_schredule = datetime.datetime.now().replace(microsecond=0) + timedelta(seconds=10)
c =0

while c < 30:
    now = datetime.datetime.now().replace(microsecond=0)
    if now == test_schredule:
        print('c la fete')
        time.sleep(2)
    time.sleep(0.5)
    c+=1
    print(f'{now} vs {test_schredule}')


