from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid

from surrogacy.models import generate_special_code

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
    special_code = models.UUIDField(default=generate_special_code, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(18, message='Возраст не может быть меньше 18 лет!'),
            MaxValueValidator(30, message='Возраст не может быть больше 30 лет!')
        ]
    )
    date_of_birth = models.DateField()
    date_of_menstrual_cycle = models.DateField()
    nationality = models.CharField(max_length=50)
    country_of_residence = models.CharField(max_length=55)
    education = models.CharField(max_length=60, choices=ED_CHOICES)
    current_job = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
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

    children = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Количество не может быть меньше 0'),
            MaxValueValidator(10, message='Количество не может быть больше 10'),
        ]
    )

    brothers_sisters = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Количество не может быть меньше 0'),
            MaxValueValidator(10, message='Количество  не может быть больше 10'),
        ]
    )
    fathers_hair_colour = models.CharField(max_length=70)
    fathers_eye_colour = models.CharField(max_length=70)

    health_status = models.CharField(max_length=50, choices=HEALTH_CHOICES)
    personality_type = models.CharField(max_length=60, choices=PERSONALITY_TYPE_CHOICES)

    hobby = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=13)
    user = models.ForeignKey('account.CustomUser', to_field='email',
                                   on_delete=models.CASCADE, related_name='donor_applications')

    comment = models.TextField()

    photo_fas = models.ImageField(upload_to='media/donor')
    photo_full = models.ImageField(upload_to='media/donor')
    photo_side = models.ImageField(upload_to='media/donor')
    tunduk_account = models.CharField(max_length=10, choices=EXP_OF_DON)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.special_code}'

    class Meta:
        verbose_name = 'Донор'
        verbose_name_plural = 'Доноры'


