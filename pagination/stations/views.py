import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        csv_dict = DictReader(f)
        pagination = Paginator(list(csv_dict), per_page=10)
    page = pagination.get_page(page_number)
    context = dict(bus_stations=page.object_list, page=page)
    return render(request, 'stations/index.html', context)
