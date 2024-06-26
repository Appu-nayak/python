'''def is_armstrong_number(num):
    
    num_str = str(num)
    num_digits = len(num_str)
    
    
    armstrong_sum = 0
    
    
    for digit_char in num_str:
        digit = int(digit_char)
        armstrong_sum += digit ** num_digits
    
    
    return armstrong_sum == num


number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")'''
'''def is_leap_year(year):
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")'''
'''def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1
    return True

string = input("Enter a string: ")
if is_palindrome(string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")'''
    
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)

    return fib_series

n_terms = int(input("Enter the number of terms in the Fibonacci series: "))

if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = fibonacci(n_terms)
    print("Fibonacci series up to {} terms:".format(n_terms), fib_series)










