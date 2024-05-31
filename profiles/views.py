from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Get all profile objects and call the index.html
    template with the profiles_list context.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Get a profile by its username and render
    the profile.html template with the profile context.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
