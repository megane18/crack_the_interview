def one_away(s, t):

    pointer_s = 0
    pointer_t = 0
    differentChar = 0

    x = len(s)
    y = len(t)

    while pointer_s < x and pointer_t < y:

        if s[pointer_s] == t[pointer_t]:
            # sameChar +=1
            pointer_s += 1
            pointer_t += 1
        else:
            differentChar += 1
            if len(s) < len(t):
                pointer_t += 1
            elif len(s) > len(t):
                pointer_s += 1
            else:
                pointer_s += 1
                pointer_t += 1

    if differentChar > 1:
        return False
    else:
        return True
