from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Note
from django.views.generic import UpdateView, DeleteView
from .forms import NoteAddForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def note_list(request): 
    if not request.user.is_authenticated:
        return redirect('logorsign')
    notes = Note.objects.filter(user=request.user)
    return render(request, 'note_list.html', {'notes' : notes})

def note_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('logorsign')
    note = get_object_or_404(Note, pk=pk, user=request.user)
    return render(request, 'note_detail.html', {'note' : note})

def note_add(request):
    if not request.user.is_authenticated:
        return redirect('logorsign')
    if request.method == 'POST':
        form = NoteAddForm(request.POST)
        if form.is_valid():
            notes = form.save(commit=False)
            notes.user = request.user
            notes.save()
            return redirect('home')
    else:
        form = NoteAddForm()
    return render(request, 'note_add.html', {"form" : form})

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteAddForm
    template_name = "note_edit.html"
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_delete.html'
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'problemmmmmm')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)     
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'problem')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form' : form})

def logorsign(request):
    return render(request, 'logorsign.html')