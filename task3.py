# 3. На языке Python реализовать функцию, которая
# быстрее всего (по процессорным тикам) отсортирует данный ей
# массив чисел. Массив может быть любого размера со случайным
# порядком чисел (в том числе и отсортированным).
# Объяснить почему вы считаете, что функция соответствует заданным критериям.

import random


minrun = 32


def ins_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        temp = arr[i]
        j = i - 1
        while j >= start and temp < arr[j]:
            arr[j + 1], arr[j] = arr[j], temp
            j -= 1
    return arr


def merge(arr, start, mid, end):
    if mid == end:
        return arr
    first = arr[start : mid + 1]
    last = arr[mid + 1 : end + 1]
    len1 = mid - start + 1
    len2 = end - mid
    i, j = 0, 0
    ind = start
    while i < len1 and j < len2:
        if first[i] < last[j]:
            arr[ind] = first[i]
            i += 1
        else:
            arr[ind] = last[j]
            j += 1
        ind += 1
    while i < len1:
        arr[ind] = first[i]
        i += 1
        ind += 1
    while j < len2:
        arr[ind] = last[j]
        j += 1
        ind += 1
    return arr


def timsort(arr):
    n = len(arr)
    # Сортировка вставками подмассивов размером minrun
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        arr = ins_sort(arr, start, end)
    # Слияние отсортированных подмассивов
    curr_size = minrun
    while curr_size < n:
        for start in range(0, n, curr_size * 2):
            mid = min(n - 1, start + curr_size - 1)
            end = min(n - 1, mid + curr_size)
            arr = merge(arr, start, mid, end)
        curr_size *= 2
    return arr


# В лучшем случае скорость работы сортировки будет O(n),
# в худшем и среднем O(nlogn)


def qsort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[0]
    left = []
    right = []
    for elem in arr[1:]:
        if elem < mid:
            left.append(elem)
        else:
            right.append(elem)
    return qsort(left) + [mid] + qsort(right)


# Qsort в свою очередь сортирует со средней скоростью O(nlogn) и менее
# требователен к памяти (logn вместо n), но в худшем случае, т.е. если
# опорный элемент выбирается как минимальный или максимальный, скорость
# работы может доходить до O(n^2)


def main():
    arr = [random.randint(1, 100) for _ in range(100)]
    print(arr)
    print(timsort(arr))
    print(qsort(arr))


if __name__ == "__main__":
    main()

# Стандартная функция sorted() или метод списка sort() реализуют сортировку timsort на C++.
# Наиболее эффективным с точки зрения времени будет использование данных функций,
# так как реализация на python будет заведомо медленнее реализации на C++.
