from django.shortcuts import render
from django.views import generic
from generic_view.models import Publisher, Book
from django.shortcuts import get_object_or_404


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


class BookList(generic.ListView):
    """查询特定对象的子集 self.object_list"""
    # queryset = Book.objects.all()
    queryset = Book.objects.filter(author__last_name='yabin')
    template_name = 'generic_view/book_list.html'
    context_object_name = 'book_list'


class PublisherBookList(generic.ListView):
    """根据url动态查询对象的子集 self.object_list"""
    # queryset = Book.objects.all()
    template_name = 'books_by_publisher.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        self._publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self._publisher)

    def get_context_data(self, *, object_list=None, **kwargs):
        """将publisher添加到上下文，传递给模板"""
        context = super().get_context_data(**kwargs)
        context['publisher'] = self._publisher
        return context
