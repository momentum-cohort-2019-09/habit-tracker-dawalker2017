# Generated by Django 2.2.7 on 2019-11-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191107_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='Max Characters: 25', max_length=25, null=True, verbose_name='Subject:')),
                ('description', models.CharField(help_text='Max Characters: 255', max_length=255, null=True, verbose_name='Description:')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
