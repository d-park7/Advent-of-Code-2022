with open('input_test.txt', 'r') as file:

    cycle = 1
    checkpoint = 20
    for line in file.read().splitlines():
        if cycle == checkpoint:
            print('find signal strength at cycle', checkpoint)
            checkpoint += 40
        cycle += 1

    while cycle < 220:
        if cycle == checkpoint:
            print('signal strength check')
            checkpoint += 40
        cycle +=1

