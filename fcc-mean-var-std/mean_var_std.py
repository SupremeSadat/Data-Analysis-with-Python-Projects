import numpy as np

def calculate(list):



    result = {}
    answer = []
    try:
        myArray = (np.asarray(list)).reshape((3,3))
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    answer.append(myArray.mean(axis=0).tolist())
    answer.append(myArray.mean(axis=1).tolist())
    answer.append(myArray.mean().tolist())
    result['mean']=answer

    answer = []
    myArray = (np.asarray(list)).reshape((3, 3))
    answer.append(myArray.var(axis=0).tolist())
    answer.append(myArray.var(axis=1).tolist())
    answer.append(myArray.var().tolist())
    result['variance'] = answer

    answer = []
    myArray = (np.asarray(list)).reshape((3, 3))
    answer.append(myArray.std(axis=0).tolist())
    answer.append(myArray.std(axis=1).tolist())
    answer.append(myArray.std().tolist())
    result['standard deviation'] = answer

    answer = []
    myArray = (np.asarray(list)).reshape((3, 3))
    answer.append(myArray.max(axis=0).tolist())
    answer.append(myArray.max(axis=1).tolist())
    answer.append(myArray.max().tolist())
    result['max'] = answer

    answer = []
    myArray = (np.asarray(list)).reshape((3, 3))
    answer.append(myArray.min(axis=0).tolist())
    answer.append(myArray.min(axis=1).tolist())
    answer.append(myArray.min().tolist())
    result['min'] = answer

    answer = []
    myArray = (np.asarray(list)).reshape((3, 3))
    answer.append(myArray.sum(axis=0).tolist())
    answer.append(myArray.sum(axis=1).tolist())
    answer.append(myArray.sum().tolist())
    result['sum'] = answer


    return result