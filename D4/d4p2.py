import re
import datetime
import sys
import itertools
from operator import itemgetter

with open("/home/user/Devel/adventofcode2018/D4/input.txt") as f:
    records = f.readlines()

def sortdate(elem):
    return datetime.datetime.strptime(elem[1:17],"%Y-%m-%d %H:%M") #chop off the non-time string content for date comparison
records.sort(key=sortdate)

guardid=[None for x in range(365)]
uniqueguardids=set()
guard_sleep_total={}

sleep_start=None
sleep_end=None

w,h=60,365 #60 minutes, by year days
timetable=[[0 for x in range(w)] for y in range(h)] #initialize canvas to 0

for record in records:
    match=re.search(r"\[.*\] Guard #(\d+) begins shift",record) #parse string
    if match is None:
        match=re.search(r"\[\d+\-(\d+\-\d+) \d+:(\d+)\] falls asleep",record) #parse string
        if match is None:
            match=re.search(r"\[\d+\-(\d+\-\d+) \d+:(\d+)\] wakes up",record) #parse string
            if match is None:
                print("Parse error format")
            else:
                sleep_end=int(match.group(2)) #save sleep_end minute and day
                day_end=datetime.datetime.strptime(match.group(1),"%m-%d").timetuple().tm_yday
        else:
            sleep_start=int(match.group(2)) #save sleep_start minute and day
            day_start=datetime.datetime.strptime(match.group(1),"%m-%d").timetuple().tm_yday
    else:
        currentguard=match.group(1) #Guard starts shift, record guardid
    if sleep_end is not None and sleep_start is not None:
        if day_start!=day_end:
            print("Parse error dates")
        else:
            for x in range(sleep_start,sleep_end):
                timetable[day_start][x]=1
            guardid[day_start]=currentguard # save the guardid for the current day
            uniqueguardids.add(currentguard) # add guardid to set (only uniques get added)
            if currentguard in guard_sleep_total:
                guard_sleep_total[currentguard]+=(sleep_end-sleep_start)+1 #add time slept to current total
            else:
                guard_sleep_total[currentguard]=(sleep_end-sleep_start)+1 #first sleep time
            sleep_start=None
            sleep_end=None

result_matrix={}
top_minute_per_guard={}
for guard in uniqueguardids:
    selector=[x == guard for x in guardid]
    guard_timetable=list(itertools.compress(timetable,selector))
    totals_per_minute=map(sum,zip(*guard_timetable))
    result_matrix[guard]=totals_per_minute

for item in result_matrix:
    minutes=result_matrix[item]
    top_minute=minutes.index(max(minutes))
    top_minute_per_guard[item]=top_minute,max(minutes)

max=0
max_min=0
g_max=0
for item in top_minute_per_guard:
    if top_minute_per_guard[item][1]>max:
        max=top_minute_per_guard[item][1]
        max_min=top_minute_per_guard[item][0]
        g_max=item

print("Result:",int(g_max)*max_min)