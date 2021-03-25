'''
def solution(mylist):
    res = []
    for i in range(len(mylist)):
        res.append(list(map(lambda L: L[i], mylist)))

    return res


if __name__ == '__main__':
    res = solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(res)
'''
##################################################################
animals = ['cat', 'dog', 'lion']    # Key list
sounds = ['meow', 'woof', 'roar']   # Value list

# K-V store를 만들 때 유용함.
answer = dict(zip(animals, sounds))
print(answer)
print(answer['cat'])