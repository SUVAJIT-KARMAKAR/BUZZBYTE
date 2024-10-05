# BUZZ -> VIEWS.PY
from django.shortcuts import render
from .models import Buzz
from .forms import BuzzForm
from django.shortcuts import get_list_or_404, redirect

def index(request):
    return render(request, 'index.html')

# LIST ALL BUZZ
def buzz_list(request):
    buzzes = Buzz.objects.all().order_by('-created_at')
    return render(request,'buzz_list.html', {
        'buzzes' : buzzes
    })

# CREATE BUZZ
def buzz_crete(request) : 
    if request.method == "POST" : 
        form = BuzzForm(request.POST, request.FILES)
        if form.is_valid() :
            buzz = form.save(commit=False)
            buzz.user = request.user
            buzz.save()
            return redirect('buzz_list')
        else : 
            form = BuzzForm()
        return render(request, 'buzz_form.html', {
            'form' : form 
        })


# EDIT BUZZ 
def buzz_edit(request, buzz_id) : 
    buzz = get_list_or_404(Buzz, key=buzz_id, user = request.user)
    if request.method == "POST" : 
        form = BuzzForm(request.POST, request.FILES, instance=buzz)
        if form.is_valid() : 
            buzz = form.save(commit=False)
            buzz.user = request.user
            buzz.save()
            return  redirect('buzz_list')
        else :
            form = BuzzForm(instance=buzz)
        return render(request, 'buzz_form.html', {
            'form' : form 
        })

# DELETE BUZZ 
def buzz_delete(request, buzz_id) : 
    buzz = get_list_or_404(Buzz, key=buzz_id, user=request.user)
    if request.method == "POST" : 
        buzz.delete()
        return redirect('buzz_list')
    return render(request, 'buzz_confirm_delete.html', {
        'buzz' : buzz
    })