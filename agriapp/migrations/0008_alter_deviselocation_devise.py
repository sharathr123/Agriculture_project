# Generated by Django 4.0.4 on 2022-12-31 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agriapp', '0007_alter_apicountthreshold_devise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviselocation',
            name='devise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agriapp.devise', unique=True),
        ),
    ]
