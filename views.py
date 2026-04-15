from django.shortcuts import render, redirect
from .main.forms import QuickContactForm

def home_view(request):
    if request.method == 'POST':
        form = QuickContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Повертаємо користувача на головну після відправки
    else:
        form = QuickContactForm()
    
    return render(request, 'index.html', {'form': form})