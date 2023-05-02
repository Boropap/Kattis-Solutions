'''
Input
The input contains one line, which has two integers A
and B, separated by a single space. The bounds on these values are 0 <= a,b <= 1.000.000

Output
Output the smaller number first, and the larger number second.
'''
x, y = input().split()
x = int(x)
y = int(y)

if (x > y):
    print(y,x)
else:
    print(x,y)