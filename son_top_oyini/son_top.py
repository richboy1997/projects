taxminlar = 0
def son_top(n):
    import random
    global taxminlar
    taxminlar = 0
    quyi,yuqori = 1,n
    son_p = random.randint(quyi,yuqori)
    print(f'Men 1 dan {yuqori} gacha oraliqda son o\'yladim uni topishga harakat qiling.\n (dasturdan chiqish uchun "exit" deb yozing')
    while True:
        son_f = input('Sonni kiriting: ')
        taxminlar+=1
        if son_f == 'exit':
            break
        if int(son_f) == son_p:
            print(f'Tabriklayman siz sonni {taxminlar} urinishda topdingiz topdingiz!')
            break
        elif int(son_f) > son_p:
            print(f'Men o\'ylagan son {son_f} dan kichik. Yana harakat qiling')
        elif int(son_f) < son_p:
            print(f'Men o\'ylagan son {son_f} dan katta. Yana harakat qiling')
    return '\n'
