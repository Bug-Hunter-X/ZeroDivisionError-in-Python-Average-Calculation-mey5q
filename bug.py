def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) #this will return 0
print(f"The average of an empty list is: {average_empty}")

#Example of a ZeroDivisionError
my_list = []
#average_error = calculate_average(my_list)
#print(f"The average is: {average_error}") #this will raise ZeroDivisionError