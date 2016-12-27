from django.shortcuts import render
from django.http import HttpResponse
from .models import ETab, AboutMe_Link, WorkExperience, CasualExperience, skill_list


# Create your views here.
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {
        'pageowner': "Jesmigel A. Cantos",
        'role': "Analyst / Programmer",
        'etab_list': ETab.objects.all(),
        'contents_aboutme': AboutMe_Link.objects.all(),
    }



    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'index.html', context_dict)
