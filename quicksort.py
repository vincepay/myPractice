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
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

#------------------------------------------
ANALYSIS OF QUICKSORT:
    Time taken by QuickSort in general can be written as following.

      T(n) = T(k) + T(n-k-1) + \theta(n)
    The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements which are smaller than pivot.
    The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

    Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot. If we consider above partition strategy where last element is always picked as pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for worst case.

        T(n) = T(0) + T(n-1) + \theta(n)
      which is equivalent to   
        T(n) = T(n-1) + \theta(n)
      The solution of above recurrence is \theta(n2).

    Best Case: The best case occurs when the partition process always picks the middle element as pivot. Following is recurrence for best case.

      T(n) = 2T(n/2) + \theta(n)
      The solution of above recurrence is \theta(nLogn). It can be solved using case 2 of Master Theorem.

    Average Case:
      To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn’t look easy.
      We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.

        T(n) = T(n/9) + T(9n/10) + \theta(n)
      Solution of above recurrence is also O(nLogn)

    Although the worst case time complexity of QuickSort is O(n2) which is more than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice, because its inner loop can be efficiently implemented on most architectures, and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stored in external storage.



'''
import numpy.random as random

# a = [2,8,7, 1,3,5,6,4]
a = [-3,6,8,2,0,2,1,-1]
# a=[9]
# a = random.randint(0,100,size=1000)


def partition(a):
  if len(a)==1:
    return a

  i=0
  j=0
  pivot = a[-1]
  for j in range(0,len(a)-1):
    if a[j] < pivot:
      a[i],a[j] = a[j], a[i]
      i = i + 1

  # replace the pivot with whatever is at position i 
  a[i],a[-1] = pivot,a[i]

  if i != 0: 
    a[0:i] = partition(a[0:i])
  if i+1 != len(a):
    a[i+1:] = partition(a[i+1:])
  return a

b = partition(a)
print(b)

