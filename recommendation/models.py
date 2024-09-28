from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)


    def __str__(self) -> str:
        return self.title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "skills": list(self.skills.values_list("name", flat=True))
        }