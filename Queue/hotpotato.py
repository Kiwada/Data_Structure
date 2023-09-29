from Fila import Fila

s = Fila()
print(s.items)
s.enqueue("Bill","jesus")
print(s.items)


'''def hotPotato(namelist, num):
    
    Pessoas = Fila()
    for name in namelist:
        Pessoas.enqueue(name)

    while Pessoas.size() > 1:
        for i in range(num):
            Pessoas.enqueue(Pessoas.dequeue())

        Pessoas.dequeue()

    return Pessoas.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

'''

