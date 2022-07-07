from django.db import migrations, models


MUNICIPALITY = (
    ("Dasma" , "Dasma"),
    ("Lobo" ,  "Lobo"),
    ("Pasay" , "Pasay"),
   
    )

PROVINCE = (
    ("Cavite" , "cavite"),
    ("Manila" , "manila"),
    ("Batangas" ,"batangas")
    )

GEN_CHOICES =(
    ("F" , "Female"),
    ("M" , "Male"),
    )


class Member_info(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=3)
    Brgy = models.CharField(max_length=50)
    Contact_No = models.CharField(max_length=20)
    ZipCode = models.CharField(max_length=30)
    DSWD_id = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10, choices = GEN_CHOICES)
    
    def __str__(self):
        return self.Name
  
class Program(models.Model):
    member_info = models.ForeignKey(Member_info, default=None, on_delete=models.CASCADE)
    Days = models.TextField(default='')
    Rate = models.TextField(default='')
    Months = models.TextField(default='')
    Total = models.TextField(default='')
    Date_time = models.DateTimeField(default='')

    def __str__(self):
        return self.Date_time
    
class Branch(models.Model): 
    member_branch = models.OneToOneField(Member_info, default=None, on_delete=models.CASCADE)
    Barangay_branch = models.CharField(max_length = 20, choices = PROVINCE, default ="")
    Municipality = models.CharField(max_length = 20, choices = MUNICIPALITY, default ="")
    Program = models.TextField(default='')

    def __str__(self):
        return self.Barangay_branch

class Barangay_report(models.Model):
    Member_rep = models.ForeignKey(Member_info, default=None, on_delete=models.CASCADE)
    Barangayreport = models.TextField(default='')
    Barangay_suggestions = models.TextField(default='')
    Barangayport_date = models.DateTimeField(default='')

    def __str__(self):
        return str(self.Barangayport_date)


class Member_report(models.Model):
    Membe_report = models.ForeignKey(Member_info, default=None, on_delete=models.CASCADE)
    Membereport = models.TextField(default='')
    Membercomment = models.TextField(default='')
    Memberrate = models.TextField(default='')
    Memberrep_date = models.DateTimeField(default='')

    def __str__(self):
        return str(self.Memberrep_date)