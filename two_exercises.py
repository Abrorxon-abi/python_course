def generate_primes(limit):
    primes = [2]
    current_num = 3

    while current_num < limit:
        is_prime = True
        for prime in primes:
            if prime * prime > current_num:
                break
            if current_num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(current_num)
        current_num += 2

    return primes


def find_prime_with_most_consecutive_sums(limit):
    primes = generate_primes(limit)
    max_consecutive = 0
    result = 0

    for i in range(len(primes)):
        consecutive = 0
        prime_sum = 0
        for j in range(i, len(primes)):
            prime_sum += primes[j]
            if prime_sum > limit:
                break
            consecutive += 1
            if prime_sum in primes and consecutive > max_consecutive:
                max_consecutive = consecutive
                result = prime_sum
    return result


limit = 1000
prime_with_most_consecutive_sums = find_prime_with_most_consecutive_sums(limit)
print("The prime below one million that can be written as the sum of the most consecutive primes is:",
      prime_with_most_consecutive_sums)


def maxArea(height):
    n = len(height)
    left = 0
    right = n - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
