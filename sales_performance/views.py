from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.db.models import Sum
from django.views.generic import CreateView
from django.contrib import messages
from .models import Sale, User
from random import randrange
from datetime import datetime, timedelta

import csv, io

cards = [
    {
        'title': 'Visualizations',
        'content': 'Visual your sales data.',
        'button': 'Show me my data',
        'link': '/data-visualization'
    },
    {
        'title': 'Data Management',
        'content': 'Create/Update new and existing data.',
        'button': 'Take me to my data',
        'link': '/data-management'
    }
]


def home(request):
    """ Load the home page of the site """
    context = {
        'cards': cards,
    }
    return render(request, 'sales_performance/home.html', context)


# TODO: apply permission_required in a real world app
def data_management(request):
    """ Page provides crud operations for sales data """

    template = 'sales_performance/data_management.html'

    context = {
        'title': 'Data Management',
        'order': 'Order of csv should be title, desc, sale_amount'
    }

    if request.method == 'GET':
        return render(request, template, context)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'must be a .csv file')
        return render(request, template, context)
    
    # Read in the csv file
    data_set = csv_file.read().decode('UTF8')
    io_string = io.StringIO(data_set)

    # Skip the header line
    next(io_string)

    # TODO: future release must allow date and sales associate to be passed in via csv
    # For simplicity we are going to generate a random date range to assign the sale to
    # we are also going to just select a random User to assign as the sales associate
    d1 = datetime.strptime('1/1/2010 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2020 4:50 AM', '%m/%d/%Y %I:%M %p')

    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Sale.objects.update_or_create(
            title=column[0],
            desc=column[1],
            sale_amount=column[2],
            sale_date=random_date(d1, d2),
            # For simplicity just grab a random user
            sales_person=User.objects.order_by('?').first()
        )
    
    return render(request, template, context)


def data_visualization(request):
    """ Provies visualization options to the user for their sales data """

    context = {
        'title': 'Data Visualization',
    }
    return render(request, 'sales_performance/data_visualization.html', context)


def chart_data(request):
    """ get all users and there total sales """

    labels = User.objects.all()

    sales = [
        Sale.objects.filter(sales_person=label).aggregate(Sum('sale_amount'))['sale_amount__sum'] or 0 
        for label in labels
    ]

    return JsonResponse(
        data={
            'name': 'Sales',
            'labels': [user.username for user in labels],
            'sales': sales
        }
    )


class SaleCreateView(CreateView):
    model = Sale
    # 2009-06-15T13:45:30
    fields = [
        'title',
        'desc',
        'sale_amount',
        'sale_date',
        'sales_person'
    ]

    def get_success_url(slef):
        return reverse('sales-performance-data-management')


def random_date(start, end):
    """ calculate a random datetime between two given dates. """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
