import sys

if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    i = 0
    j = 0
    if len(str2) >= len(str1):
        len1 = len(str2)
        len2 = len(str1)
    else:
        len1 = len(str1)
        len2 = len(str2)
    bool = True
    while i < len2:
        if str1[i] != str2[j] and str1[i] != '*' and str2[j] != '*':
            bool = False
        i += 1
        j += 1

    if bool == True:
        print('OK')
    else:
        print('KO')
