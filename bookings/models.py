from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


TIME_SLOTS = [
    ('10:00', '10:00 AM - 04:00 PM'),
    ('18:00', '06:00 PM - 08:00 AM'),
]

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.CharField(max_length=5, choices=TIME_SLOTS)
    world = models.ForeignKey('worlds.World', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'Booking {self.id} - {self.user.username} - {self.world.display_name} - {self.date} - {self.get_start_time_display()}'