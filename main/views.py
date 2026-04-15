from django.shortcuts import render, redirect
from django.http import JsonResponse 
from .forms import QuickContactForm

def home_view(request): 
    if request.method == 'POST':
        form = QuickContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success'})
            
            return redirect('home')
    else:
        form = QuickContactForm()
    
    return render(request, 'main/index.html', {'form': form})