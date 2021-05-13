from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Skateteam, Teamcat


# Create your views here.


def skateteam(request):

    skateteam = Skateteam.objects.all()

    context = {
        'skateteam': skateteam,
    }

    return render(request, 'skateteam/skateteam.html', context)


def sdetail(request, memeber_id):
    """ A view to show individual product details """

    memeber = get_object_or_404(Skateteam, pk=memeber_id)

    context = {
        'memeber': memeber,
    }

    return render(request, 'skateteam/sdetail.html', context)
