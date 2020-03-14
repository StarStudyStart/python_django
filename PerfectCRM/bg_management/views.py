from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bg_management import bgadmin
from bg_management.utils import after_filter


# Create your views here.
def index(request):
    """所有表"""
    admins = bgadmin.enabled_admins
    print(bgadmin.enabled_admins['crm']['customer'].model)
    return render(request, 'bg_management/index.html', {'admins': admins})


def model_list(request, app_name, table_name):
    """表单字段显示"""
    admins = bgadmin.enabled_admins
    admin_calss = admins[app_name][table_name]
    model_lists, filter_conditions = after_filter(request, admin_calss)
    # model_lists = admin_calss.model.objects.filter()
    paginator = Paginator(model_lists, admin_calss.list_per_page)

    page = request.GET.get('page')
    model_pages = paginator.get_page(page)

    return render(request, 'bg_management/detail.html', {'admin_class': admin_calss,
                                                         'model_lists': model_lists,
                                                         'filter_conditions': filter_conditions,
                                                         'app_name': app_name,
                                                         'table_name': table_name,
                                                         'model_pages': model_pages, })
