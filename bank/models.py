from django.db import models

# Create your models here.


class Client(models.Model):
    client_id = models.IntegerField(blank=False, primary_key=True)
    Second_name = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    Third_name = models.CharField(max_length=30, blank=True, default=None, null=True)
    Passport = models.CharField(max_length=30)
    Address = models.CharField(max_length=60)
    Salary = models.IntegerField(blank=False)


class CreditType(models.Model):
    credit_type_id = models.IntegerField(blank=False, primary_key=True)
    credit_name = models.CharField(max_length=30)
    interest_rate = models.IntegerField(blank=False)
    provision_condition = models.CharField(max_length=50)


class Credit(models.Model):
    # credit_id = models.IntegerField(blank=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    credit_type_id = models.ForeignKey(CreditType, on_delete=models.CASCADE)
    submission_date = models.DateField('submission date')
    how_long = models.DateField('how long')
    return_date = models.DateField('return date', blank=True, default=None, null=True)
    cost = models.IntegerField(blank=False)
    is_payed = models.BooleanField(default=False)

    def return_date_is(self):
        self.return_date = self.submssion_date + self.how_long
        return super().save(*args, **kwargs)


