from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from account.models import CustomUser

TYPE_CHOICES = (
    ('yes', 'Да'),
    ('no', 'Нет')
)

BLOOD_TYPE = (
    ('a_RhD_positive', 'RhD положительный (А+)'),
    ('b_RhD_positive', 'В RhD положительный (В+)'),
    ('o_RhD_positive', 'O RhD положительный (O+)'),
    ('ab_RhD_positive', 'AB RhD положительный (AB+)'),
)


class Surrogacy(models.Model):
    owner_email = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                    related_name='surrogacy_applications')
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    family_status = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    education = models.CharField(max_length=130)
    job = models.CharField(max_length=125)

    height = models.IntegerField(
        validators=[
            MinValueValidator(150, message='Рост не должен быть меньше 150см'),
            MaxValueValidator(180, message='Рост не должен быть больше 180см')
        ]
    )

    weight = models.IntegerField(
        validators=[
            MinValueValidator(40, 'Вес не должен быть меньше 40кг'),
            MaxValueValidator(90, 'Вес не должен быть больше 90кг')
        ]
    )
    hows_pregnancy_g = models.TextField()

    arterial_pressure = models.CharField(max_length=500)

    children = models.JSONField(default=list, blank=True)
    breastfeeding = models.CharField(10, choices=TYPE_CHOICES)
    when_breast_feed = models.DateField()
    usage_hormon_contr = models.CharField(10, choices=TYPE_CHOICES)

    blood_type = models.CharField(max_length=100, choices=BLOOD_TYPE)
    menstrual_cycle = models.CharField(max_length=120)
    last_menstrual_cycle = models.DateField()
    gynecological_history = models.CharField(max_length=120)

    sexually_transmitted_diseases = models.TextField()

    # АБОРТЫ И ВЫКИДЫШИ
    miscarriages_abortions = models.CharField(max_length=10, choices=TYPE_CHOICES)
    # ПОЛЯ В СЛУЧАЕ ОТВЕТА ДА
    ab_term = models.CharField(max_length=150, blank=True, null=True)
    ab_quantity = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        blank=True,
        null=True
    )
    ab_year = models.TextField(blank=True, null=True)

    surrogacy_experience = models.CharField(max_length=50, choices=TYPE_CHOICES)
    smoking = models.CharField(max_length=50, choices=TYPE_CHOICES)
    alcohol = models.CharField(max_length=50, choices=TYPE_CHOICES)
    chronic_diseases = models.CharField(max_length=300)

    operations_which_when = models.TextField()
    family_medical_history = models.TextField()
    multiple_pregnancies_in_family = models.CharField(max_length=50, choices=TYPE_CHOICES)

    why_surrogate_mother = models.TextField()
    how_learned_about_surrogacy_program = models.TextField()
    family_approval = models.CharField(max_length=50, choices=TYPE_CHOICES)

    legal_issues = models.CharField(50, choices=TYPE_CHOICES)

    phone_number = models.CharField(max_length=50)

    face_photo = models.ImageField(upload_to='media/surrogacy')
    full_body_selfie = models.ImageField(upload_to='media/surrogacy')
    passport_photo = models.ImageField(upload_to='media/surrogacy')

    manager_name = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Анкета суррогатной матери'
        verbose_name_plural = 'Анкеты суррогатных матерей'






