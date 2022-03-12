from django.shortcuts import render
from django.http import HttpResponse

resumeList = [
    {
    'id':'1',
    'title':'водитель',
    'description':'опыт вождения 3 года'
    },
    {
    'id':'2',
    'title':'бухгалтер',
    'description':'окончил учебу РУДН'
    },
    {
    'id':'3',
    'title':'парикмахер',
    'description':'Карэ кабярэ'
    },
]

vacancyList = [
    {
    'id':'4',
    'title':'Требуется повар',
    'description':'Опыт кондитер'
    },
    {
    'id':'5',
    'title':'Требуется Няня',
    'description':'фыворол фыволрфывапдофыдв'
    },
    {
    'id':'6',
    'title':'Требуется охранник',
    'description':'фывфы дплдвфырпалырд'
    },
]


def board(request):
    page = 'board'
    context = {'page':page, 'board_resume':resumeList,'board_vacancy':vacancyList}
    return render(request, 'board/board.html', context)
    

def resume(request, pk):
    resumeObj = None
    for i in resumeList:
        if i['id'] == pk:
            resumeObj = i
    return render(request, 'board/resume.html',{'resume':resumeObj})


def vacancy(request, pk):
    vacancyObj = None
    for i in vacancyList:
        if i['id'] == pk:
            vacancyObj = i
    return render(request, 'board/vacancy.html', {'vacancy':vacancyObj})