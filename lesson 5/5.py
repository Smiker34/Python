import sys
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
def filter():
    result = []
    while True:
        try:
            num = src[0]
            try:
                src.index(num, 1)
            except ValueError:
                result.append(num)
            finally:
                while True:
                    try:
                        src.remove(num)
                    except ValueError:
                        break
        except IndexError:
            break
    return result
result = filter()
print(result)
print(sys.getsizeof(result))
print(sys.getsizeof(filter()))