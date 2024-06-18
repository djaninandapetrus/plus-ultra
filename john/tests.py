from django.test import TestCase
from .models import User, PetrusProject, PetrusSkill

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.bio, "Lorem ipsum dolor sit amet")

    def test_update_user(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        user.name = "Jane Doe"
        user.bio = "Updated bio"
        user.save()
        updated_user = User.objects.get(pk=user.pk)
        self.assertEqual(updated_user.name, "Jane Doe")
        self.assertEqual(updated_user.bio, "Updated bio")

    def test_delete_user(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        user.delete()
        self.assertFalse(User.objects.filter(pk=user.pk).exists())

class PetrusProjectModelTest(TestCase):
    def test_create_petrus_project(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        petrus_project = PetrusProject.objects.create(user=user, title="Project 1", description="Lorem ipsum dolor sit amet")
        self.assertEqual(petrus_project.title, "Project 1")
        self.assertEqual(petrus_project.description, "Lorem ipsum dolor sit amet")

    def test_update_petrus_project(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        petrus_project = PetrusProject.objects.create(user=user, title="Project 1", description="Lorem ipsum dolor sit amet")
        petrus_project.title = "Updated Project"
        petrus_project.description = "Updated description"
        petrus_project.save()
        updated_petrus_project = PetrusProject.objects.get(pk=petrus_project.pk)
        self.assertEqual(updated_petrus_project.title, "Updated Project")
        self.assertEqual(updated_petrus_project.description, "Updated description")

    def test_delete_petrus_project(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        petrus_project = PetrusProject.objects.create(user=user, title="Project 1", description="Lorem ipsum dolor sit amet")
        petrus_project.delete()
        self.assertFalse(PetrusProject.objects.filter(pk=petrus_project.pk).exists())

class PetrusSkillModelTest(TestCase):
    def test_create_petrus_skill(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        petrus_skill = PetrusSkill.objects.create(user=user, name="HTML", category="Front-end Development")
        self.assertEqual(petrus_skill.name, "HTML")
        self.assertEqual(petrus_skill.category, "Front-end Development")

    def test_update_petrus_skill(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        petrus_skill = PetrusSkill.objects.create(user=user, name="HTML", category="Front-end Development")
        petrus_skill.name = "CSS"
        petrus_skill.category = "Front-end Design"
        petrus_skill.save()
        updated_petrus_skill = PetrusSkill.objects.get(pk=petrus_skill.pk)
        self.assertEqual(updated_petrus_skill.name, "CSS")
        self.assertEqual(updated_petrus_skill.category, "Front-end Design")

    def test_delete_petrus_skill(self):
        user = User.objects.create(name="John Doe", bio="Lorem ipsum dolor sit amet")
        petrus_skill = PetrusSkill.objects.create(user=user, name="HTML", category="Front-end Development")
        petrus_skill.delete()
        self.assertFalse(PetrusSkill.objects.filter(pk=petrus_skill.pk).exists())

