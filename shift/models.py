from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField('カテゴリ', max_length=15)

    def __str__(self):
        return self.title


class ShiftBoard(models.Model):
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT, blank=False)
    count = models.IntegerField(verbose_name='件数', blank=False)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return str(self.date) + "：" +str(self.category)
