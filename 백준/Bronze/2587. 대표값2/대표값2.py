nums = []
for _ in range(5):
    nums.append(int(input()))
nums.sort()
avg = sum(nums) / 5
mid = nums[2]
print(int(avg))
print(mid)

