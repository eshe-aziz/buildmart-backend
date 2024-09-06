# Generated by Django 5.1 on 2024-09-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeowner', '0002_remove_homeowner_homeowner_id_remove_homeowner_email_and_more'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='email',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='homeowner_id',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='password',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='supplier',
            name='homeowner',
            field=models.ManyToManyField(related_name='suppliers', to='homeowner.homeowner'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
