from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext, Context
from member.models import Member
from django.shortcuts import render
from django.http import HttpResponseRedirect
from member.forms import MemberForm
# Create your views here.
import re
#import regular expressions

def member_search(request):
#    import pdb; pdb.set_trace()
    if request.method == 'POST':
        query = request.POST['search_box']
        results = Member.objects.filter(fName=query)

    
    return render(request, 'member/search_member.html',{results:results});
        
    

def member_create(request):
 #   import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = MemberForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('member_random')
    else:
        form = MemberForm()

    return render(request, 'member/create_member.html',{'form':form})



def member(request):
#    import pdb; pdb.set_trace()
    member = Member.objects.all()[0]
    context = Context({
            'member':member
            })
    template = loader.get_template('member/member.html')
    return HttpResponse(template.render(context))


