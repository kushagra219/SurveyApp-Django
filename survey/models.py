from django.db import models

roles = [
    ('ST', 'Student'),
    ('PT', 'Part Time'),
    ('FT', 'Full TIme'),
    ('OT', 'Others')
]

recommendations = [
    ('DF', 'Definitely'),
    ('MB', 'Maybe'),
    ('NS', 'Not Sure')
]

languages = [
    ('CP', 'C++'),
    ('JV', 'Java'),
    ('PY', 'Python')
]

improvements = [
    ('FE', 'Frontend'),
    ('BE', 'Backend'),
    ('DV', 'Data Vizualisation')
]

# Create your models here.
class Improvement(models.Model):
    description = models.CharField(choices=improvements, max_length=2)

    def __str__(self):
        return self.description


class Survey(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    current_role = models.CharField(choices=roles, max_length=2)
    recommendation = models.CharField(choices=recommendations, max_length=2)
    fav_language = models.CharField(choices=languages, max_length=2)
    improvements = models.ManyToManyField(Improvement)

    def __str__(self):
        return f"{self.id}. {self.name}"

    def get_improvements_string(self):
        string = ""
        for id in self.improvements:
            improvement_obj = Improvement.objects.get(id=id)
            string += improvement_obj + ", "
        return string[:-2] if len(string) > 0 else string


# Common Model Queries
# model.objects.all() - gives all the objects of that models
# model.objects.get(field1=value1, field2=value2....) - give you a single object satisfying the condition
# model.objects.filter(field1=value1, field2=value2......) - give you multiple objects satisfying the conditions




