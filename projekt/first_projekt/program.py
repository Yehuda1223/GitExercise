import math

def sum_number(a, b):
    sum = 0
    for i in range(a, b):
        sum = sum + i
    return sum
    
def main():
    a = 1
    b = 100
    print(sum_number(a, b))
    print(assembly(1558))
    print(assembly(5))
    print(assembly(6))
    print(assembly(7))
    print(assembly(8))
    print(is_prime(5))
    print(is_prime(6))
    print(is_prime(7))
    print(is_prime(8))
    print(is_prime(14))
    print(is_prime(152))
    print(is_prime(60693))
def assembly(number):
    return math.factorial(number)
    

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()