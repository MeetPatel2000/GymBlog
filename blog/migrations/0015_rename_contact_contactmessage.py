# Generated by Django 5.0 on 2024-02-12 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_contact_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactMessage',
        ),
    ]
