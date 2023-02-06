from random import sample
'''
Функция Ьinary_search получает отсортированный массив и значение. Если
значение присутствует в массиве, то функция возвращает его позицию. При
этом мы должны следить за тем, в какои части массива проводится поиск.
'''


def binary_search(list,item):
    low = 0
    high = len(list)-1
    count = 0

    while low<=high:
        mid = int((low+high)/2)
        guess = list[mid]
        count+=1
        if guess == item:
            print(f'{count} step for search')
            return mid+1
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    print(f'{count} step for search')
    return None

m_list = sorted(sample(range(1, 129), 128))

print(binary_search(m_list,127))




