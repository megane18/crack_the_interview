def is_permutation(s, t):
    dict_s = {}
    dict_t = {}

    for item in s:
        if item not in dict_s:
            dict_s[item] = 1
        else:
            dict_s[item] += 1

    for item in t:
        if item not in dict_t:
            dict_t[item] = 1
        else:
            dict_t[item] += 1

    return dict_s == dict_t


s = ""
t = ""
print(is_permutation(s, t))
