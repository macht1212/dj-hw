import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def info() -> list:
    with open("data-398-2018-08-30.csv") as f:
        rows = csv.reader(f, delimiter=",")
        raw_stations = list(rows)
        stations = []
        for station in raw_stations:
            stations.append([station[1], station[4], station[6]])

        return stations


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get("page", 1))
    info_ = info()

    paginator = Paginator(info_, 10)
    page = paginator.get_page(page_number)

    context = {
        # 'bus_stations': info(),
        'page': page,
    }
    return render(request, 'stations/index.html', context)
