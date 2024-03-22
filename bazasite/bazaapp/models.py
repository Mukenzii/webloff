from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255,unique=True,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Article(models.Model):
    title = models.CharField(max_length=255,unique=True, null=True,blank=True)
    description = models.TextField()
    link = models.CharField(max_length=255, unique=True,null=True,blank=True)
    photo = models.ImageField(blank=True,null=True,upload_to='photos/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kontent"
        verbose_name_plural = "Kontentlar"