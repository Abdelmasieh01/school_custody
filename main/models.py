from django.db import models

class Item(models.Model):
    name = models.CharField(unique=True, max_length=150, verbose_name='اسم العهدة')
    count = models.PositiveSmallIntegerField(verbose_name='العدد')

    def __str__(self):
        return self.name + ': ' + str(self.count)

class Reqeust(models.Model):
    name = models.CharField(unique=True, max_length=150, verbose_name='اسم المستلم: ')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='اختر العهدة: ')
    count = models.PositiveSmallIntegerField(verbose_name='العدد')
    date = models.DateField(verbose_name='تاريخ الطلب', null=True)

    def __str__(self):
        return self.name + ' - ' + self.item.name + ': ' + str(self.item.count)