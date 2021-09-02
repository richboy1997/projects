taxminlar = 0
def son_top(n):
    import random
    global taxminlar
    taxminlar = 0
    matn = 'To\'g\'ri (t) , Kattaroq (+) , Kichikroq (-): '
    yuqori,quyi = n,1
    son_p = random.randint(quyi,yuqori)
    print(f'1 dan {yuqori} gacha oraliqda son o\'ylang men uni topishga harakat qilaman.')
    print(input('O\'ylagan bo\'lsangiz istalgan tugmani bosing!'))
    while True:
        son_p = random.randint(quyi, yuqori)
        son_f = input(f'Siz {son_p} sonini o\'yladingizmi? {matn}')
        taxminlar+=1
        if son_f == 'exit':
            break
        if son_f == 't':
            print(f'Siz o\'ylagan sonni {taxminlar} urinishda topdim!')
            break
        elif son_f == '-':
            yuqori = son_p -1
        elif son_f == '+':
            quyi = son_p +1
    return '\n'