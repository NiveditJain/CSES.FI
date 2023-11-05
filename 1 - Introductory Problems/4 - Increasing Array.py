# Solution of cses.fi problem https://cses.fi/problemset/task/1094 by NiveditJain
# this is only meant to be used for educational purpose and used in 
# DSA Course by Nivedit Jain, here: https://www.linkedin.com/posts/nivedit-jain_on-the-auspecious-occasion-of-dussehra-i-activity-7122587967113621504-0stf

# accepting input and typecasting it to int
n = int(input())
numbers = list(map(int, input().split()))

increments = 0
last_minimum = numbers[0]

for number in numbers[1:]:
    if number < last_minimum:
        increments += last_minimum - number
    else:
        last_minimum = number

print(increments)
