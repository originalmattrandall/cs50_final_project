from django.shortcuts import render
from django.http import JsonResponse
from .models import Sale, User

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


def data_management(request):
    """ Page provides crud operations for sales data """
    return render(request, 'sales_performance/data_management.html', {'title': 'Data Management'})


def data_visualization(request):
    """ Provies visualization options to the user for their sales data """

    results = Sale.objects.all()
    all_users = User.objects.all()

    labels = [user.username for user in all_users]

    context = {
        'title': 'Data Visualization',
        'sales': Sale.objects.all(),
        'labels': labels
    }
    return render(request, 'sales_performance/data_visualization.html', context)


def chart_data(request):
    """ description """
    all_users = User.objects.all()

    labels = [user.username for user in all_users]

    return JsonResponse(
        data={
            'name': 'Sales',
            'labels': labels,
            'sales': [23, 67]
        }
    )
