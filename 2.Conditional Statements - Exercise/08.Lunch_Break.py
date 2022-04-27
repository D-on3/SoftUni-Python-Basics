import math
#Име на сериал – текст
name_of_show = input()
#Продължителност на епизод  – цяло число в диапазона [10… 90]
duration_of_episode = int(input())
#Продължителност на почивката  – цяло число в диапазона [10… 120]
duration_of_brake = int(input())

time_for_spend = duration_of_brake -((duration_of_brake * 0.125)+(duration_of_brake* 0.25))
#time_episode = time_for_spend // duration_of_episode

if time_for_spend >= duration_of_episode:
    left_time = int(time_for_spend - duration_of_episode)
    print(f"You have enough time to watch {name_of_show} and left with {left_time} minutes free time.")
elif time_for_spend < duration_of_episode:
    need = duration_of_episode - time_for_spend
    need1 = math.ceil(need)
    print(f"You don't have enough time to watch {name_of_show}, you need {need1} more minutes.")
