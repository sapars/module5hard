from typing import List

titles = [
    'Titanium',
    'Teal km',
    'Hunkover',
    'Fiends'
]
duration = [
    8200,
    7200,
    5400,
    120000
]
modes = [
    False,
    True,
    True,
    False
]
time_now: list[int] = [0] * 4
movs = list(zip(titles, duration, time_now, modes))


if __name__ == "__main__":
    movs = list(zip(titles, duration, modes))
    for i in movs:
        print(*i)
