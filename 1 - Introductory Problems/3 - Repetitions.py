# Solution of cses.fi problem https://cses.fi/problemset/task/1069 by NiveditJain
# this is only meant to be used for educational purpose and used in 
# DSA Course by Nivedit Jain, here: https://www.linkedin.com/posts/nivedit-jain_on-the-auspecious-occasion-of-dussehra-i-activity-7122587967113621504-0stf

# accepting input and typecasting it to int
string = input()

last = 'Z'
# CONCEPT: Storage of last
count = 0
max_count = 0

for character in string:
    if character == last:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 1
        last = character

print(max(max_count, count))
