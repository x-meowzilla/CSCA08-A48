def insertion_sort(L):
    for i in range(1, len(L)):                      # 5 steps - len/range 1 step, for 3 steps
        current_val = L[i]                          # 2 steps - selection 1 step, assignment 1 step
        j = i                                       # 1 steps - assignment 1 step
        while (j > 0 and L[j - 1] > current_val):   # 11 steps - comparison 2 step, subtraction 1 step, selection 1 step, while 3 steps
            L[j] = L[j - 1]                         # 4 steps - subtraction 1 step, selection 1 step
            j = j - 1                               # 2 steps
        L[j] = current_val                          # 2 steps

    # worst case analysis
    # line 5-7 may happen up to n times: (11 + 4 + 2) * n = 17n
    # line 2-4 + line 5-7 + line 8 may happen up to n times: (5 + 2 + 1 +17n + 2) * n = 17n^2 + 10n
    # T(n) = 17n^2 + 10n


if (__name__ == "__main__"):
    L = [5, 7, 1, 9, 3, 2, 0, 4, 6, 8]
    insertion_sort(L)
    print(L)
