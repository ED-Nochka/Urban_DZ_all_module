numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_prime = []
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
            set_not_prime = (set(numbers) - set(primes))
            not_prime = list(set_not_prime)
print(f"Primes: {primes}")
print(f"Not_prime: {not_prime}")

