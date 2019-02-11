from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


def productFile(instance, filename):
    return '/'.join(['products', str(instance.id), filename])

class Movie(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField( upload_to= productFile, max_length=254, blank=True, null=True)
    description = models.CharField(max_length=300, default='SOME STRING')
    fantasy = models.CharField(max_length=32, default='SOME STRING')
    romance = models.CharField(max_length=32, default='SOME STRING')
    action = models.CharField(max_length=32, default='SOME STRING')
    director = models.CharField(max_length=32, default='SOME STRING')


    def avg_rating(self):
        sum = 0
        all_ratings = Rating.objects.filter(movie=self)
        for rating in all_ratings:
            sum += rating.stars

        if len(all_ratings) > 0:
            return sum / len(all_ratings)
        else:
            return 0


    def no_of_ratings(self):
        all_ratings = Rating.objects.filter(movie=self)
        return len(all_ratings)

    def productFile(instance, filename):
        return '/'.join(['products', str(instance.id), filename])


class Rating(models.Model):
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
