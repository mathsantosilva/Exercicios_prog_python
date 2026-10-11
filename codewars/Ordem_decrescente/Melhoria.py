## Solução Kata

def descending_order(num):
    # Bust a move right here
    limite_reducao = 1
    list_nums = list(str(num))
    troca = True
    while troca and limite_reducao < len(list_nums):
        troca = False
        for i in range(len(list_nums) - limite_reducao):
            if list_nums[i] < list_nums[i + 1]:
                temp = list_nums[i]
                list_nums[i] = list_nums[i + 1]
                list_nums[i + 1] = temp
                troca = True
        limite_reducao += 1
    return int(''.join(list_nums))