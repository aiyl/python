def itoBase(num, from_base, to_base):
    try:

        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return char[n]
        else:
            return itoBase(n // to_base, 10, to_base) + char[n % to_base]

    except Exception as e:
        print('Некорректные данные! ', e)

if __name__ == "__main__":
    print("введите число")
    number = input()
    print("введите систему счисления")
    baseSrc = int(input())
    print("В какую систему счисления перевести?")
    baseDst = int(input())
    print('Ответ:')
    print(itoBase(number, baseSrc, baseDst))
