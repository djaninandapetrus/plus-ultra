from django.contrib import admin
from .models import user, PetrusProject, PetrusSkill

class userInline(admin.TabularInline):
    model = user
    extra = 1      
@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    inlines = [userInline,]


class PetrusProjectInline(admin.TabularInline):
    model = PetrusProject
    extra = 3
@admin.register(PetrusProject)
class PetrusProjectAdmin(admin.ModelAdmin):
    inlines = [PetrusProjectInline,]


class PetrusSkillInline(admin.TabularInline):
    model = PetrusSkill
    extra = 3
@admin.register(PetrusSkill)
class PetrusSkillAdmin(admin.ModelAdmin):
    inlines = [PetrusSkillInline,]

