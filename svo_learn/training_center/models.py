from django.db import models


class EducationOrg(models.Model):
    pass


class DirectionOfTraining(models.Model):
    pass


class RiskLevel(models.Model):
    pass


class TermsOfRetraining(models.Model):
    pass


class EducationMethod(models.Model):
    code = models.CharField(max_length=255, verbose_name='Код')
    name = models.CharField(max_length=255, verbose_name='Название')
    edeucation_org = models.ForeignKey(
        EducationOrg,
        on_delete=models.CASCADE,
        verbose_name='Учебная организация',
        blank=True,
        null=True
    )
    cost = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Стоимость за человека'
    )
    duration = models.SmallIntegerField(
        blank=True,
        null=True,
        verbose_name='Количество дней обучения'
    )
    direction_of_training = models.ForeignKey(
        DirectionOfTraining,
        on_delete=models.SET_NULL,
        verbose_name='Направление обучения',
        blank=True,
        null=True
    )
    risk_level = models.ForeignKey(
        RiskLevel,
        on_delete=models.SET_NULL,
        verbose_name='Уровень риска',
        blank=True,
        null=True
    )
    terms_of_retraining = models.ForeignKey(
        TermsOfRetraining,
        on_delete=models.SET_NULL,
        verbose_name='Сроки переподготовки',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Учебная программа'
        verbose_name_plural = 'Учебные программы'
        default_related_name = 'education_methods'

    def __str__(self):
        return self.name
