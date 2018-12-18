# FROM: dailycodingproblem.com
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
# I: Question: do we need to know which combination of element pairs sum to the given number? Not requiring it, would it make it easier?
# I: Generalization:  what if any number of array elements could sum to our given number?  so give 10,  and [1 2 3 4 5 6 7 8 9]  we would see 1+9 and 2+8 ... are the 

# a = [10, 15, 3, 7]
# n = 17
puts 'Enter a list of integers, separated by space:'
a = gets.strip.split.map { |n| n.to_i }
puts 'Enter a number for the sum?'
k = gets.strip.to_i

# ----- Naive solution -------
# a.each_with_index do |x, i|
#   y = n - x
#   if (a.include? y)
#     puts('Yes')
#     exit
#   end
# end
# puts('No')

# Solution:
# Lets assume the array is sorted (which can be achieved in nln time at best)
# 

# k=7
# a = [1,2,5,7,0,9]
a.sort!
leftIdx = 0
rightIdx = a.length - 1
pairs = []
while (rightIdx > leftIdx)
  s = a[leftIdx] + a[rightIdx]
  if (s == k)
    pairs.append([leftIdx,rightIdx])
    rightIdx -= 1
  elsif (s > k)
    rightIdx -= 1
  else
    leftIdx += 1
  end
end

if !pairs.empty?
  puts "Found pairs whose sum are #{k}:"
  puts pairs.to_s
  puts pairs.length
  for x in pairs
    puts "(#{a[x[0]]}, #{a[x[1]]}) @ indeces (#{x[0]}, #{x[1]})" 
  end
else
  puts "No paris with sum of #{k} was found"
end

