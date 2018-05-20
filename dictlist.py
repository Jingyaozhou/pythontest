rawlist = [('a', 3), ('b', 4), ('a', 5)]


def dictlistfunc(rawlist):
    dictlist = {}
    for key, value in rawlist:
        if key not in dictlist.keys():
            dictlist[key] = [value]

        else:
            dictlist[key].append(value)
    return dictlist


print(dictlistfunc(rawlist))
rawname = ['a', 'b', 'a']
rawvalue = [3, 4, 5]
print(dictlistfunc(zip(rawname, rawvalue)))

d = {key: [value] for (key, value) in rawlist}
print(d)
