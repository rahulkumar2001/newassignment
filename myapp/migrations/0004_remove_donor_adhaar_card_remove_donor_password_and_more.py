# Generated by Django 4.0.4 on 2022-05-27 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_donor_adhaar_card_donor_pan_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='adhaar_card',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='password',
        ),
        migrations.AddField(
            model_name='donor',
            name='adhar_card',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='payment_status',
            field=models.CharField(default=False, max_length=255),
        ),
        migrations.AddField(
            model_name='donor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donor',
            name='user_plan',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='donor',
            name='email',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='pan_card',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='phone',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='upline_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]
