# input = [5, 10, 15, 20, 25]
# print(input[4])
# or
# input = [5, 10, 15, 20, 25]
# print(max(input))


listOfNumbers = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input())
    listOfNumbers.append(numbers)
print("Output", sum(listOfNumbers))