from django.shortcuts import render
from bg_management import bgadmin
# Create your views here.
def index(request):
    admins = bgadmin.enabled_admins
    print(bgadmin.enabled_admins['crm']['customer'].model)
    return render(request,'bg_management/index.html', {'admins':admins})