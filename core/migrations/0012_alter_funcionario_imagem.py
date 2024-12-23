# Generated by Django 5.1.1 on 2024-11-04 19:59

import core.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': False, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
    ]
