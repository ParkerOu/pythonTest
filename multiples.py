# Find the sum of all the multiples of 3 or 5 below 1000.
multiples = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 5 == 0:
        multiples = multiples + i

print(f"The sum of multiples: {multiples}")