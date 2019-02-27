from django.db import models

# Create your models here.
class Class_Model_Model1(models.Model):
    router_name = models.CharField(max_length = 60,unique=True)
    mgtIP = models.CharField(max_length = 60)
    # licenselevel = models.CharField(max_length = 60)
    version = models.CharField(max_length = 60)
    cpu = models.CharField(max_length = 60)
    cpu_frequency = models.CharField(max_length = 60)
    architecture_name = models.CharField(max_length = 60)
    board_name = models.CharField(max_length = 60)
    alive = models.CharField(max_length = 60)

    def __str__(self):
        return self.router_name
