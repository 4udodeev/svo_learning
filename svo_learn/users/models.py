from django.contrib.auth.models import AbstractUser
from django.db import models

from training_center.models import EducationMethod


SEX_CHOISES = [
    ('male', 'мужской'),
    ('female', 'женский')
]


class CurrentStates(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код')
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Состояние сотрудника'
        verbose_name_plural = 'Состояния сотрудника'
        default_related_name = 'current_states'

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Код',
        default=None
    )
    middle_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Отчество'
    )
    sex = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        choices=SEX_CHOISES,
        verbose_name='Пол'
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата рождения'
    )
    photo = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Фото',
        upload_to='employes_photo'
    )
    passport = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Паспортные данные'
    )
    driver_license = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='Водительское удостоверение'
    )
    education = models.CharField(
        max_length=256,
        verbose_name='Образование',
        blank=True,
        null=True
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарий'
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Адрес электронной почты'
    )
    username = models.CharField(
        max_length=256,
        verbose_name='Имя пользователя',
        unique=True)
    password = models.CharField(max_length=256, verbose_name='пароль')
    is_banned = models.BooleanField(
        default=False,
        verbose_name='Доступ запрещен'
    )

    is_candidate = models.BooleanField(
        default=False,
        verbose_name='Является кандидатом'
    )
    is_dismiss = models.BooleanField(
        default=False,
        verbose_name='Уволен'
    )
    hire_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата приема'
    )
    dismiss_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата увольнения'
    )
    current_state = models.ForeignKey(
        CurrentStates,
        on_delete=models.SET_NULL,
        verbose_name='Текущее состояние',
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        default_related_name = 'employes'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.code
        super().save(*args, **kwargs)


class ChangeLog(models.Model):
    pass


class HistoryState(models.Model):
    pass


class Organization(models.Model):
    code = models.CharField(
        max_length=255,
        verbose_name='Код',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        default_related_name = 'organizations'

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    code = models.CharField(
        max_length=255,
        verbose_name='Код',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='subs'
    )
    parent_subdivision = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    is_disbanded = models.BooleanField(
        default=False,
        verbose_name='Расформировано'
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        default_related_name = 'subdivisions'

    def __str__(self):
        return self.name


class BasePosition(models.Model):
    code = models.CharField(
        max_length=255,
        verbose_name='Код',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    training_requirements = models.ManyToManyField(
        EducationMethod,
        blank=True,
        verbose_name='Обязательное обучение',
        related_name='base_positions'
    )

    class Meta:
        verbose_name = 'Типовая должность'
        verbose_name_plural = 'Типовые должности'
        default_related_name = 'base_positions'

    def __str__(self):
        return self.name


class PositionCategory(models.Model):
    code = models.CharField(
        max_length=255,
        verbose_name='Код',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория должности'
        verbose_name_plural = 'Категории должности'
        default_related_name = 'position_cathegorys'

    def __str__(self):
        return self.name


class PositionTypeOfWork(models.Model):
    code = models.CharField(
        max_length=255,
        verbose_name='Код',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип должности'
        verbose_name_plural = 'Типы должности'
        default_related_name = 'position_types_of_work'

    def __str__(self):
        return self.name


class Mvz(models.Model):
    code = models.CharField(
        max_length=255,
        verbose_name='Код',
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'МВЗ'
        verbose_name_plural = 'МВЗ'
        default_related_name = 'MVZ'

    def __str__(self):
        return self.name


class Position(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код')
    name = models.CharField(max_length=255, verbose_name='Название')
    position_cathegory = models.ForeignKey(
        PositionCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    position_type_of_work = models.ForeignKey(
        PositionTypeOfWork,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    mvz = models.ForeignKey(
        Mvz,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        default_related_name = 'positions'

    def __str__(self):
        return self.name
