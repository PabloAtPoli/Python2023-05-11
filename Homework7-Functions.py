# Third commit


# swap of variables using addition and subtractions
# def arithmetic_swap(a, b):
#     sum_variables = a + b
#     a = sum_variables - a
#     b = sum_variables - b
#     return a, b


# x = 4
# y = 5
# print("Before arithmetic swap: x =  ", x, " y = ", y)
# x, y = arithmetic_swap(x, y)
# print("After arithmetic swap: x =  ", x, " y = ", y)

# swap of variables using no additional  memory
# def no_additional_memory_swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b
#
#
# x = 4
# y = 5
# print("Before no-additional-memory swap: x =  ", x, " y = ", y)
# x, y = no_additional_memory_swap(x, y)
# print("After no-additional-memory swap: x =  ", x, " y = ", y)


# swap of variables using xor operator without using additional memory
# q: write the xor_swap(a, b) function in Java                      
# q: write the xor_swap(a, b) function in C++
# q: write the xor_swap(a, b) function in C

# Write a SQL a table named Employee in SQL using Python  with the following ttributes:
# 1. id
# 2. name
# 3. email
# 4. phone
# 5. address
# 6. city
# 7. state
# 8. zip
# 9. country
# 10. username
# 11. password
# 12. date_created
# 13. date_updated
# 14. last_login        
# 15. last_logout
# 16. is_active     
# 17. is_admin





# def xor_swap(a, b):
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
#     return a, b


# x = 4
# y = 5
# print("Before xor swap: x =  ", x, " y = ", y)
# x, y = xor_swap(x, y)
# print("After xor swap: x =  ", x, " y = ", y)


# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "fizzbuzz"
#     elif num % 3 == 0:
#         return "fizz"
#     elif num % 5 == 0:
#         return "buzz"
#     else:
#         return num
#
#
# print(fizz_buzz(5))
# print(fizz_buzz(3))
# print(fizz_buzz(8))
# print(fizz_buzz(15))

# Swaps packing and unpacking tuples
# x = 4
# y = 5
# print("Before packing and unpacking swap: x =  ", x, " y = ", y)
# y, x = x, y
# print("After packing and unpacking s swap: x =  ", x, " y = ", y)

# Print the first 100 natural numbers except for those divisible by 3, using continue statement
# for i in range(1,101):
#     if i % 3 == 0:
#         continue
#     print(i, end=", ")

# Simplify the previous code without the continue statement
# for i in range(1,101):
#     if i % 3 != 0:
#         print(i, end=", ")

# Print the first 100 natural numbers except for those divisible by 3 or 5, using continue statement
# print("First 100 natural numbers except for those divisible by 3 or 5, using continue statement:")
# for i in range(1,101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i, end=", ")

# Simplify the previous code without the continue statement
# print("\nFirst 100 natural numbers except for those divisible by 3 or 5, without continue statement:")
# for i in range(1, 101):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i, end=", ")

# Print the first 100 natural numbers except for those divisible by 3 or 5, using list comprehension
# print([i for i in range(1, 101) if i % 3 != 0 and i % 5 != 0])

# Says if a number is prime or not, using for else loop

# Using the function is_prime(n) below, write a program that generates prime numbers up to 100
# using the function is_prime(n) below, write a prog
# This function was fixed by Alejandro
def is_prime(n):
    if n <= 1:
        return False
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return True


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True


# count = 0
# i = 2
# while count < 100:
#     if is_prime(i):
#         print(i, end=", ")
#         count += 1
#     i += 1
#
# print()
# Says if a number is prime or not, using for else loop
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True


# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(n, " is prime")
# else:
#     print(n, " is not prime")
# Says if a number is prime or not, checking possible factors up to n/2, using for else loop
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n/2) + 1):
#         if n % i == 0:
#             break
#             return False
#     else:
#         return True


# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(n, " is prime")
# else:
#     print(n, " is not prime")


# Says if a number is prime or not, optimized and using for else loop
# def is_prime_optimized(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             break
#             return False
#     else:
#         return True




# Write a comment describing what this code does, as well as any other information you think is relevant. Include any function names, variable names, or other identifiers that you think are important. You can also include any other information that you think is relevant, such as the purpose of the code, the context in which it is used, or any other information that you think is relevant.

# This code uses the general form of the for loop, which is:
# for i in range(start, stop, step):
#     statements
# where start is the starting value of the loop, stop is the stopping value of the loop, and step is the step size of the loop.



# swap of variables using addition and subtractions
# def arithmetic_swap(a, b):
#     sum_variables = a + b
#     a = sum_variables - a
#     b = sum_variables - b
#     return a, b
#
#
# x = 4
# y = 5
# print("Before arithmetic swap: x =  ", x, " y = ", y)
# x, y = arithmetic_swap(x, y)
# print("After arithmetic swap: x =  ", x, " y = ", y)

# swap of variables using no additional  memory
# def no_additional_memory_swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b
#
#
# x = 4
# y = 5
# print("Before no-additional-memory swap: x =  ", x, " y = ", y)
# x, y = no_additional_memory_swap(x, y)
# print("After no-additional-memory swap: x =  ", x, " y = ", y)


# swap of variables using xor operator without using additional memory
# def xor_swap(a, b):
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
#     return a, b
#
#
# x = 4
# y = 5
# print("Before xor swap: x =  ", x, " y = ", y)
# x, y = xor_swap(x, y)
# print("After xor swap: x =  ", x, " y = ", y)


# def fizz_buzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "fizzbuzz"
#     elif num % 3 == 0:
#         return "fizz"
#     elif num % 5 == 0:
#         return "buzz"
#     else:
#         return num
#
#
# print(fizz_buzz(5))
# print(fizz_buzz(3))
# print(fizz_buzz(8))
# print(fizz_buzz(15))

# Swaps packing and unpacking tuples
# x = 4
# y = 5
# print("Before packing and unpacking swap: x =  ", x, " y = ", y)
# y, x = x, y
# print("After packing and unpacking s swap: x =  ", x, " y = ", y)

# Print the first 100 natural numbers except for those divisible by 3, using continue statement
# for i in range(1,101):
#     if i % 3 == 0:
#         continue
#     print(i, end=", ")

# Simplify the previous code without the continue statement
# for i in range(1,101):
#     if i % 3 != 0:
#         print(i, end=", ")

# Print the first 100 natural numbers except for those divisible by 3 or 5, using continue statement
# print("First 100 natural numbers except for those divisible by 3 or 5, using continue statement:")
# for i in range(1,101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i, end=", ")

# Simplify the previous code without the continue statement
# print("\nFirst 100 natural numbers except for those divisible by 3 or 5, without continue statement:")
# for i in range(1, 101):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i, end=", ")

# Print the first 100 natural numbers except for those divisible by 3 or 5, using list comprehension
# print([i for i in range(1, 101) if i % 3 != 0 and i % 5 != 0])

# Says if a number is prime or not, using for else loop
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             break
#             return False
#     else:
#         return True
#
#
# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(n, " is prime")
# else:
#     print(n, " is not prime")

# Says if a number is prime or not, checking possible factors up to n/2, using for else loop
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n/2) + 1):
#         if n % i == 0:
#             break
#             return False
#     else:
#         return True


# n = int(input("Enter a number: "))
# if is_prime(n):
#     print(n, " is prime")
# else:
#     print(n, " is not prime")


# Says if a number is prime or not, optimized and using for else loop
# def is_prime_optimized(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             break
#             return False
#     else:
#         return True


# n = int(input("Enter a number: "))
# if is_prime_optimized(n):
#     print(n, " is prime")
# else:
#     print(n, " is not prime")


# print("Primes no optimized")
# for i in range (1000):
#     if is_prime(i):
#         print(i, end=", ")

# print("\nPrimes optimized")
# for i in range (1000):
#     if is_prime_optimized(i):
#         print(i, end=", ")

#         print(i, end=", ")

# n = int(input("Enter a number: "))
# if is_prime_optimized(n):
#     print(n, " is prime")
# else:
#     print(n, " is not prime")


# print("Primes no optimized")
# for i in range (1000):
#     if is_prime(i):
#         print(i, end=", ")

# print("\nPrimes optimized")
# for i in range (1000):
#     if is_prime_optimized(i):
#         print(i, end=", ")