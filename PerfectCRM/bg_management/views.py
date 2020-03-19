from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from bg_management import bgadmin
from bg_management.utils import after_filter, after_search
from bg_management.forms import create_model_form


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
    """更新数据表"""
    admin_class = bgadmin.enabled_admins[app_name][table_name]
    model_form_class = create_model_form(admin_class)
    obj = get_object_or_404(admin_class.model, id=id)

    if request.method != 'POST':
        # 显示原有数据
        dynamic_forms = model_form_class(instance=obj)
    else:
        # 对比数据库中的数据，并更新
        dynamic_forms = model_form_class(request.POST, instance=obj)
        if dynamic_forms.is_valid():
            dynamic_forms.save()

    return render(request, 'bg_management/model_obj_change.html', {'forms': dynamic_forms, })
