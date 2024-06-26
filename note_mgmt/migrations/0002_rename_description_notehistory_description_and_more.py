# Generated by Django 5.0.4 on 2024-04-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notehistory',
            old_name='Description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='notehistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notehistory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notehistory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
