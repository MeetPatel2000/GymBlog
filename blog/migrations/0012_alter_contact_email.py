# Generated by Django 5.0 on 2024-02-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_contact_delete_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
