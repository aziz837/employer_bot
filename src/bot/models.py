from django.db import models

class Profile(models.Model):
    external_id = models.PositiveIntegerField(verbose_name='id uchun')
    name = models.TextField(verbose_name='name ucun')

    def __str__(self):
        return f'#{self.external_id}{self.name}'
    class Metta :
        verbose_name='Profil'
        verbose_name_plural = 'profilar'
class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    text= models.TextField(),
    create_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'message{self.pk}{self.profile}'
    class Metta :
        verbose_name='Profil'
        verbose_name_plural = 'profilar'