from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Delete all blog posts'

    def handle(self, *args, **kwargs):
        Post.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all blog posts'))
