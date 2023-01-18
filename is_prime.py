def is_prime(num):
    if num > 1:

        for i in range(2, int(num / 2) + 1):

            if (num % i) == 0:
                return f"{num}, is not a prime number"
        else:
            return f"{num}, is a prime number"
    else:
        return f"{num}, is not a prime number"
