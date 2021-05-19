from django.shortcuts import render
from .forms import AddItem

# Create your views here.
def add_view(request):
    form=AddItem()
    if request.method=='POST':
        form=AddItem(request.POST)
        if form.is_valid():
            item=form.cleaned_data['item']
            quantity=form.cleaned_data['quantity']
            request.session[item]=quantity

    return render(request,'sessiondata/additem.html',{'form':form})

def dispaly_view(request):
    return render(request,'sessiondata/display.html')