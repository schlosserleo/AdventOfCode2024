a = [[i for i in range(10)] for _ in range(10)]

b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

anzahl_zeilen: int = len(b)
anzahl_spalten: int = len(b[0])

zeilen_counter = 0
spalten_counter = 0

diag_lines = anzahl_zeilen + anzahl_spalten - 1


for i in range(diag_lines):
    j = abs(zeilen_counter - spalten_counter)
    k = 0
    print(
        f"i = {i}, j = {j}, zeilen_counter = {zeilen_counter}, spalten_counter = {spalten_counter}"
    )
    for _ in range(spalten_counter + 1):
        print(f"{[b[zeilen_counter - k][j]]}", end="")
        j += 1
        k += 1

    if i < anzahl_zeilen - 1:
        zeilen_counter += 1

    if i < anzahl_spalten - 1:
        spalten_counter += 1
    else:
        spalten_counter -= 1
    print(
        f"\ni = {i}, j = {j}, zeilen_counter = {zeilen_counter}, spalten_counter = {spalten_counter}"
    )
    print()
