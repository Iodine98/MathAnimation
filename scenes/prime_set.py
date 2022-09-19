from copy import copy




class PrimeSet:
    """
    Calculate a number's prime set
    """

    def __init__(self, number: int, **kwargs):
        self.number = number
        if 'primes' in kwargs:
            self.primes = kwargs['primes']
        else:
            self.primes = [2]
        self.prime_set = dict()
        self.calculate_prime_set()

    def as_array(self, layer_no: int = -1):
        if layer_no == -1:
            return [[base, exp] for base, exp in self.prime_set.items()]
        else:
            return [[base, exp, layer_no] for base, exp in self.prime_set.items()]

    def __str__(self):
        prime_set_str = "{"
        for index, (base, exp) in enumerate(self.prime_set.items()):
            prime_set_str += f"({base}, {exp})"
            if index < len(self.prime_set) - 1:
                prime_set_str += ","
        return prime_set_str + "}"

    def is_prime(self, k: int):
        for prime in self.primes:
            if k % prime == 0:
                return False
        return True

    def calculate_prime_set(self):
        temp_number = copy(self.number)
        for number in range(3, temp_number):
            if temp_number in (0,1):
                break
            if not self.is_prime(number):
                continue
            self.primes.append(number)
            for prime in self.primes:
                count = 0
                while temp_number % prime == 0:
                    temp_number = temp_number // prime
                    count += 1
                if count > 0:
                    self.prime_set[prime] = count
        if temp_number > 1:
            self.prime_set[self.number] = 1
