import sys

if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    bool = True
    j = 0
    i = 0
    check = False
    while str1 != ''  and len(str2) >= 1:

        if str1[i] == str2[j] or str2[j] == '*':
            if str2[j] == '*':
                check = True
            if str1 != '':
                str1 = str1[1: (len(str1))]
            if str2 != '':
                str2 = str2[1: (len(str2))]

        elif str1[i] != str2[j] and check == False:
            bool = False
            break

        elif str1[i] != str2[j] and check == True:
            s = len(str2)
            str1 = str1[1: (len(str1))]

    if str1 == '' and len(str2) >= 1:
        for l in range(len(str2)):
            if str2[l] == '*':
                bool *= True
            else:
                bool *= False

    if bool == True:
        print('OK')
    else:
        print('KO')
