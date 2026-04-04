from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"

class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='products', 
        verbose_name="Kategoriya"
    )
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    desc = models.TextField(blank=True, verbose_name="Tavsif")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Narxi")
    stock = models.PositiveIntegerField(default=0, verbose_name="Ombordagi soni")
    is_available = models.BooleanField(default=True, verbose_name="Sotuvda bor")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Mahsulot"

    def __str__(self):
        return self.name