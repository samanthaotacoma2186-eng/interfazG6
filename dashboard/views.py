from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def dashboard(request):
    return HttpResponse(
        f"Usuario: {request.user.username} - Autenticado: {request.user.is_authenticated}"
    )