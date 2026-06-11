from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies: list = []
    operations = [
        migrations.CreateModel(
            name="DummyModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
