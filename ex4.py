def ex4():
    def fibonacci(n):
        a, b = 0, 1
        sequence = []
        for _ in range(n):
            sequence.append(b)
            a, b = b, a + b
        return sequence

    n = int(input("Enter a number: "))
    fib_sequence = fibonacci(n)

    print(fib_sequence)


if __name__ == "__main__":
    ex4()

