from blist import blist

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr1 = blist(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    i = j = 0

    for idx in range(0, (len(arr1) + len(arr2))):
        print(arr1)
        if i < len(arr1) and arr2 and arr2[j] < arr1[i]:
            arr1.insert(i, arr2[j])
            arr2.pop(j)
        i += 1

    if arr2:
        arr1 = arr1 + arr2

    

    print(arr1)
