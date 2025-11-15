def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left = mergesort(lista[:mid])
    right = mergesort(lista[mid:])

    return merge(left, right)
