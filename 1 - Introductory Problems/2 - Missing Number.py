# Solution of cses.fi problem https://cses.fi/problemset/task/1068 by NiveditJain
# this is only meant to be used for educational purpose and used in 
# DSA Course by Nivedit Jain, here: https://www.linkedin.com/posts/nivedit-jain_on-the-auspecious-occasion-of-dussehra-i-activity-7122587967113621504-0stf

# accepting input and typecasting it to int
n = int(input())
# CONCEPT: map function
numbers = list(map(int, input().split()))

# CONCEPT: XOR of 00,01,10,11 is 0
# CONCEPT: XOR is commutative
# CONCEPT: XOR is associative
# CONCEPT: XOR of a number with itself is 0
# CONCEPT: XOR of a number with 0 is the number itself
# CONCEPT: Dark or Shadow Numbers/Data
xor = 0
for number in numbers:
    xor ^= number

extension = 3 - n % 4

for number in range(n + 1, n + extension + 1):
    xor ^= number

print(xor)
