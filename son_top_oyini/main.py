def main():
    import son_top as f
    import son_top_pc as pc
    while True:
        print(f.son_top(100))
        print(pc.son_top(100))
        if f.taxminlar == pc.taxminlar:
            print('Durrang')
        elif f.taxminlar>pc.taxminlar:
            print('Siz yutqazdingiz!')
        elif f.taxminlar<pc.taxminlar:
            print('Siz yutdingiz!')
        m = input('Yana o\'ynaymizmi? yes/no: ')
        if m == 'yes':
            continue
        else:
            break
    return 'Dastur tugadi!'
print(main())