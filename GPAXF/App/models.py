from django.db import models


class Carousel(models.Model):
    """
        axf_wheel(img,name,trackid)
    """
    img = models.CharField(max_length=500)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField(default=1)

    class Meta:
        db_table = 'carousel'