from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required(login_url='logorsign')
def task_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'notes' : notes})

@login_required(login_url='logorsign')
def task_note(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'task_note.html', {'note' : note})

@login_required(login_url='logorsign')
def task_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    return redirect('home')
    

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Note
    fields = ['title', 'text']
    template_name = 'task_edit.html'
    success_url = reverse_lazy('home')


@login_required(login_url='logorsign')
def task_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.user = request.user
            notes.save()
            return redirect('home')


    else:
        form = NoteForm()
    return render(request, 'task_add.html', {'form': form})

def logorsign(request):
    return render(request, 'logorsign.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password is not correct")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')