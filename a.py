# 1. Prime no b/w range
# m - n -> print all prime nos

# 2. Perfect no.
# Sum of factors equal to no    28   1, 2, 4, 7, 14

# 3. Fibonacci series
# 0, 1, 1, 2, 3, 5 .....
# WAP to print exact n fibonacci nos.

# 4. Series --> 1,4, 9, 16, 25 ... n print

# 5. Input no of units consumed(monthly).
# 0-10  3/unit
# 10-20 5/unit
# 20-40 7/unit
# >40 	10/unit
# output bill in Rs.

# 6. WAP which takes n as a input and returns the factorial of n.

# 7. Series --> 1,4, 27, 256 ...n


def isPalindrome(n):
    temp = n
    s = 0
    while n != 0:
        d = n % 10
        s = s*10+d
        n = int(n/10)
    return s == temp


if __name__ == '__main__':
    print(isPalindrome(151))
