# Generated by Django 4.1.2 on 2022-11-11 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kycdocuments',
            name='name',
            field=models.CharField(default='Test Value', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('holder_name', models.CharField(max_length=255)),
                ('swift', models.CharField(max_length=255)),
                ('iban', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=32)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'banks',
            },
        ),
    ]