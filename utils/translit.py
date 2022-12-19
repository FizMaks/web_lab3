def translit(s):
    rus_alf = list(
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    angl_alf = ['a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh', 'z', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'r', 's', 't', 'y', 'f', 'h', 't', 'sch', 'shs', 'chy', "~", "iy", "`", 'ej', 'u', 'ia']
    ans = ''

    s = s.lower()
    if s:
        for i in s:
            if i in rus_alf:
                ans += angl_alf[rus_alf.index(i)]
            else:
                ans += i
        return ans
    else:
        return 'empty'


if __name__ == "__main__":
    print(translit(
        'Privet МИр 45, как твои дела (!?) абвгдеёжзийклмнопрстуфхцчшщъыьэюя, АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'))
