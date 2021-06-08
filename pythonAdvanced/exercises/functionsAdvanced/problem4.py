nums = list(map(int, input().split(" ")))

positive_sum = sum(filter(lambda x: x > 0, nums))
negative_sum = sum(filter(lambda x: x < 0, nums))
print(negative_sum)
print(positive_sum)

if positive_sum > -negative_sum:
    print("The positives are stronger than the negatives")

else:
    print("The negatives are stronger than the positives")

