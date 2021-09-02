from get_soz import get_soz
from display import display
def play():
    word = get_soz()
    word_letters = set(word)
    user_letters = ''
    print(f'Men {len(word)} honalik so\'z o\'yladim,Topa olasizmi? ')
    while len(word_letters)>0:
        print(display(user_letters, word))
        if user_letters:
            print(f'Shu vaqtgacha kiritgan harflaringiz: {user_letters}')
        letter = input('Xarf kiriting: ').upper()
        if letter in user_letters:
            print('Siz bunday harf kiritgansiz!')
        elif letter in word:
            word_letters.remove(letter)
            print(f'{letter} xarfi to\'g\'ri')
        else:
            print('Bunday harf yo\'q')
        user_letters += letter
    print(f'Tabriklayman Siz {word} so\'zini {len(user_letters)} urinishda topdingiz!')
print(play())

