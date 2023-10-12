def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main":
    try:
        start_range = int(input("Enter the start of the range: "))
        end_range = int(input("Enter the end of the range: "))
        
        if start_range <= end_range:
            prime_numbers = generate_primes(start_range, end_range)
    
            print("Prime numbers between {} and {}:".format(start_range, end_range))
            for prime in prime_numbers:
                print(prime)
        else:
            print("The start range must be less than or equal to the end range.")
    except ValueError:
        print("Please enter valid integer values for the range.")
