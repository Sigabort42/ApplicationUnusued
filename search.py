#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time

from datetime import datetime, timedelta


if (len(sys.argv) < 2):
    print("usage: {} number_of_days".format(sys.argv[0]))
    exit()

listOfFiles = os.listdir('/Applications')
tab_date = []
req = requests.Session()
for file in listOfFiles:
    tab_date.append((
        "/Applications/" + file,
        time.ctime(os.path.getmtime("/Applications/" + file)),
        os.path.getmtime("/Applications/" + file)
    ))
    
d = datetime.now() - timedelta(days=int(sys.argv[1]), hours=0, minutes=0, seconds=0)
dt = datetime.timestamp(d)

print("Les applications non utilisé depuis le {} sont:".format(d))
for date in tab_date:
    if (date[2] > dt):
        print("\033[31m-------------------------------------------------------------------------> {}\033[00m".format(date[0]))
