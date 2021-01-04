alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def build_from_z(z: list) -> str:
    if z[0] != 0:
        return "!"

    s = ""
    new_char = 0

    # идём по каждому числу из z
    for i in range(len(z)):
        # переменная i одновременно и индекс в z и индекс буквы в s
        # если i равна длине s и z[i] == 0 значит выбор только один - дописать новую букву
        if z[i] == 0 and len(s) == i:
            s += alphabet[new_char]
            new_char += 1
        # длина строки также может оказаться больше i т. к. мы дописали её на основании предыдущих z[i]
        else:
            # если в z[i] длина префикса больше, чем можно дописать, то такого не может быть
            if z[i] > len(z) - i:
                return "!"
            # здесь идёт дописывание строки или проверка уже написанного, чтобы оно согласовывалось
            for j in range(z[i]):
                if i + j == len(s):
                    s += s[j]
                elif s[j] != s[j + i]:
                    return "!"
            # условие ниже отсекает некорректные z функции, где в z[i] написана не максимальная длина префикса
            # например [0, 4, 2, 2, 1, 0]
            if i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
                return "!"
    return s


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        z = [int(i) for i in input().split()]
        print(build_from_z(z))
