def max_number(a: int, b=7, c=15) -> int:
    if a <= 0:
        return -1
    else:
        if b <= a >= c:
            return a
        elif a <= b >= c:
            return b
        elif a <= c >= b:
            return c


def main():
    a = int(input())
    print(max_number(a))


if __name__ == "__main__":
    main()
