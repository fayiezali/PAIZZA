from django.db import models
from django.contrib.auth.models import User
import uuid

class BaseModel(models.Model): 
    uid        = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4)
    created_at  = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    class Meta:
        abstract = True
    
        # 'admin'display the field name on a page
    def __str__(self):
        return str(self.uid)  + ' ' +  str(self.created_at)  + ' ' + str(self.updated_at)


class PizzaCategory(BaseModel):
    category_name = models.CharField(max_length=100)
        # 'admin'display the field name on a page
    def __str__(self):
        return self.category_name


class Pizza(BaseModel):
    category   = models.ForeignKey(PizzaCategory , on_delete=models.CASCADE , related_name="pizzas")
    pizza_name = models.CharField(max_length=100)
    price      = models.IntegerField(default=100)
    images    = models.ImageField(upload_to='pizza')

    # 'admin'display the field name on a page
    def __str__(self):
        return self.pizza_name


class Cart(BaseModel):
    user   = models.ForeignKey(User , null=True , blank=True, on_delete=models.SET_NULL , related_name="carts")
    # user   = models.ForeignKey(User ,  on_delete=models.SET_NULL , related_name="carts")
    is_paid = models.BooleanField(default=False)
    
        # 'admin'display the field name on a page
    def __str__(self):
        return 'User Name:' + str(self.user) + '_____' + 'Is Paid:' +  str(self.is_paid)

    # def get_cart_total(self):
    #     return CartItems.objects.filter(cart = self).aggregate(Sum('pizza__price'))['pizza__price_sum']

class CartItems(BaseModel):
    cart  = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name="cart_items")
    pizza = models.ForeignKey(Pizza , on_delete=models.CASCADE )

    # 'admin'display the field name on a page
    def __str__(self):
        return str(self.pizza)

