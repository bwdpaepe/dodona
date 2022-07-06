matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = zip(*matrix)
list(transposed)

def alfabetisch(input):
    inputList = str.split(input)
    sortedList = sorted(inputList)
    output = sortedList.pop(0)
    for item in sortedList:
        output = output + ' ' + item
    return output

