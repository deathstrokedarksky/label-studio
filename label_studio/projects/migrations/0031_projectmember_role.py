from django.db import migrations, models
import django_migration_linter as linter

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0030_project_search_vector_index'),
    ]

    operations = [
        linter.IgnoreMigration(),
        migrations.AddField(
            model_name='projectmember',
            name='role',
            field=models.CharField(default='ANNOTATOR', max_length=32, choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('ANNOTATOR', 'Annotator')]),
        ),
    ]
