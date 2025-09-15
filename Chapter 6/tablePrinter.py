#! /usr/bin/python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    # Find the maximum width of each column
    output = ''
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for item in tableData[i]:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)

    # Print the table with right-justified columns
    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            output += tableData[col][row].rjust(colWidths[col]) + ' '
        output += '\n'
    return output


print(printTable(tableData))
