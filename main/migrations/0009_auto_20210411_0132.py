# Generated by Django 3.1.7 on 2021-04-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('btn', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
