from django.contrib.postgres.fields import ArrayField
from django.db import models


class Goals(models.Model):
    travel = models.BooleanField()
    relocate = models.BooleanField()
    study = models.BooleanField()
    work = models.BooleanField()


class Monday(models.Model):
    time_8_00 = models.BooleanField()
    time_10_00 = models.BooleanField()
    time_12_00 = models.BooleanField()
    time_14_00 = models.BooleanField()
    time_16_00 = models.BooleanField()
    time_18_00 = models.BooleanField()
    time_20_00 = models.BooleanField()
    time_22_00 = models.BooleanField()


class Teachers(models.Model):
    name = models.CharField(max_length=64)
    about = models.TextField()
    rating = models.FloatField()
    picture = models.TextField()
    price = models.IntegerField()
    goals = models.ForeignKey(Goals, on_delete=models.CASCADE)
    monday = models.ForeignKey(Monday, on_delete=models.CASCADE)


goals_model_manager = Goals.objects
monday_model_manager = Monday.objects
teachers_model_manager = Teachers.objects

'''mon = Monday.objects.create(time_8_00=False, time_10_00=False, time_12_00=False, time_14_00=False, time_16_00=True,
                            time_18_00=True, time_20_00=True, time_22_00=True)

goal = Goals.objects.create(travel=True, relocate=False, study=False, work=True)

Teachers.objects.create(name='Andrew G',
                        about="Hi guys, My name is Andrew and I am an English teacher from the USA currently living "
                              "now in Atlanta, Georgia.My teaching experience ranges from 1 on 1 to groups, "
                              "children to adults, in-person or online. IMPORTANT*** Although I have experience "
                              "teaching Children, right now I'm only teaching Adults through Conversational English. "
                              "This is my specialty and I do this through focusing mainly on Accent Reduction, "
                              "Pronunciation, Speech Therapy, and improving one's Vocabulary.I have been traveling "
                              "and teaching since 2008 and my travels have really helped me be more culturally aware, "
                              "and relevant. I am fun and unique when it comes to teaching English, you won't that "
                              "find my classes anywhere else.",
                        rating=4.2,
                        picture='https://i.pravatar.cc/300?img=38',
                        price=900,
                        goals=goal,
                        monday=mon
                        )'''