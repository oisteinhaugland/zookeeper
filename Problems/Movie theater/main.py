num_halls = int(input())
hall_capacity = int(input())
num_viewers = int(input())

total_capacity = num_halls * hall_capacity
print(total_capacity >= num_viewers)
