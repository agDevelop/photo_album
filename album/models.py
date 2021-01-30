from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    size = models.ForeignKey('Size', null=True, on_delete= models.PROTECT)
    binding = models.ForeignKey('Binding', null=True, on_delete= models.PROTECT)
    template = models.ForeignKey('Template', null=True, on_delete= models.PROTECT)
    description = models.TextField(blank=True)
    pages = models.IntegerField()


    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.size


class Binding(models.Model):
    binding = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.binding


class Template(models.Model):
    template = models.CharField (max_length=40, db_index=True)
    def __str__(self):
        return self.template



