from django.db import models

class user(models.Model):
    name = models.charfield(max_length=20)
    greetings_1 = models.charfield(max_length=5)
    greetings_2 = models.charfield(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.name
    
class Project(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=100)

    def __str__(self):
        return self.title   
class Skill(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name    