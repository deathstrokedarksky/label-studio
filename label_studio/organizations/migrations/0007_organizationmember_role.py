from django.db import migrations, models
import django_migration_linter as linter

class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_alter_organizationmember_deleted_at'),
    ]

    operations = [
        linter.IgnoreMigration(),
        migrations.AddField(
            model_name='organizationmember',
            name='role',
            field=models.CharField(default='ANNOTATOR', max_length=32, choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('ANNOTATOR', 'Annotator')]),
        ),
    ]
