# Generated by Django 2.0.2 on 2018-02-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=300)),
                ('active_p', models.BooleanField(default=True)),
                ('show_f_p', models.BooleanField(default=True)),
                ('show_d_p', models.BooleanField(default=True)),
                ('show_h_f_p', models.BooleanField(default=False)),
                ('show_h_d_p', models.BooleanField(default=False)),
                ('can_down_p', models.BooleanField(default=False)),
                ('can_up_p', models.BooleanField(default=False)),
                ('can_del_p', models.BooleanField(default=False)),
                ('can_crt_p', models.BooleanField(default=False)),
                ('can_run_p', models.BooleanField(default=False)),
                ('active_u', models.BooleanField(default=True)),
                ('show_f_u', models.BooleanField(default=True)),
                ('show_d_u', models.BooleanField(default=True)),
                ('show_h_f_u', models.BooleanField(default=False)),
                ('show_h_d_u', models.BooleanField(default=False)),
                ('can_down_u', models.BooleanField(default=True)),
                ('can_up_u', models.BooleanField(default=True)),
                ('can_del_u', models.BooleanField(default=False)),
                ('can_crt_u', models.BooleanField(default=True)),
                ('can_run_u', models.BooleanField(default=False)),
                ('active_a', models.BooleanField(default=True)),
                ('show_f_a', models.BooleanField(default=True)),
                ('show_d_a', models.BooleanField(default=True)),
                ('show_h_f_a', models.BooleanField(default=True)),
                ('show_h_d_a', models.BooleanField(default=True)),
                ('can_down_a', models.BooleanField(default=True)),
                ('can_up_a', models.BooleanField(default=True)),
                ('can_del_a', models.BooleanField(default=True)),
                ('can_crt_a', models.BooleanField(default=True)),
                ('can_run_a', models.BooleanField(default=True)),
            ],
        ),
    ]
