from django.shortcuts import render
from .models import Skateteam


# Create your views here.


def skateteam(request):

    skateteam = Skateteam.objects.all()

    context = {
        'skateteam': skateteam,
    }

    return render(request, 'skateteam/skateteam.html', context)
