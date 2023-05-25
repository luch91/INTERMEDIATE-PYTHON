with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

# compare and print numbers that appear in both files
result = [int(num) for num in file1_data if num in file2_data]

# compare print the even numbers that exists in both files
print_even_numbers = [int(num) for num in file1_data if num in file2_data and int(num) % 2 == 0]

print(result)
print(print_even_numbers)
