# List methods: built-in functions to modify and query lists

nums = [3, 1, 4, 1, 5, 9, 2]

nums.append(6)          # add to end
nums.insert(0, 0)       # insert at index
nums.remove(1)          # remove first occurrence of value
popped = nums.pop()     # remove and return last item
nums.sort()             # sort in-place
print(nums)

nums.reverse()          # reverse in-place
print(nums)

print(nums.index(4))    # find index of value
print(nums.count(1))    # count occurrences
nums.clear()            # remove all items
print(nums)             # []
