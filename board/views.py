from django.shortcuts import render
from django.http import HttpResponse





def board(request):
    return render(request, 'board/board.html')

def resume(request, pk):
    return render(request, 'board/resume.html')

def vacancy(request, pk):
    return render(request, 'board/vacancy.html')