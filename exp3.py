with open('zen_of_python.txt') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
