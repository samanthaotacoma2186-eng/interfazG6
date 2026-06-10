from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def hola(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def donation(request):
    return render(request, 'donation.html')

def event(request):
    return render(request, 'event.html')

def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    mensaje = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        print("Usuario:", user, "- Autenticado:", user is not None)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            mensaje = "Credenciales incorrectas"

    return render(request, 'login.html', {'mensaje': mensaje})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = UserCreationForm(request.POST or None)
    mensaje = ''

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/dashboard/')
            return redirect('login')
        mensaje = 'Corrige los errores del formulario.'

    return render(request, 'register.html', {'form': form, 'mensaje': mensaje})
