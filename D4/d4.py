import re
import datetime
import sys
import itertools

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

top_sleeper=max(guard_sleep_total,key=guard_sleep_total.get) #Guardid that slept the most

selectors=[x == top_sleeper for x in guardid] #create Filter when the top_sleeper guard was on duty
top_sleeper_timetable=list(itertools.compress(timetable,selectors)) #fitler out the timetable only for the days the guard was on duty
totals_per_minute=map(sum,zip(*top_sleeper_timetable)) #sum the total minutes per column the guard was slept
top_minute=totals_per_minute.index(max(totals_per_minute)) #find the max

print("Result:",int(top_sleeper)*top_minute)

#for y in range(365):
#    sys.stdout.write(str(y))
#    sys.stdout.write(" ")
#    for x in range(60):
#        sys.stdout.write(str(timetable[y][x]))
#    print("")