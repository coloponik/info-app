from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    descrip = models.TextField()
    temp = models.TextField()
    hum = models.TextField()
    pressure = models.TextField()
    icon = models.URLField()
    time = models.DateTimeField(auto_now=True)

    def __srt__(self):
        return self.name, self.descrip, self.temp, self.hum, self.pressure, self.icon, self.time