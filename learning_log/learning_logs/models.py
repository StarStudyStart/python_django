from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """返回模型字符串的表示"""
        return self.text
        
class Entry(models.Model):
    """主题下的内容条目"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """返回模型的字符串表示"""
        text = ''
        if len(self.text) < 50:
            text = self.text
        else:
            text = self.text[:50] + '...'
            
        return text
        
    
