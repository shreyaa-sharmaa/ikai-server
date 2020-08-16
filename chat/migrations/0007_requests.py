# Generated by Django 3.1 on 2020-08-15 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_auto_20200813_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('DECLINED', 'DECLINED')], max_length=20)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requests_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='requests_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]