from django.db import models


class UsUser(models.Model):
    us_id = models.AutoField(primary_key=True)
    us_name = models.CharField(unique=True, max_length=50)
    us_email = models.CharField(max_length=50)
    us_department = models.CharField(max_length=50)
    us_roomname = models.CharField(max_length=50)
    us_roomtime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'us_user'
    def __str__(self):
        return self.us_name

class UsRoominfo(models.Model):
    us_roomname = models.CharField(max_length=40)
    us_roomtime = models.CharField(max_length=40)
    us_roompassword = models.CharField(max_length=40)
    us_use = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'us_roominfo'
    def __str__(self):
        return self.us_roomname
