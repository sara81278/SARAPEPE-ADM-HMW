if __name__ == '__main__':
    lista = []
    commands = []
    N = int(input())
    for _ in range(0,N):
        comm, *elements = input().split()
        commands.append([comm, elements])
        
    for command, element in commands:
        if(command == 'append'):
            lista.append(int(*element))
        elif(command == 'print'):
            print(lista)
        elif(command == 'remove'):
            lista.remove(int(*element))
        elif(command == 'insert'):
            lista.insert(int(element[0]), int(element[1]))
        elif(command == 'sort'):
            lista.sort()
        elif(command == 'pop'):
            lista.pop()
        elif(command == 'reverse'):
            lista.reverse()
