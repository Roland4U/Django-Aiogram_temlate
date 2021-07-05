from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Run Telegram Bot'

    def handle(self, *args, **options):
        from bot.core import app
        app