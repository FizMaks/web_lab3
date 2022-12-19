from django.shortcuts import render
from .models import Comment
from .forms import CommentForm
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def date_to_date(bad_date):
    date_list = str(bad_date).split()[0].split('-')
    date_list.reverse()
    return('.'.join(date_list))

def post_detail(request):
    template_name = 'about/about.html'
    new_comment = None

    if request.method == 'POST' and is_ajax(request):
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
            comment_form = CommentForm()
            return JsonResponse(data = {}, status=200)
    else:
        comment_form = CommentForm()
        

    return render(request, template_name, {'comment_form': comment_form})

def get_all_comms(request):
    username = request.GET.get('username', None)
    all_comms = [ {"body" : comm.body, "date" : date_to_date(comm.date_pub)} for comm in Comment.objects.all()]

    all_comms = { i : comm for i, comm in enumerate(all_comms)}

    response = {
        'len_comms' : len(all_comms),
        'all_comms': all_comms
    }
    return JsonResponse(response)