from django.db import models


class Main(models.Model):
    """img,name,trackid"""

    img = models.CharField(max_length=500)
    name = models.CharField(max_length=64)
    trackid = models.BigIntegerField(default=1)

    class Meta:
        abstract = True


class Carousel(Main):
    """
        axf_wheel(img,name,trackid)
    """

    class Meta:
        db_table = 'carousel'


class MainNav(Main):
    """
        market_nav(img,name,trackid)
    """

    class Meta:
        db_table = 'market_nav'


class MainHot(Main):
    """
        market_hot(img,name,trackid)
    """

    class Meta:
        db_table = 'market_hot'
