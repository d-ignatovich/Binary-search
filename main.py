import timeit


# The function determines the index of the first occurrence of the specified element.
def ind_rec(numbers, x):
    low = 0
    high = len(numbers) - 1
    while low < high:
        m = (low + high) // 2
        if x > numbers[m]:
            low = m + 1
        else:
            high = m
    if numbers[high] == x:
        return high
    return None


# Data entry
numbers = list(map(int, input().split()))
value = int(input())

# Recursive search
t0 = timeit.default_timer()
print(ind_rec(numbers, value))
t1 = timeit.default_timer() - t0
print(t1)

# Iterative search
t0 = timeit.default_timer()
mid = len(numbers) // 2
low = 0
high = len(numbers) - 1

while numbers[mid] != value and low <= high:
    if value > numbers[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("None")
else:
    print(mid)

t1 = timeit.default_timer() - t0
print(t1)
