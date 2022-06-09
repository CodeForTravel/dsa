
n = 3


def simple_recurrence(n):
    print("==================")
    if n > 0:
        print(f"hello {n}")
        n = n-1
        simple_recurrence(n)


simple_recurrence(n)
# it's calling the function n+1 times
