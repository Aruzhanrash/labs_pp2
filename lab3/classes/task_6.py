class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def filter_primes(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

numbers_input = input("Введите числа через пробел: ")
numbers = list(map(int, numbers_input.split()))

prime_filter = PrimeFilter(numbers)

prime_numbers = prime_filter.filter_primes()

print(f"Простые числа: {prime_numbers}")
