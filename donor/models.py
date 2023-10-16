from uuid import uuid4

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

ED_CHOICES = (
    ('no_education', 'Без образования'),
    ('early_childhood_education', 'Дошкольное образование'),
    ('primary_education', 'Начальное образование'),
    ('lower_secondary_educatoin', 'Неполное среднее образование'),
    ('upper_secondary_education', 'Полное среднее образование'),
    ('post-secondary_non-tertiary_education', 'Послесреднее невысшее образование'),
    ('short-cycle_tertiary_education', 'Краткосрочное высшее образование'),
    ('bachelor\'s_or_equivalent_level', 'Бакалавр или эквивалентный уровень'),
    ('master\'s_or_equivalent_level', 'Магистр или эквивалентный уровень'),
    ('doctoral_or_equivalent_level', 'Докторантура или эквивалентный уровень'),
    ('not_elsewhere_classified', 'Не классифицировано в вышеперечисленном'),
)

MARITAL_STATUS_CHOICES = (
    ('single', 'Одинокий'),
    ('married', 'Женатый'),
    ('widowed', 'Вдовец'),
    ('divorced', 'В разводе'),
)

EXP_OF_DON = (
    ('yes', 'Да'),
    ('no', 'Нет'),
)

BLOOD_TYPE = (
    ('a_RhD_positive', 'RhD положительный (А+)'),
    ('b_RhD_positive', 'В RhD положительный (В+)'),
    ('o_RhD_positive', 'O RhD положительный (O+)'),
    ('ab_RhD_positive', 'AB RhD положительный (AB+)'),
)

HEALTH_CHOICES = (
    ('healthy', 'Здоров'),
    ('not_healthy', 'Не здоров')
)

PERSONALITY_TYPE_CHOICES = (
    ('sanguine', 'Сангвиник'),
    ('choleric', 'Холерик'),
    ('phlegmatic', 'Флегматик'),
    ('melancholic', 'Меланхолик')
)

# Анкета для регистрации донора------------------------------


class DonorApplication(models.Model):
    special_code = models.CharField(max_length=3333)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(18, message='Возраст не может быть меньше 18 лет!'),
            MaxValueValidator(30, message='Возраст не может быть больше 30 лет!')
        ], null=True
    )
    date_of_birth = models.DateField()
    date_of_menstrual_cycle = models.DateField()
    nationality = models.CharField(max_length=50)
    country_of_residence = models.CharField(max_length=55)
    education = models.CharField(max_length=60, choices=ED_CHOICES)
    current_job = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=30, choices=MARITAL_STATUS_CHOICES)
    experience_of_donation = models.CharField(max_length=10, choices=EXP_OF_DON)
    willingness_to_travel = models.CharField(max_length=10, choices=EXP_OF_DON)
    physical_characteristics = models.CharField(max_length=16, choices=BLOOD_TYPE)
    height = models.IntegerField(
        validators=[
            MinValueValidator(160, message='Высота донора должна быть не менее 160см'),
            MaxValueValidator(200, message='Высота донора должна быть не более 200см')
        ]
    )
    weight = models.IntegerField(
        validators=[
            MinValueValidator(50, message='Вес донора должен быть не менее 50кг'),
            MaxValueValidator(100, message='Вес донора должен быть не более 100кг')
        ]
    )
    mothers_hair_colour = models.CharField(max_length=70)
    mothers_eye_colour = models.CharField(max_length=70)

    fathers_hair_colour = models.CharField(max_length=70)
    fathers_eye_colour = models.CharField(max_length=70)

    health_status = models.CharField(max_length=50, choices=HEALTH_CHOICES)
    personality_type = models.CharField(max_length=60, choices=PERSONALITY_TYPE_CHOICES)

    phone_number = models.CharField(max_length=13)
    email = models.EmailField(unique=True)

    comment = models.TextField()

    def __str__(self):
        return f'{self.special_code}'

    def create_special_code(self):
        code = str(uuid4())
        self.special_code = code