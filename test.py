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

print("\n")

# 1. Prime no b/w range
print("Question 1")

def prime_numbers(a,b):
    for i in range(a,b):
        count=0
        for j in range(1,i):
            if i%j ==0:
                count=count+1
        if count<2:
            print(i)

if __name__ == '__main__':
    print(prime_numbers(10,100))

print("\n")

# 2. Perfect no.
# Sum of factors equal to no    28   1, 2, 4, 7, 14
print("Question 2")

def perfact_num(p):
    temp=0
    for i in range(1,p):
        if p%i ==0:
            temp=temp+i
    return temp == p

if __name__ == '__main__':
    print(perfact_num(28))


print("\n")

# 3. Fibonacci series
# 0, 1, 1, 2, 3, 5 .....
# WAP to print exact n fibonacci nos.
print("Question 3")

def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        temp=a+b
        a=b
        b=temp

if __name__ == '__main__':
    print(fibonacci(20))


print("\n")

# 4. Series --> 1,4, 9, 16, 25 ... n print
print("Question 4")

def square(s):
    for i in range(1,s+1):
        print(pow(i,2))
    
if __name__ == '__main__':
    print(square(10))

print("\n")

# 5. Input no of units consumed(monthly).
# 0-10  3/unit
# 10-20 5/unit
# 20-40 7/unit
# >40 	10/unit
# output bill in Rs.
print("Question 5")

def bill(unit):
    amount=0
    if unit<10 :
        amount= unit*3
    elif unit<20 :
        amount= (unit-10)*5 + 30
    elif unit<40 :
        amount= (unit-20)*7 + 50 + 30
    else:
        amount= (unit-40)*10 + 140 + 50 + 30
    return amount

if __name__ == '__main__':
    print(bill(100))

print("\n")

# 6. WAP which takes f as a input and returns the factorial of f.
print("Question 6")

def factorial(f):
    if f > 1:
        return f * factorial(f-1)
    else:
        return 1


if __name__ == '__main__':
    print(factorial(6))

print("\n")

# 7. Series --> 1,4, 27, 256 ...n

print("Question 7")

def series(S):
    for i in range(1,S+1):
        print(pow(i,i))

if __name__ == '__main__':
    print(series(8))
    
