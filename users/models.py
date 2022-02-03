import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from student.models.utils_models import Community

USER_ROLES = [('Admin', 'Admin'), ('Staff', 'Staff'),
              ('Utilisateur', 'Utilisateur')]


class UserAccountManager(UserManager):
    """ DOCSTRING:
        Define a custom user manager
    """

    # override create user method to accept email as username
    def create_user(self,
                    username=None,
                    email=None,
                    password=None,
                    **extra_fields):

        return super().create_user(username=username,
                                   email=email,
                                   password=password,
                                   **extra_fields)

    # override createusuperuser method to accept email as username
    def create_superuser(self,
                         username=None,
                         email=None,
                         password=None,
                         **extra_fields):

        return super().create_superuser(username=username,
                                        email=email,
                                        password=password,
                                        **extra_fields)


class UserAccount(AbstractUser):
    """ DOCSTRING:
        define a custom user models
    """
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=40,
                            choices=USER_ROLES,
                            default='Utilisateur')
    # Student have to provide a valide phone number associate to an organisation
    #to be able sign up
    phone = models.CharField(verbose_name="Whats'app",
                             max_length=20,
                             null=True,
                             blank=True)

    community = models.ForeignKey(Community,
                                  null=True,
                                  on_delete=models.CASCADE)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'password']

    objects = UserAccountManager()

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    def clean(self):
        if self.phone not in self.community.phones:
            ValidationError(
                _("Votre numero de telephone, n'est reconnus dans aucune community"
                  ))
