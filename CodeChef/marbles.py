#!/usr/bin/python
'''

* Link: https://www.codechef.com/problems/MARBLES
* Author: Shubham Kumar
* Type: Medium
* Concept: Begger's method of permutation and combination

'''
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)
def ncr(n,r):
    p = 1
    k = 1
    if (n - r < r): 
        r = n - r 
    if (r != 0):  
        while (r): 
            p *= n 
            k *= r 
            m = gcd(p, k) 
            p //= m 
            k //= m 
            n -= 1
            r -= 1
    else: 
        p = 1
    return p
for z in xrange(input()):
    n,r = map(int,raw_input().split())
    print ncr(n-1,r-1)
