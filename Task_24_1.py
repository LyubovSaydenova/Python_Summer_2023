def bubble_sort(items):
    print('Сортировка пузырьком')
    for limit in range(len(items) - 1, 0, -1):
        print(items)
        for i in range(limit):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
def selection_sort(items):
    print('\nСортировка выборкой')
    for i in range(len(items) - 1):
        print(items)
        index_min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[index_min]:
                index_min = j
        items[i], items[index_min] = items[index_min], items[i]
items1 = list(map(int, input().split()))
items2 = items1[:]
bubble_sort(items1)
print(items1)
selection_sort(items2)
print(items2)
