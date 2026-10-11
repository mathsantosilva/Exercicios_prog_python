## Solução Kata

def descending_order(num):
    # Bust a move right here
    list_nums = list(str(num))
    troca = True
    while troca:
        troca = False
        for i in range(len(list_nums) - 1):
            if list_nums[i] < list_nums[i + 1]:
                temp = list_nums[i]
                list_nums[i] = list_nums[i + 1]
                list_nums[i + 1] = temp
                troca = True
    lista_string = ''.join(list_nums)
    return int(lista_string)

