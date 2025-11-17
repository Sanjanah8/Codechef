"""
Alice, Bob, and Charlie are contributing to buy a Netflix subscription. However, Netfix allows only two users to share a subscription.
Given that Alice, Bob, and Charlie have A,B, and C rupees respectively and a Netflix subscription costs 
X rupees, find whether any two of them can contribute to buy a subscription.
"""
t=int(input())
for i in range(t):
    a,b,c,x=map(int,input().split())
    if a+b>=x or a+c>=x or b+c>=x:
        print("YES")
    else:
        print("NO")
