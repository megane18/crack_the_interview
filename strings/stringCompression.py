def string_compress(s):

    result = ""

    first = 0

    second = 1

    count = 1

    while first < len(s):

        while second < len(s) and first < len(s):

            if s[first] == s[second]:

                count += 1

                second += 1

            else:

                result += f"{s[first]}{count}"

                first = second

                second += 1

                count = 1

        result += f"{s[first]}{count}"

        first = second

    return result if len(result) < len(s) else s
