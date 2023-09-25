from django.db import models

class Movie(models.Model):
    name = models.TextField()
    year = models.TextField()
    genre = models.TextField()

    def __str__(self):
        return self.name

class Attend(models.Model):
    ATTN_Number = models.IntegerField()
    Movie_Name = models.TextField()  # This should be related to the Movie model
    Seat_Number = models.TextField()
    Show_Time = models.TextField()

    def __str__(self):
        return f"Attendance {self.ATTN_Number} for {self.Movie_Name}"
