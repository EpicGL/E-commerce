from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('store')  # Redirect to the home page after successful login
            else:
                return render(request, 'login.html', {'error_message': 'Your account is disabled.'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials.'})
    if request.user.is_authenticated:
        return redirect('store')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('store')