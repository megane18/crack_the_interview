def palindrome_permutation(s):

    new_s= s.replace(" ", "")

    new_dict = {}


    for item in new_s.lower():
        if item not in new_dict:
            new_dict[item] = 1
        else:
            new_dict[item] +=1

    count=0
    for item in new_dict.values():
        if item == 1:
            count +=1

    if count >1:
        return False
    else:
        return True