# Slicing: extract a sub-list using [start:stop:step]
# stop is exclusive

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])    # [2, 3, 4]
print(nums[:4])     # [0, 1, 2, 3]
print(nums[6:])     # [6, 7, 8, 9]
print(nums[::2])    # [0, 2, 4, 6, 8] — every other
print(nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] — reversed
print(nums[1:8:3])  # [1, 4, 7]
