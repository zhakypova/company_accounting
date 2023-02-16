from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    birth_date = models.DateField()
    address = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    department = models.CharField(max_length=30)

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Employee.objects.all()
    #     return context

    def __str__(self):
        return f'{self.name} - {self.lastname}'








