# Generated by Django 4.0.5 on 2022-06-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardapp', '0004_remove_review_date_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-Ok'), (2, '2-Watchable'), (3, '3-Good'), (4, '4-Very Good'), (5, '5-Perfect'), (6, '6-Master Piece')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-Ok'), (2, '2-Watchable'), (3, '3-Good'), (4, '4-Very Good'), (5, '5-Perfect'), (6, '6-Master Piece')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-Ok'), (2, '2-Watchable'), (3, '3-Good'), (4, '4-Very Good'), (5, '5-Perfect'), (6, '6-Master Piece')], default=0),
        ),
    ]
