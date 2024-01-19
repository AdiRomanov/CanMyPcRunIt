from django.shortcuts import render


# Create your views here.
def index(request, *args, **kwargs):
    """
    Funcția care returnează șablonul pentru pagina principală.

    Args:
        request: Obiectul cererii HTTP.
        *args: Argumente suplimentare (nu sunt utilizate în acest caz).
        **kwargs: Argumente cheie suplimentare (nu sunt utilizate în acest caz).

    Returns:
        HttpResponse: Răspunsul HTTP care afișează șablonul pentru pagina principală.
    """
    return render(request, 'frontend/index.html')
