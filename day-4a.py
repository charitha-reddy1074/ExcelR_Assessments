def sum_of_even_numbers(n):
    # Calculate the sum of all even numbers between 1 and n
    sum_even = sum(i for i in range(2, n+1, 2))
    return sum_even

# Input the positive integer n
n = int(input("Enter a positive integer: "))

# Calculate and print the sum of even numbers
sum_even = sum_of_even_numbers(n)
print(f"The sum of all even numbers between 1 and {n} is: {sum_even}")