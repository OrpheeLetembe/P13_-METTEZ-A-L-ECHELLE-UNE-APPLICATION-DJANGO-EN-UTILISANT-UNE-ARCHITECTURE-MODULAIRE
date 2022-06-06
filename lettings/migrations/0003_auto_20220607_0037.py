# Generated by Django 3.0 on 2022-06-06 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_auto_20220607_0023'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO lettings_letting(
                id,
                title,
                address_id
            )
            SELECT
                id,
                title,
                address_id
            FROM
                oc_lettings_site_letting
         """)
    ]
