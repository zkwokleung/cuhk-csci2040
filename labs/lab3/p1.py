def non_unique(list):
    result = {}
    joinedList = []
    for l in list:
        joinedList += l
    joinedList.sort()

    for i in joinedList:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    # print("DEBUG:", joinedList)
    # print("DEBUG:", result)

    result = {key: value for (key, value) in result.items() if value > 2}

    return result


if __name__ == '__main__':
    print(non_unique([['a', 'c', 'a', 'e', 'e', 'f', 'j', 'j']]))
