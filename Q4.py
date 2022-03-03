# input = [5, 10, 15, 20, 25]
# print(input[4])
# or
# input = [5, 10, 15, 20, 25]
# print(max(input))


listOfNumbers = []
for n in range(5):
    numbers = int(input())
    listOfNumbers.append(numbers)
print("Output", sum(listOfNumbers))