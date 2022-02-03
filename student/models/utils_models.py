#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Communaute(models.Model):
    """ Communauté models from student app """
    name = models.CharField(max_length=100,
                            verbose_name="Nom de l'association",
                            null=False,
                            unique=True,
                            blank=False)


class AllowedNumber(models.Model):
    """ Model for allowed phone number from student app """
    phone = models.CharField(max_length=20,
                             unique=True,
                             null=False,
                             blank=False,
                             verbose_name="Whats'app")
    communaute = models.ForeignKey(Communaute,
                                   related_name="phones",
                                   on_delete=models.CASCADE,
                                   verbose_name="Communauté")

    def clean(self):
        if len(self.phone) > 20:
            ValidationError(
                _(f"Votre numero est incorrect, " +
                  f"car le nombre maximal de digits saisi est superieur a 20"))
