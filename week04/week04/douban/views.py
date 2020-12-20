from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Movie, Comment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def movie_comment(request, mid):
    """
    返回指定电影的评论、星级、日期
    """
    query_set = Movie.objects.filter(mid=mid)
    if len(query_set) == 0:
        return HttpResponseNotFound("404 页面没有发现，检查输入的URL是否正确")

    # 电影名
    movie_name = query_set[0].name

    # 评论
    if request.method == "GET":
        comment = Comment.objects.filter(mid=mid)
    elif request.method == "POST":
        q = request.POST.get('q')
        comment = Comment.objects.filter(mid=mid).filter(comment__contains=q)
    
    #comment = Comment.objects.filter(mid=mid)
    for item in comment:
        item.date = item.date.strftime('%Y-%m-%d')

    return render(request, 'index.html', locals())