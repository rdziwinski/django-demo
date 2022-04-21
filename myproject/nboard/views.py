from django.shortcuts import render
from django.views import generic
from .models import Notice


class NoticeBoard(generic.ListView):
    context_object_name = 'notices'
    template_name = 'index.html'

    queryset = Notice.objects.order_by('-created_on')

class NoticeDetail(generic.DetailView):
    model = Notice
    template_name = 'notice.html'

