# Generated by Django 2.1.1 on 2019-01-29 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipes_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientList',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='receipes_api.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InstructionList',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='receipes_api.Instruction')),
            ],
        ),
        migrations.CreateModel(
            name='Portion',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('portion_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='instructionlist',
            name='list_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='receipes_api.Receipe'),
        ),
        migrations.AddField(
            model_name='ingredientlist',
            name='list_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='receipes_api.Receipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='portion',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='receipes_api.Portion'),
        ),
    ]