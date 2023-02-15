from django.db import models


class Items(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField('Items')
    total_price = models.FloatField()

    def __str__(self):
        return f'Заказ №{self.id} на сумму: {self.total_price}'

    def get_total_price(self):
        summ = 0
        for item in self.items:
            summ += item.price
        return summ

    def save(self, *args, **kwargs):
        print('SAVE!!!!!!!!!!!!')
        super().save(*args, **kwargs)
        print('PAST SAVE**************')
        print(self.items)
