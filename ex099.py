def maior(*num):
    print('-=' * 20)
    mai = 0
    print(f'Foram informados {len(num)} valores sendo eles: ', end='')
    for c in num:
        print(c, end=' ')
        if c > mai:
            mai = c
    print()
    print(f'O maior valor informado foi: {mai}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()