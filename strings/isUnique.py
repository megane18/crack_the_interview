def is_unique(s):

    for item in range(0, len(s) - 1):
        for items in range(item + 1, len(s)):

            if s[item] == s[items]:
                return False

    return True


s = ""
print(is_unique(s))
