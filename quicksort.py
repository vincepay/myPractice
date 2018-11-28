'''
FROM: https://www.quora.com/What-is-an-intuitive-explanation-of-QuickSort
I liked th explanation and the visuals above. 
For more thorough understanding of all variations of pivor sort, consider all variations as explained in:
FROM: https://www.quora.com/How-do-I-analyse-a-Quicksort-algorithm-in-depth
Record, analyze and graph performance on datasets of varying size created using heuristics such as ascending, descending, monotonic, QuickSort Adversary, Median of 3 Adversary, few unique and any other arrangements imaginable (there are many). To be truly in-depth, examine and test many different algorithms of the Quick family of sorts, including deterministic pivot, randomized pivot, Yaroslavsky dual-pivot, triple pivot, median of 3, median of 9, iterative, recursive and even hybrids like IntroSort, among many other variants you will never find in textbooks. This will then be among what I'd consider pretty well in-depth. Done correctly, this should keep your computer and you busy for some time to come.

Write implementation for :
  choice of pivot: 
    mdeterministic pivot
    randomized pivot
    Yaroslavsky dual-pivot
    triple pivot
    median of 3
    media of 9
    
  iterative
  recursive
  hybrids:
    IntroSort



More inspiration at:
FROM: https://www.geeksforgeeks.org/quick-sort/

'''
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

