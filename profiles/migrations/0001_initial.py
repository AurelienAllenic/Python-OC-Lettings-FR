from django.db import migrations
from oc_lettings_site.models import Profile as OldProfile
from profiles.models import Profile as NewProfile
from django.conf import settings
from django.db import models
import django.db.models.deletion

def copy_old_profiles(apps, schema_editor):

    # Accédez aux données de l'ancienne table
    old_profiles = OldProfile.objects.all()
    
    # Parcourez les anciens profils et copiez les données dans la nouvelle table
    for old_profile in old_profiles:
        NewProfile.objects.create(
            favorite_city=old_profile.favorite_city,
            user=old_profile.user
        )

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_city', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', related_query_name='profile_user_query', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(copy_old_profiles),
    ]
