def factorial_number(n):
        count = 0
        i = 5
        while (n / i>=1):
            count += int(n/i)
            i *=5
        return int(count)
n = 100
print("fatorial of the number"+
         "is 100 is",factorial_number(n))
