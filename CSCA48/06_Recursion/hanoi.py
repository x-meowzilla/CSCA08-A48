def hanoi(n, from_tower="Tower A",
          spare_tower="Tower B",
          to_tower="Tower C"):
    if (n > 0):
        hanoi(n - 1, from_tower, to_tower, spare_tower)
        print(from_tower + ' --> ' + to_tower)
        hanoi(n - 1, spare_tower, from_tower, to_tower)


if __name__ == "__main__":
    hanoi(3)
