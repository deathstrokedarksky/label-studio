from django.db import migrations, models
import django_migration_linter as linter

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_custom_hotkeys'),
    ]

    operations = [
        linter.IgnoreMigration(),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='ANNOTATOR', max_length=32, choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('ANNOTATOR', 'Annotator')]),
        ),
    ]
