from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(blank=False, unique=True)
    liked_shops = models.ManyToManyField('Shop', related_name='liked_by')
    disliked_shops = models.ManyToManyField('Shop', through='UserShop', related_name='disliked_by')


class Shop(gis_models.Model):
    name = gis_models.CharField(max_length=200)
    location = gis_models.PointField()
    poster = gis_models.URLField(default='https://www.jumblebee.co.uk/site/wp-content/uploads/2014/06/JB-FE-Shop_10.png')


class UserShop(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, related_name='user_shop')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_shop')
    disliked_at = models.DateField()

