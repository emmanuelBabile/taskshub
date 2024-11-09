# tasks/scripts/load_initial_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Project, Task, Comment


class Command(BaseCommand):
    help = 'Loads initial data for the app'

    def handle(self, *args, **kwargs):
        # Delete existing data to avoid duplicates during multiple loads
        Comment.objects.all().delete()
        Task.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()

        # Create users
        user1 = User.objects.create_user(username="Alice", email="alice@taskshub.com", password="password123")
        user2 = User.objects.create_user(username="Bob", email="bob@taskshub.com", password="password123")
        user3 = User.objects.create_user(username="James", email="james@taskshub.com", password="password123")
        user4 = User.objects.create_user(username="Brenna", email="brenna@taskshub.com", password="password123")

        # Create projects
        project1 = Project.objects.create(name="Product Launch", description="Prepare and launch the new product.")
        project2 = Project.objects.create(name="Internal Reorganization",
                                          description="Plan for a better internal reorganization.")

        # Add members to the projects
        project1.members.add(user1, user2)
        project2.members.add(user1, user2)

        # Create tasks for project 1
        task1 = Task.objects.create(title="Market Research", description="Analyze market trends.",
                                    project=project1, assigned_to=user1, status="TO_DO", priority=1)
        task2 = Task.objects.create(title="Product Development", description="Create the prototype.",
                                    project=project1, assigned_to=user2, status="IN_PROGRESS", priority=2)
        task3 = Task.objects.create(title="Marketing Strategy", description="Develop a launch strategy.",
                                    project=project1, assigned_to=user1, status="DONE", priority=3)

        # Create tasks for project 2
        task4 = Task.objects.create(title="Process Analysis", description="Examine current processes.",
                                    project=project2, assigned_to=user1, status="DONE", priority=1)
        task5 = Task.objects.create(title="Reorganization Plan", description="Develop the new plan for organization.",
                                    project=project2, assigned_to=user2, status="IN_PROGRESS", priority=2)
        task6 = Task.objects.create(title="Implementation", description="Implement the new plan.",
                                    project=project2, assigned_to=user3, status="TO_DO", priority=1)

        # Create comments for the tasks
        Comment.objects.create(task=task1, user=user1, content="I have started analyzing market data.")
        Comment.objects.create(task=task2, user=user2, content="The prototype is under development.")
        Comment.objects.create(task=task3, user=user3, content="The marketing strategy is completed.")
        Comment.objects.create(task=task4, user=user4, content="I have identified possible improvements in current processes.")
        Comment.objects.create(task=task5, user=user1, content="The reorganization plan is almost ready.")
        Comment.objects.create(task=task6, user=user2, content="Implementation will begin next week.")

        self.stdout.write(self.style.SUCCESS('Initial data loaded successfully.'))
