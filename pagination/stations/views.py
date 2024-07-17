from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import pagination.settings
from csv import DictReader

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    num_page = int(request.GET.get('page', 1))
    with open(pagination.settings.BUS_STATION_CSV, "r", encoding='utf-8') as f:
        reader = DictReader(f)
        station = list(reader)
    paginator = Paginator(station, 10)
    page = paginator.get_page(num_page)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
