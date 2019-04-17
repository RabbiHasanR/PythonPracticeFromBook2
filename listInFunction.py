def add_numbers(numbers):
   numbers[0]=10
   return numbers

numbers=[1,2,3,4,5]
print('Before function call',numbers)

print('After functionn call',add_numbers(numbers))
