def obrnuto(x):
    if len(x)==1:
        return x
    else:
        return obrnuto(x[1::]) + x[0]

x = input("unesi string koji se treba obrnuti")
