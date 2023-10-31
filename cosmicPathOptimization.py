from typing import List


def average_temperature(n: int, temperatures: List[int]) -> int:
    total_temperature = sum(temperatures)
    return total_temperature // n


def main() -> None:
    n = int(input())
    temperatures = list(map(int, input().split()))
    print(average_temperature(n, temperatures))


if __name__ == "__main__":
    main()
