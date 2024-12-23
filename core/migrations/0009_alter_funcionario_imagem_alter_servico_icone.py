# Generated by Django 5.1.1 on 2024-11-01 18:31

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_funcionario_imagem_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('ini-cog', 'Engrenagem'), ('ini-users', 'Usuários'), ('ini-stats-up', 'Gráficos'), ('ini-mobile', 'Mobile'), ('ini-rocket', 'Foguete'), ('ini-layers', 'Design')], max_length=12, verbose_name='Icone'),
        ),
    ]
