def hanoi(원반개수, 시작, 목표, 보조):
    if 원반개수 == 1:
        print(시작, '->', 목표) #원반개수가 1개라면 보조기둥을 쓸필요없이 바로 목표로 옮길 수 있다
        return          
    if:            
        hanoi(원반개수 -1, 시작, 보조, 목표) #목표기둥엔 가장큰 원반이 쌓여야 하기 때문에 보조를 써야한다 n개 일땐 n-1(큰거 빼고)개를 보조로 옮겨야한다
        print(시작, '->', 목표)       # 작은걸 다옮긴후 시작에 있는 큰 원반을 목표로 이동! 큰원반이 가장 아래에 있다면 움직일 필요가 없다 이 후 부터는 원래 원반 개수에서 한개를 뺀 갯수로 진행!
                                            #그렇다면 2번기둥에 있는 작은 원반들을 시작기둥으로 원래 시작기둥이였던 1번기둥을 보조로

        hanoi(원반개수 -1, 보조, 목표, 시작)
