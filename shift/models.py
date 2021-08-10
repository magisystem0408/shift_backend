from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField('カテゴリ', max_length=15)

    def __str__(self):
        return self.title


class ShiftBoard(models.Model):
    # category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT, blank=False,
    #                              related_name='category'
    #                              )
    #
    categorys_choice =(
        ('施工','施工'),
        ('コンサル','コンサル'),
        ('記念日','記念日'),
         )
    category =models.CharField(verbose_name="カテゴリー", choices=categorys_choice, max_length=10)
    count = models.IntegerField(verbose_name='件数', blank=False)
    date = models.DateField(verbose_name='日程', null=False, blank=False)
    release =models.BooleanField(verbose_name='公開中',null=False,blank=False,default=False)

    def __str__(self):
        return str(self.date) + "：" +str(self.category)
