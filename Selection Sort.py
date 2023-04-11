def selection_sort(lista):
    for i in range(len(lista)):
        j=i
        for k in range(i+1,len(lista)):
            if lista[k]<lista[j]:
                j=k
        aux=lista[i]
        lista[i]=lista[j]
        lista[j]=aux
    return lista
l=[5,8,9,3,2,4,7,6,1,10]
print(selection_sort(l))
