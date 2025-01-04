from django.db import models

# Create your models here.
class Kategori(models.Model):
  nama_kategori = models.CharField(max_length=30)
  def __str__(self):
    return self.nama_kategori
  

class Produk(models.Model):
  nama_produk = models.CharField(max_length=100)
  harga_produk = models.BigIntegerField()
  stok_produk = models.SmallIntegerField()
  kategori_produk = models.ForeignKey(Kategori,
                                      on_delete=models.CASCADE,
                                       related_name='produk' )
  def __str__(self):
    return self.nama_produk