# Generated by Django 5.1 on 2024-09-05 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeowner', '0003_homeowner_myuser'),
        ('myuser', '0001_initial'),
        ('supplier', '0002_remove_supplier_email_remove_supplier_homeowner_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='id',
        ),
        migrations.AddField(
            model_name='supplier',
            name='myuser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='myuser.myuser'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='homeowner',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='supplier',
            name='homeowner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='homeowner.homeowner'),
            preserve_default=False,
        ),
    ]
