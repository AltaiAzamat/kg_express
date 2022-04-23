from django.db import models

# Create your models here.
# PRODUCT MODELS

class Category(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("слаг", max_length=60, unique=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ['name']
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="sabcategory"
    )
    name = models.CharField("название", max_length=70, unique=True)
    slug = models.SlugField("слаг", max_length=80, unique=True)

    class Meta:
        verbose_name = "под категория"
        verbose_name_plural = "подкатегории"
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("навание",max_length=225)
    descriptions = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10,decimal_places=2)
    image = models.ImageField("фото", upload_to = "product_images/")
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory,on_delete= models.PROTECT,related_name="products")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("активный", default=True)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
        ordering = ['-created']

    def __str__(self):
        return  self.name