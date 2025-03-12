from django.db import models
from django.conf import settings

class Destination(models.Model):
    """
    Modell für ein Reiseziel.
    """
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.country}"

class Trip(models.Model):
    """
    Modell für eine Reise, die vom Benutzer geplant wird.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Trip to {self.destination.name} by {self.user.username}"

class Budget(models.Model):
    """
    Modell zur Budgetverfolgung einer Reise.
    """
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remaining = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.amount}€ for Trip {self.trip.id}"