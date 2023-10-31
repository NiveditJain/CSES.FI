# Solution of cses.fi problem https://cses.fi/problemset/task/1068 by NiveditJain
# this is only meant to be used for educational purpose and used in 
# DSA Course by Nivedit Jain, here: https://www.linkedin.com/posts/nivedit-jain_on-the-auspecious-occasion-of-dussehra-i-activity-7122587967113621504-0stf

# accepting input and typecasting it to int
n = int(input())


# function to check if the number is even or odd
# CONCEPT: code reusability and readability
def is_even(number):
    return number % 2 == 0


# function to perform the weird algorithm
# think like state, you are somewhere and 
# need to go to next, based on a rule 
# you will decide where to go next
# CONCEPT: recursion
# CONCEPT: think like a state machine
def calculate(number):

    print(number, end=" ")

    # base case
    # if number is 1 then return
    # CONCEPT: base case
    # CONCEPT: termination condition
    if number == 1:
        return

    # if number is even then divide it by 2
    if is_even(number):
        calculate(number // 2)

    # if number is odd then multiply it by 3 and add 1
    else:
        calculate(number * 3 + 1)


calculate(n)
