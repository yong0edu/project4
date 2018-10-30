from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def insert(request):
    for i in range(1, 1001): # 게시물 1000개 입력
        Board.objects.create(title='제목 ' + str(i), content='내용 ' + str(i))
    return HttpResponse('insert 1000')

def board_list(request):
    now_page = request.GET['page']
    board_list = Board.objects.order_by('-id')
    paginator = Paginator(board_list, 10)
    page_info = paginator.page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 10

    page_range=range(start_page, end_page)
    return render(request,
                  'pagination/list.html',
                  {'page_info':page_info,
                   'page_range':page_range})