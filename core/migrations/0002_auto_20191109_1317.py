# Generated by Django 2.2.7 on 2019-11-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='Habits_completed',
        ),
        migrations.AddField(
            model_name='log',
            name='Habits_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='habit',
            name='description',
            field=models.TextField(blank=True, help_text='Max Characters: 255', max_length=255, null=True, verbose_name='Description:'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='title',
            field=models.CharField(help_text='Max Characters: 255', max_length=255, null=True, verbose_name='Title:'),
        ),
    ]