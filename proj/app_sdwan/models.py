from django.db import models

# Create your models here.
class ClassModel_Router_Basicinfo(models.Model):
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

class ClassModel_Router_Register(models.Model):
    routerip = models.CharField(max_length = 60,unique = True)
    username = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)

    def __str__(self):
        return self.routerip


class ClassModel_Router_pingresult(models.Model):
    mgtIP = models.CharField(max_length = 60)
    username = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)
    router_name = models.CharField(max_length = 60)
    success = models.CharField(max_length = 60)
    destinationIP = models.CharField(max_length = 60)
    packet_loss = models.CharField(max_length = 60)
    rtt_min = models.CharField(max_length = 60)
    rtt_avg = models.CharField(max_length = 60)
    time = models.CharField(max_length = 60,unique=True)

    def __str__(self):
        return self.router_name + self.destinationIP+self.time
