def remove_duplicate(x):
    res = list(set(x))
    return res


n = [1, 1, 2, 2, 3, 5, 5, 6, 6, 7, 8, 9]

if __name__ == "__main__":
    print(type(remove_duplicate(n)))
