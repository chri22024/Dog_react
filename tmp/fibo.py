# Fibonacci numbers module
def fib(n):  # フィボナッチ級数を n まで出力
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):  # n までのフィボナッチ級数をリストで返す。
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result