from django.db import models

class user(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.name
    
class PetrusProject(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=100)

    def __str__(self):
        return self.title   
class PetrusSkill(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name    