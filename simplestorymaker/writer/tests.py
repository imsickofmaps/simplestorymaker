"""
These will execute when you run "manage.py test".

"""

from django.test import TestCase
from django.utils import timezone

from writer.models import Role, Story


class WriterTests(TestCase):
    def test_role_creation(self):
        """
        Tests that roles are createable
        """
        new_role = Role(name="Test Role")
        self.assertEqual(new_role.name, "Test Role")

    def test_role_save(self):
        """
        Tests that roles are saveable
        """
        new_role = Role(name="Test Role")
        new_role.save()
        self.assertEqual(new_role.id, 1)

    def test_story_creation(self):
        """
        Tests that stories are createable
        """
        new_role = Role(name="Test Role")
        new_role.save()
        # role = Role.objects.get(n)
        now = timezone.now()
        new_story = Story(reason='test reason', role=new_role,
                          goal='test goal', create_date=now)
        self.assertEqual(new_story.reason, "test reason")
        self.assertEqual(new_story.goal, "test goal")
        self.assertEqual(new_story.create_date, now)
        self.assertEqual(new_story.role, new_role)

    def test_story_save(self):
        """
        Tests that stories are saveable
        """
        new_role = Role(name="Test Role")
        new_role.save()
        # role = Role.objects.get(n)
        now = timezone.now()
        new_story = Story(reason='test reason', role=new_role,
                          goal='test goal', create_date=now)
        new_story.save()
        self.assertEqual(new_story.id, 1)
