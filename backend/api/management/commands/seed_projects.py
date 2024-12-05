import random
from django.core.management.base import BaseCommand

from api.models import Projects, Categories


class Command(BaseCommand):
    help = 'Seed the database with projects and categories'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding projects and categories...'))
        run_seed()
        self.stdout.write(self.style.SUCCESS('Successfully seeded projects and categories'))


def create_category(index):
    category = Categories(
        title=f'Category Title {index}'  # Add the iterator to the title
    )
    category.save()
    return category


def create_project():
    # Select a random category for the project
    category = random.choice(Categories.objects.all())
    project = Projects(
        title=f'Project Title {random.randint(1, 100)}',
        description='This is a project description.',
        category=category  # Assign a random category
    )
    project.save()
    return project


def clear_data():
    Projects.objects.all().delete()
    Categories.objects.all().delete()  # Ensure categories are also cleared


def run_seed():
    # Clear existing data
    # clear_data()

    # Create 4 categories
    for i in range(1, 5):
        create_category(i)

    # Create 16 projects, each assigned to a random category
    for _ in range(16):
        create_project()
