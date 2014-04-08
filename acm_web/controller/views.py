# Create your views here.
from django.http import HttpResponse
from django.template import loader, RequestContext, Context
from controller.models import Visits

import re

def home(request):
    template = loader.get_template('controller/index.html')
    count = Visits.incrementVisitCount('index')
    context = Context({
            'views':count
            })
    return HttpResponse(template.render(context))

def page(request):
    #    import pudb; pudb.set_trace()
    path = request.path[1:]
    count = Visits.incrementVisitCount('%s' % path[1:])
    template = loader.get_template('controller/%s' % path)
    
    context = Context({
            'views':count,
            'hasname': 0
            })
    if request.GET.get("firstname"):
        context['firstname'] = request.GET.get("firstname")
        context['lastname'] = request.GET.get("lastname")
        context['hasname'] =  1

    return HttpResponse(template.render(context))

def test(request):
    from datetime import datetime
    
    viewcount = Visits.incrementVisitCount('test')

    Date = str(datetime.now())
    template = loader.get_template('controller/test.psp')
    context = Context({
            'Date':Date,
            'viewCount':viewcount
            })
    return HttpResponse(template.render(context))

from django.shortcuts import render
from django.http import HttpResponseRedirect
from controller.forms import MemberForm
def member(request):
    if request.method =='POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = MemberForm()
        
    return render(request, 'controller/roster-edit.html',{'form':form})
