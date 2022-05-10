import sys

def taskEval(taskData):
    total = 0
    correct = 0
    for line in taskData:
        total += 1
        words = line.split(' ')
        if words[3] == words[4]:
            correct += 1
    return(correct / total)
        
with open(sys.argv[1], 'r') as task_w2v, open(sys.argv[2], 'r') as task_myv:
    print('正解率(word2vec): '+str(taskEval(task_w2v)))
    print('正解率(ex85): '+str(taskEval(task_myv)))
    
