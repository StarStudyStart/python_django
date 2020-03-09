from django.shortcuts import render
from django.template import RequestContext
from django.template import loader, Template
from django.http import HttpResponse


# Create your views here.
def custom_proc(request):
    return {
        'app': "My app",
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
    }


def request_context_test1(request):
    t = Template('{{ user }}: {{ ip_address }}')
    # t = loader.get_template('advance_template/show_request_info.html')
    # request_context = RequestContext(request, {'message': "I'm view1"},[custom_proc])
    context = {'messages': 'This is View1', 'name':'<b>yabin'}
    return render(request,'advance_template/show_request_info.html', context)


def request_context_test2(request):
    t = loader.get_template('advance_template/show_request_info.html')
    c = {'messages': 'This is View2'}
    return HttpResponse(t.render(c))
