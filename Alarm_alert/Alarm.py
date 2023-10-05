import datetime
from playsound import playsound

alarm_time = input("Enter the time of alar11m to be set:HH:MM:SS am/pm\n")
alarm_hour = (alarm_time[0:2])
alarm_minute = (alarm_time[3:5])
alarm_sec = (alarm_time[6:8])
alarm_period = alarm_time[9:11]
print(alarm_time,alarm_period,alarm_sec,alarm_minute)

print("ALarm set!")
if alarm_period =="pm" and alarm_hour != 12:
    alarm_hour = int(alarm_hour) + 12
    print("run")

alarm_minute = int(alarm_minute)
alarm_sec = int(alarm_sec)

while True:
    if(alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute  
    and alarm_sec == datetime.datetime.now().second):
        print("wake up!")
        playsound('mixkit-morning-birds-singing-2467.wav')
        break