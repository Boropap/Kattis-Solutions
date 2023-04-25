'''
Given two positive integers, determine whether the first one is larger than the second one.

Input
The single line of input contains two positive integers,a and b (0 < a, b <= 10^9).

Output
Output a single line with 1 if a > b, 0 otherwise.
'''
a, b = input().split()

if(a > b):
    print("1")
else:
    print("0")
