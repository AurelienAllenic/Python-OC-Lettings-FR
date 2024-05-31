from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    Get all lettings from the database and
    render the lettings_index.html template.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Get a letting by its id and render
    the letting.html template with context.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
