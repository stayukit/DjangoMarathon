from django.db import models
from django.utils import safestring, timezone


class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='ชื่อสินค้า')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    categories = models.ManyToManyField(Categorie, related_name='products')
    created_at = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, null=True, blank=True)

    @property
    def _title(self):
        return self.name

    def __str__(self):
        return self._title
    
class ProductStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    instock = models.DecimalField(default=1, max_digits=10, decimal_places=2)
    sold = models.DecimalField(default=1, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + ' (instock: {} sold: {})'.format(self.instock, self.sold)

class Staff(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class CustomerForm(models.Model):
    name = models.CharField(max_length=200, verbose_name='ชื่อผู้ถาม (name)')
    title = models.CharField(max_length=200, verbose_name='ประเภทปัญหา')
    detail = models.TextField(null=True, blank=True, verbose_name='รายละเอียด')
    email = models.CharField(max_length=200, verbose_name='อีเมลสำหรับติดต่อกลับ')
    done = models.BooleanField(default=False, verbose_name='ปัญหาแก้ปัญหาจบแล้วหรือไม่')
    summary = models.TextField(null=True, blank=True, default='', verbose_name='สรุปปัญหา วิธีแก้ไข')
    created_at = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now = True, null=True, blank=True)

    @property
    def _title(self):
        # local_created_at = timezone.localtime(self.created_at).strftime("%Y-%m-%d %H:%M:%S.%f")
        # string = safestring.mark_safe('[{}]&ensp;{}'.format(local_created_at ,self.title))
        string = '{} - จากคุณ: {}'.format(self.title, self.name)
        return string

    def __str__(self):
        return self._title

