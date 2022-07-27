n = int(input())
years = int(input())

def bank(a, b):
    result = a+(b*(a/100*10))
    print(result)

bank(n, years)    