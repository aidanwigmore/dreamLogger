from dreams.models import Dream
from dreams.forms import DreamForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

def dream_index(request):
    # Show list of dreams
    dreams = Dream.objects.all()
    return render(request, 'dream_index.html', {'dreams': dreams})

def dream_create(request):
    if request.method == 'POST':
        form = DreamForm(request.POST)
        if form.is_valid():
            dream = form.save()
            return redirect('dream_detail', pk=dream.pk)
    else:
        form = DreamForm()
    return render(request, 'dream_create.html', {
        'form': form,
    })

def dream_detail(request, pk):
    # Show a specific dream
    dream = get_object_or_404(Dream, pk=pk)
    return render(request, 'dream_detail.html', {'dream': dream})

def dream_delete(request, pk):
    dream = get_object_or_404(Dream, pk=pk)
    if request.method == 'POST':
        dream.delete()
        return redirect('dream_index')
    return redirect('dream_detail', pk=pk)