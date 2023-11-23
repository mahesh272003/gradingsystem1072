# Generated by Django 4.2.5 on 2023-10-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(choices=[('CSE-R', 'CSE(Regular)'), ('CSE-H', 'CSE(Honors)'), ('CSIT', 'CS&IT')], max_length=100)),
                ('academicyear', models.CharField(choices=[('2022-23', '2022-23'), ('2023-24', '2023-24')], max_length=20)),
                ('program', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech')], max_length=50)),
                ('semester', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10)),
                ('year', models.IntegerField()),
                ('coursecode', models.CharField(max_length=20)),
                ('coursetitle', models.CharField(max_length=20)),
                ('ltps', models.CharField(max_length=10)),
                ('credits', models.FloatField()),
            ],
            options={
                'db_table': 'course_table',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('facultyid', models.BigIntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=20)),
                ('department', models.CharField(choices=[('CSE-R', 'CSE(Regular)'), ('CSE-H', 'CSE(Honors)'), ('CSIT', 'CS&IT')], max_length=100)),
                ('qualification', models.CharField(choices=[('Ph.d', 'Ph.d'), ('M.Tech', 'M.Tech')], max_length=50)),
                ('designation', models.CharField(choices=[('Prof.', 'Professor'), ('Assoc. Prof.', 'Associate Proffesor'), ('Asst. prof', 'Assistant Professor')], max_length=50)),
                ('semester', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10)),
                ('year', models.IntegerField()),
                ('password', models.CharField(default='klu123', max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'faculty_table',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('studentid', models.BigIntegerField(unique=True)),
                ('fullname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=20)),
                ('department', models.CharField(choices=[('CSE-R', 'CSE(Regular)'), ('CSE-H', 'CSE(Honors)'), ('CSIT', 'CS&IT')], max_length=100)),
                ('program', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech')], max_length=50)),
                ('semester', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=10)),
                ('year', models.IntegerField()),
                ('password', models.CharField(default='klu123', max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'Student_table',
            },
        ),
    ]
