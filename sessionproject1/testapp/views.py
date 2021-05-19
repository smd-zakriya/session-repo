from django.shortcuts import render

# Create your views here.
def cookie_count_view(request):
    cookie_count=int(request.COOKIES.get('count',0))
    cookie_newcount=cookie_count+1
    response=render(request,'index.html',{'c_count':cookie_newcount})
    response.set_cookie('count',cookie_newcount)
    return response

def session_count_view(request):
    session_count=request.session.get('count',0)
    session_newcount=session_count+1
    request.session['count']=session_newcount
    return render(request,'index2.html',{'s_count':session_newcount})
