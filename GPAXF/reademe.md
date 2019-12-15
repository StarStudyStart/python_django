## 注意事项
- bloc.super
    -
    ```
    home.html中
    {% extends 'axf/base_main.html' %}
    {% load static %}
    {% block ext_css %}
        {{ block.super }}  
        <link rel="stylesheet" href="{% static 'axf/main/css/home.css' %}">
    {% endblock %}
    
    {% block ext_js %}
        {{ block.super }}
        <script type="text/javascript" src="{% static 'axf/js/swiper.jquery.js' %}"></script>
    {% endblock %}
    ```
    - ext_css是base.html中的占位符;
    - home中继承的是base_main.html，一定要使用block.super将base_main的定义样式继承过来
    否则只有最新加载的了base_main.html的渲染效果就会丢失
    - 官方解释 如果想要在父block中新增内容而不是完全覆盖它，这将非常有用。使用{{ block.super }} 插入的数据不会被自动转义，因为父模板中的内容已经被转义。