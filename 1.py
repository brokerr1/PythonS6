def check(text):
    sets = set() 
    for i in text.split():
        count = 0
        for j in i:
            if j in 'ауоыиэяюёе':
                count += 1
        sets.add(count)
    print(sets)
    if len(sets) == 1:
        return 'Парам пам-пам'
    return 'Пам парам'
    print(sets)

text = input('Введите стих: ')
print(check(text))