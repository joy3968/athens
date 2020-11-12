# Generated by Django 3.1.2 on 2020-11-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0008_cust_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpage_tbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_img_main', models.ImageField(blank=True, null=True, upload_to='userpage/')),
                ('page_img_sub1', models.ImageField(blank=True, null=True, upload_to='userpage/')),
                ('page_img_sub2', models.ImageField(blank=True, null=True, upload_to='userpage/')),
            ],
        ),
        migrations.DeleteModel(
            name='cust_info',
        ),
    ]