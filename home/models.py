from django.db import models

# Create your models here.

class Departments(models.Model):
        dep_name = models.CharField( max_length=100)
        dep_description = models.TextField()

        def __str__(self) :
                return self.dep_name


class Doctors(models.Model):
        doc_name = models.CharField(max_length=255)
        doc_spcl = models.CharField(max_length=255)
        dep_name = models.ForeignKey(Departments,on_delete=models.CASCADE)
        doc_image = models.ImageField(upload_to='doctors')

        def __str__(self):
                return 'Dr ' +  self.doc_name + '- (' + self.doc_spcl + ')'



class Booking(models.Model):
        p_name = models.CharField(max_length=255)
        p_phon = models.CharField(max_length=10)
        doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
        booking_date= models.DateField()
        booked_on = models.DateField(auto_now=True)


       




        
       


             

    
    
# class Meta:
#         verbose_name = _("Departments")
#         verbose_name_plural = _("Departmentss")

# def __str__(self):
#         return self.name

# def get_absolute_url(self):
#         return reverse("Departments_detail", kwargs={"pk": self.pk})


    

# class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

# def __str__(self):
#         return self.name

# def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
 