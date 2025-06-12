def sum_1(*args):
    negative = 0
    positive = 0

    for n in args:
        if n > 0:
            positive += n
        else:
            negative += n

    return negative, positive


numbers = [int(x) for x in input().split()]

print(sum_1(*numbers)[0])
print(sum_1(*numbers)[1])
if abs(sum_1(*numbers)[0])> sum_1(*numbers)[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
