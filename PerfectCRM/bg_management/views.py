from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bg_management import bgadmin
from bg_management.utils import after_filter, after_search


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
    after_filter_lists, filter_conditions = after_filter(request, admin_calss)
    after_search_lists = after_search(request, after_filter_lists, admin_calss)
    # model_lists = admin_calss.model.objects.filter()
    paginator = Paginator(after_search_lists, admin_calss.list_per_page)

    page = request.GET.get('page')
    handled_model_lists = paginator.get_page(page)

    return render(request, 'bg_management/table_obj.html', {'admin_class': admin_calss,
                                                            'filter_conditions': filter_conditions,
                                                            'app_name': app_name,
                                                            'table_name': table_name,
                                                            'handled_model_lists': handled_model_lists,
                                                            'query': request.GET.get('_q', "")})


def model_list_change(request, app_name, table_name, id):
    return render(request, 'bg_management/model_obj_change.html')
