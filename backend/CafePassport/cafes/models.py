from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

class Cafe(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="cafes/logos/", blank=True, null=True)

    def __str__(self):
        return self.name


class Passport(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="passport"
    )
    cafes = models.ManyToManyField("Cafe", through="PassportCafe", related_name="passports")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Passport"


class PassportCafe(models.Model):
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE, related_name="passport_cafes")
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="cafe_passports")
    rating = models.PositiveSmallIntegerField(null=True, blank=True)  # 1–5 stars maybe
    bio = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("passport", "cafe")  # prevent duplicate entries

    def __str__(self):
        return f"{self.passport.user.username} → {self.cafe.name} (Rating: {self.rating})"
