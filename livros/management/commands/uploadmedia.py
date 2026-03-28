import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
from livros.models import Livro


class Command(BaseCommand):
    help = 'Upload local media files (media/) to the configured DEFAULT_FILE_STORAGE (Cloudinary)'

    def handle(self, *args, **options):
        media_dir = settings.MEDIA_ROOT
        if not os.path.isdir(media_dir):
            self.stdout.write(self.style.ERROR(f'MEDIA_ROOT not found: {media_dir}'))
            return

        livros = Livro.objects.exclude(imagem='')
        total = livros.count()
        self.stdout.write(self.style.NOTICE(f'Found {total} livros with imagem field set.'))

        for livro in livros:
            path = os.path.join(media_dir, str(livro.imagem))
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    django_file = File(f)
                    # Save to default storage (Cloudinary) under same name
                    livro.imagem.save(os.path.basename(path), django_file, save=True)
                    self.stdout.write(self.style.SUCCESS(f'Uploaded {path} -> {livro.imagem.url}'))
            else:
                self.stdout.write(self.style.WARNING(f'Local file not found: {path}'))
