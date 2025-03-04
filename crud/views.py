from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request,'listingpage.html',{'users':users})
# new
def add_user(request):
    mydict={}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form'] = form
    return render(request,'add.html',mydict)
def edit_user(request,id=None):
    one_record = User.objects.get(pk=id)
    form = UserForm(request.POST or None,instance=one_record)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict={'form':form}
    return render(request,'edit.html',mydict)
def delete_user(request,id=None):
    one_record = User.objects.get(pk=id)
    if request.method == 'POST':
        one_record.delete()
        return redirect('/')
    return render(request,'delete.html',{'form':one_record})
def view_user(request,id=None):
    mydict={}
    one_record = User.objects.get(pk=id)
    mydict['user']=one_record
    return render(request,'view.html',mydict)

