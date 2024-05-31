from django.shortcuts import render

def index(request):
    """
    Render the index.html template.
    """
    return render(request, 'oc_lettings_site/index.html')


def handle_404(request, exception):
    """
    Render the 404.html template.
    """
    print('on passe par la view')
    return render(request, 'oc_lettings_site/404.html', status=404)


def handle_500(request):
    """
    Render the 500.html template.
    """
    return render(request, 'oc_lettings_site/500.html', status=500)


def get_500(request):
    # Ligne ajoutée pour provoquer une erreur 500
    print('on passe par la view')
    raise Exception("Ceci est une erreur 500 test.")
