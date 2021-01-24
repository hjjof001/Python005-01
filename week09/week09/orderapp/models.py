from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    ORDER_STATUS = (
        (1, "New"),
        (2, "Cancelled")
    )

    product_id = models.CharField(max_length=64)
    buyer = models.ForeignKey(
        'auth.User', related_name='orders', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=ORDER_STATUS, default=1)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.product_id
