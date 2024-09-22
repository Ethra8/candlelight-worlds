from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


TIME_SLOTS = [
    ('10 am - 5 pm', '10 am - 5 pm'),
    ('7 pm - 8 am', '7 pm - 8 am'),
]

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    world = models.ForeignKey('worlds.World', on_delete=models.CASCADE, default=1)
    date = models.DateField()
    time = models.CharField(max_length=19, choices=TIME_SLOTS)

    def __str__(self):
        return f'Booking {self.id} - {self.user.username} - {self.world.display_name} - {self.date} - {self.get_time_display()}'