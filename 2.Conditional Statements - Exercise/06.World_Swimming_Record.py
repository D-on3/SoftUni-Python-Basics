#Рекордът в секунди – реално число;
record_sec = float(input())
#Разстоянието в метри – реално число;
distance_meters = float(input())
#Времето в секунди, за което плува разстояние от 1 м. - реално число.
time_in_sec = float(input())
#съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
time_swimmin = distance_meters * time_in_sec
resistance  = (distance_meters // 15. ) * 12.5
time_swimming = time_swimmin + resistance
if time_swimming < record_sec:
    print(f" Yes, he succeeded! The new world record is {time_swimming:.2f} seconds.")
elif time_swimming > record_sec:
    seconds = abs(record_sec - time_swimming)
    print(f'No, he failed! He was {seconds:.2f} seconds slower.')