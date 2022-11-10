from django.core.validators import FileExtensionValidator
from django.db import models


class Pet(models.Model):
    owner = models.ForeignKey("users.Owner", on_delete=models.CASCADE, related_name="owners")
    photo = models.ImageField()
    video = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    vaccination_plan = models.ImageField
    vaccination_observations = models.CharField(max_length=1000)
    breed = models.CharField(max_length=255)
    size = models.CharField(choices=(('sm', 'Small'),
                                     ('md', 'Medium'),
                                     ('lg', 'Large')),
                            max_length=2)