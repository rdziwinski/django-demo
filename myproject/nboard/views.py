from django.shortcuts import render
from django.views import generic
from .models import Notice


class NoticeBoard(generic.ListView):
    context_object_name = 'notices'
    template_name = 'index.html'

    def get_queryset(self):
        notices = {
            'future': Notice.objects.filter(status=0).order_by('-created_on'),
            'inprogress': Notice.objects.filter(status=1).order_by('-created_on'),
            'archive': Notice.objects.filter(status=2).order_by('-created_on'),
        }
        return notices


class NoticeDetail(generic.DetailView):
    model = Notice
    template_name = 'notice.html'

