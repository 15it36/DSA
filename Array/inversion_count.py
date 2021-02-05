INV_COUNT = 0
def merge_sort(arr: list):
    global INV_COUNT
    if len(arr) > 1:
        mid = int(len(arr) // 2)

        L = arr[:mid]
        R = arr[mid:]
        INV_COUNT += merge_sort(L)
        INV_COUNT += merge_sort(R)

        print(L)
        print(R)

        i = j = k = 0

        while i < j:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                print("comes to else")
                arr[k] = R[j]
                j += 1
                INV_COUNT += (mid - i + 1)
            k += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print(INV_COUNT)

    return INV_COUNT


def merge(arr, left, right):


def inversion_count(arr):
    inv_count = merge_sort(arr)
    print(arr)
    return inv_count


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    print(inversion_count(arr))