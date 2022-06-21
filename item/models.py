from django.db import models

# Create your models here.
class item(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    item_name=models.CharField(max_length=255)
    item_price=models.FloatField()


    class Meta:
        db_table="item"