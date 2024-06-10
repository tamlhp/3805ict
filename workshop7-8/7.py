"""
To demonstrate the solution to the recurrence relation
T(u)=T(sqrt(u))+O(1) is T(u)=lglgu, let's proceed through the steps methodically, avoiding any redundancy.

Step 1: Understanding the Recurrence
The given recurrence relation tells us that solving a problem of size u requires solving a smaller problem of size sqrt(u), 
plus a constant amount of additional work O(1).

Step 2: Iterative Expansion
We repeatedly apply the recurrence:

First application: T(u)=T(sqrt(u))+O(1)
Second application: T(u)=T(u^(1/4))+2*O(1)
After k applications: T(u)=T(u^(1/2^k))+k*O(1)

Step 3: Reaching the Base Case
We look for the number of applications k after which the argument of T, u^(1/2^k), becomes constant. We consider 
2 as a practical base case for simplification, leading to:
u^(1/2^k)=2

Taking logarithms on both sides gives us:

1/2^k*logu=log2

Since log2=1 in base 2, we simplify to:
2^k =logu

Taking logarithms again:
k=log(logu)

Step 4: Solution Interpretation
The number of steps k required to reduce the problem size to a constant is proportional to
log(logu). Since each step adds a constant time complexity, the total time complexity is:

T(u)=k⋅O(1)=log(logu)⋅O(1)

Given that multiplication by a constant does not change the asymptotic behavior, we conclude:
T(u)=O(loglogu)
"""