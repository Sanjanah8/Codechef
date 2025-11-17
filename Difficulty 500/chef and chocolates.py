"""Chef and Chocolates
Chef wants to gift C chocolates to Botswal on his birthday. However, he has only X chocolates with him.
The cost of 1 chocolate is Y rupees.
Find the minimum money in rupees Chef needs to spend so that he can gift C chocolates to Botswal.
"""
t=int(input())
for i in range(t):
    c,x,y=map(int,input().split())
    print((c-x)*y)
