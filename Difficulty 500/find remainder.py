"""
Find Remainder
Write a program to find the remainder when an integer A is divided by an integer B.
The first line contains an integer T, the total number of test cases. Then T lines follow, each line contains two Integers A and B.
"""
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(a%b)
