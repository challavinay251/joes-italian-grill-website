from django.db import models
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"


class EventBooking(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    EVENT_TYPES = [
        ("birthday", "Birthday Party"),
        ("anniversary", "Anniversary"),
        ("corporate", "Corporate Event"),
        ("private", "Private Party"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    event_date = models.DateField()
    event_time = models.TimeField()

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    guests = models.CharField(max_length=50)

    need_catering = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event_type} ({self.status})"