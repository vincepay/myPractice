# FROM: Email: Daily coding Problem #2
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the
# original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
# expected output would be [2, 3, 6].
# Follow-up: what if you can't use division

# [1,2,3] --> [6,3,2]
# [1,2,3,4] --->  [ 2*3*4,  1*3*4,  1*2*4,  1*2*4]

#
# For array 'a' of size 100, counter1=298,  counter2=10000,  counter3=9900  ==>   counter3 = 33.2 * counter1 !!!!
#      By timing the methods, time2 = 43.6  * time1 !!!
# For array of size 1000,   time2 = 228.7 * time1 !!!
# For array of size 10000,  time 2 = 374.5 * time1

import time
import math

# a = list(range(1,6))
a = list (range(1,10000))
l = [1] * len(a)
r = l[:]
p1 = l[:]    # to ensure an actual copy w/ different id
p2 = l[:]
p3 = l[:]
p4 = l[:]

# Trivial method:
start = time.time()
# counter2 = 0
# counter3 = 0
for i in range(len(a)):
    for j in range(len(a)):
        # counter2 += 1
        if i!=j:
            # counter3 += 1
            p1[i] = p1[i] * a[j]
time1 = time.time() - start

#--------------------------------------------------
# NON-trivial method 1:
# INSPIRED FROM: https://www.geeksforgeeks.org/a-product-array-puzzle/
# time complexity: O(3N) = O(N)
# space complexity:  O(N)          I think this refers to the final product array
# Auxilliary space: O(2*N) = O(N)  I think this refers to the space for left and right arrays

# counter1 = 0
start=time.time()
for i in range(1,len(a)):
    # counter1 += 1
    l[i] = l[i-1] * a[i-1]

for i in range(len(a)-2,-1,-1):
    # counter1 += 1
    r[i] = r[i+1] * a[i+1]

for i in range(len(a)):
    # counter1 += 1
    p2[i] = l[i] * r[i]

time2 = time.time() - start



#--------------------------------------------------
# NON-trivial method 2:
# time complexity: O(2N) = O(N)
# auxillary space complexity: O(1)
#
# The problem with the above solution is bad space complexity. Besides the product array, we had to create 2 extra arrays and thats not
# cool! So another way, is to create the left and right arrays right ON the product array. There is however a little catch: we can go
# through the array and create the left array fine, but trying to create the right array while going through the 'a' , we still need a
# temp variable to keep the multiplication of all the right-side elements, thus O(1)

# starting from 2nd element all the way to last:
start = time.time()

for i in range(1, len(a)):
    p3[i] = p3[i-1] * a[i-1]
# starting from 2nd from last all the way to first:
tmp=1
for i in range(len(a)-2,-1,-1):
    tmp = tmp * a[i+1]
    p3[i] = p3[i] * tmp

time3 = time.time() - start


#--------------------------------------------------
# NON-trivial method 2:
# INSPIRED FROM: https://www.geeksforgeeks.org/product-array-puzzle-set-2-o1-space/
# This method doesnt work well with large array, cuz I get 'Numerical result out of range' error!
# lets say the product of ALL elements is 'P', and 'p' is the array we want to find. Thus p[k] = P/a[k]
# We cant use division, thus we resort to logarithmic approach, converting divisions and multiplicatsions to subtraction and sums:
# log(p[k]) = log(P) - log(a[k])  ==> p[k] = 10 ** (log(P) - log(a[k])  ==   10 ** (  (log(a[1]) + log(a[2]) +...)  - log(a[k]) )

start = time.time()

# P = 1
#
# # epsilon value to maintain precision
# EPS = 1e-9
#
# for i in range(len(a)):
#     P *= a[i]
#
# P_log = math.log10(P)   # to avoid calculating this everytime in the power of 10 below
#
# for i in range(len(a)):
#     # # p4[i] = 10 ** ( P_log - math.log10(a[i]))               # ---> precision error
#     p4[i] = int(EPS + 10 ** ( P_log - math.log10(a[i])))        # ---> A tiny bit faster than the alternative below
#     # p4[i] = round(10 ** ( P_log - math.log10(a[i])))

time4 = time.time() - start

#=================================================
print('-'*20)
print('p1 = ', p1)
print('p2 = ', p2)
print('p3 = ', p3)
print('p4 = ', p4)

# print(counter1)
# print(counter2)
# print(counter3)
# print(counter3/counter1)  # --> 33.2
print('time1 = ', time1)
print('time2 = ', time2)
print('time3 = ', time3)
print('time4 = ', time4)
#   - - - - - - - - - - - - - - - - - - - - - N=5 ,     N=10    N=100     N=1000   N=10,000
print('time1/time2 = ', time1/time2)  # -->  1.66       3       29        30         43!!
print('time1/time3 = ', time1/time3)  # -->  2.68       4.28    44        31
print('time1/time4 = ', time1/time4)  # -->  0.35!!!    0.89    23        --
print()
print('time2/time3 = ', time2/time3)  # -->   1.7      1.43     1.5       1.006
print('time4/time3 = ', time4/time3)  # -->   8        4.48     1.8


