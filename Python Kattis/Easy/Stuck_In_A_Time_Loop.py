'''
Input
Input consists of a single integer N (1 <= N <= 100).

Output
Output the entire wizard’s spell by counting from 
to N, giving one number and “Abracadabra” per line.
'''
x = int(input())
y = 1
while (x >= y):
    print("{} Abracadabra".format(y))
    y += 1
