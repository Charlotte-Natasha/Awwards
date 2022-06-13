# Generated by Django 4.0.5 on 2022-06-13 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wardapp', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('text', models.TextField(blank=True, max_length=3000)),
                ('design', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('usability', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('content', models.PositiveSmallIntegerField(choices=[(1, '1- Trash'), (2, '2- Horrible'), (3, '3- Terrible'), (4, '4- Bad'), (5, '5- Ok'), (6, '6- Watchable'), (7, '7- Good'), (8, '8- Very Good'), (9, '9- perfect'), (10, '10- Master Piece')], default=0)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wardapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
