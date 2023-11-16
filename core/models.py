from django.db import models


class GenericModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: bool = True


class ContactRequest(GenericModelMixin):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'Contact Request from {self.name} - {self.message[:20]}'
