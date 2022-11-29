

def next_pal(i):
    i = i+1
    i = str(i)
    while i != i[::-1]:
        i = int(i)
        i = i+1
        i = str(i)
    return(i)


print(next_pal(11))
