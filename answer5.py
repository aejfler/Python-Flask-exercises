from random import randint
def roll(amount, type=6, modifier=0):
    TYPE = [3,4,6,8,10,12,100]

    if type not in TYPE:
        raise Exception
    result = sum(randint(1,type) for _ in range(amount)) + modifier
    return result

print(roll(2,10,20))