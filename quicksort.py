import numpy.random as random

# a = [2,8,7, 1,3,5,6,4]
# a = [-3,6,8,2,0,2,1,-1]
# a=[9]
a = random.randint(0,100,size=1000)


def partition(a):
  # print(a)
  # print(len(a))
  if len(a)==1:
    return a
    # print(len(a))

  i=0
  j=0
  pivot = a[-1]
  for j in range(0,len(a)-1):
    if a[j] < pivot:
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
      i = i + 1

  # replace the pivot with whatever is at position i 
  tmp= a[i]
  a[i] = pivot
  a[-1] = tmp
  # print('i=',i, 'a before recurse', a[0:i])
  if i != 0: 
    a[0:i] = partition(a[0:i])
  if i+1 != len(a):
    a[i+1:] = partition(a[i+1:])
  return a

b = partition(a)
print(b)

