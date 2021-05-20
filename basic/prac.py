scores = [
    {'name':'형민'},
    {'name':'정하','score':'80',},
    {'name':'미영','score':'90',},
    {'name':'용을','score':'50',},
    {'name':'승찬','score':'30',},
    {'name':'연준','score':'90',},
    {'name':'영우','score':'20',}
]




for s in scores:
    try:
        if s['score'] > 20:
            print(s['name'])
    except:
        name = s['name']
        print(f'{name} - 에러입니다')