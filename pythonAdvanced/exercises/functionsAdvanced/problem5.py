command = input()

nums = list(map(int, input().split(" ")))

print(sum(filter(lambda x: x%2 == (0 if command == "Even" else 1), nums))*len(nums))
