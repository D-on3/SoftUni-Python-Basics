goal = 10000
total_steps = 0
is_reached_the_goal = False
while total_steps <= goal:
    steps_walked = input()
    if steps_walked != 'Going home':
        steps_walked_conv = int(steps_walked)
        total_steps += steps_walked_conv
    elif steps_walked == 'Going home':
        steps_walked_conv = int(input())
        total_steps += steps_walked_conv
        is_reached_the_goal = True
        break
if goal <= total_steps:
    difference = abs(goal - total_steps)
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")

elif goal >= total_steps:
    differenc = abs(goal - total_steps)
    print(f"{differenc} more steps to reach goal.")
