from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.name


class Product(BaseModel):
    title = models.CharField(max_length=100, verbose_name="Tovar nomi", blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Tovar narxi')
    discount_percent = models.PositiveSmallIntegerField(verbose_name="Chegirma foizi")
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoria")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def discounted_price(self):
        return float(self.price) * (1 - self.discount_percent / 100)

    def __str__(self):
        return self.title


class Contact(BaseModel):
    GENDER_CHOISE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOISE, default='M')
    image = models.FileField(upload_to="contact_images/", blank=True, null=True)

    def __str__(self):
        return self.name


class Bucket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class BucketProduct(BaseModel):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class Rating(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

