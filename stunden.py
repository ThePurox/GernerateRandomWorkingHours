import random
import time
import datetime
import locale
import platform
if platform.system() == "Linux":
    locale.setlocale(locale.LC_ALL, "de_DE.utf8") # Linux
if platform.system() == "Windows":
    locale.setlocale(locale.LC_ALL, "deu_deu") # windows

TOTALHOURS = 20
MONTH = 6
YEAR = 2018
POSSIBLETIMES = [8,22]
MINDIST = 12
MAXTIME = 6


def genPair(last, currentSum):
    # problem start time can be possibletimes[1]
    dt = datetime.timedelta( days = random.randint(0,7) , hours = random.randint( POSSIBLETIMES[0] - last.hour, POSSIBLETIMES[1] - last.hour))
    if dt.total_seconds()//3600 < MINDIST:
        dt += datetime.timedelta(days = random.randint(1,7))
    start = last + dt
    end = start + datetime.timedelta(hours = min(random.randint(1,MAXTIME) , POSSIBLETIMES[1] -start.hour,TOTALHOURS - currentSum))
    return [start , end]

def genfirst():
    MINDAY = 1
    if MONTH == 1:
        MINDAY = 7
    last = datetime.datetime(YEAR,MONTH,MINDAY + random.randint(0,7) ,random.randint(POSSIBLETIMES[0],POSSIBLETIMES[1]))
    return last

def isValid(times):
    if times[-1][1].month != MONTH:
        return False
    return True

def sumTimes(times):
    sum = datetime.timedelta(0)
    for [t1,t2] in times:
        sum += t2 - t1
    return sum.total_seconds()//3600

def printTimes(times):
    s = r"Datum & Anfangszeit & Endzeit & Arbeitsstunden\\" + "\n" +r"\hline" + "\n"
    for [t1,t2] in times:
        print(t1,t2)
        dt = t2 - t1
        s += t1.strftime("%x & %H:%M") + r" & " + t2.strftime("%H:%M") + r" & " + str(dt.total_seconds()//3600) + r"\\" + "\n"
    print(s)
    pre = times[1][1].strftime("%Y_%m_")
    file = open(pre + "tableData.tex", "w")
    file.write(s)
    file.close()



while(True):
    times = [genPair(genfirst(),0)]
    while( sumTimes(times) < TOTALHOURS):
        times.append(genPair(times[-1][1],sumTimes(times)))
    if isValid(times):
        printTimes(times)
        break


# def genPair(times):
#     start = random.randint((max(times[-1]+minDist)%24 , possibleTimes[0]),possibleTimes[1])
#     end = min(totalHours - start , random.randint(1 , maxTime))
# while(sumTime(times) < totalHours):
#     times.append(genPair(times))
