from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from generic_view.models import Publisher, Book
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PublisherList(generic.ListView):
    """标准通用视图"""
    model = Publisher
    context_object_name = 'other_list'


class PublisherDetail(generic.DetailView):
    """Detail必须从url中接收一个关于模型字段的命名组，根据这个条件返回查询结果self.object"""
    model = Publisher

    # 添加额外的上下文
    def get_context_data(self, **kwargs):
        # 首先继承父类的上下文环境
        context = super().get_context_data(**kwargs)
        # 然后合并上下文返回
        context['book_list'] = Book.objects.all()
        return context

    # 额外的工作
    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj


class BookList(LoginRequiredMixin, generic.ListView):
    login_url = '/users/login/'
    redirect_field_name = 'my_redirect_field'
    """查询特定对象的子集 self.object_list"""
    # queryset = Book.objects.all()
    queryset = Book.objects.filter(author__last_name='yabin')
    template_name = 'generic_view/book_list.html'
    context_object_name = 'book_list'


class PublisherBookList(generic.ListView):
    """根据url动态查询对象的子集 self.object_list"""
    # queryset = Book.objects.all()
    template_name = 'generic_view/books_by_publisher.html'
    context_object_name = 'book_list'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])

    def get_queryset(self):
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, *, object_list=None, **kwargs):
        """将publisher添加到上下文，传递给模板"""
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context
