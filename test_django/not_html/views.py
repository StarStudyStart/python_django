from django.shortcuts import render
from django.http import HttpResponse
from generic_view.models import Publisher

import os
from io import BytesIO
import csv
from reportlab.pdfgen import canvas

UNRULY_PASSENGERS = [146, 184, 235, 200, 226, 251, 299, 273, 281, 304, 203]
PARENT_DR = os.path.dirname(os.path.abspath(__file__))


# Create your views here.

def my_image(request):
    image_data = open(os.path.join(PARENT_DR, '404.jpg'), 'rb').read()
    response = HttpResponse(image_data, content_type='image/jpg')
    return response


def my_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=unruly.csv"
    response['Cache-Control'] = "No-cache"
    writer = csv.writer(response)
    writer.writerow(['year', 'Unruly Airline passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])

    return response


def my_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    temp = BytesIO()

    p = canvas.Canvas(temp)
    # publishers = Publisher.objects.order_by('-name')
    p.drawString(100, 100, 'hello world')
    p.showPage()
    p.save()

    response.write(temp.getvalue())
    return response


def my_zipfile(request):
    pass


def my_tarfile(request):
    pass


def my_pil(request):
    pass
