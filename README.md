def is_prime(n):
    flag = True
    for i in range(2, n):

        if n % i == 0:
            flag = False
            return flag

    return flag


number = int(input("enter number : "))
print(is_prime(number))
