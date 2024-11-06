# Generated by Django 5.0.2 on 2024-11-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['phone'], name='accounts_cu_phone_c30b3c_idx'),
        ),
        migrations.AddIndex(
            model_name='customuser',
            index=models.Index(fields=['id', 'level'], name='accounts_cu_id_840666_idx'),
        ),
    ]
