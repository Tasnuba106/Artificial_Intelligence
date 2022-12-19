def pattern_make(x,y):
    for i in range(x,y):
        for j in range(i,i+5):
            print(j,end='')
        print()
pattern_make(1,6)