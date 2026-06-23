from django.db import models
from django.contrib.auth.models import User
import datetime

class RegistrationRequest(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('alumni', 'Alumni')
    ]

    full_name = models.CharField(max_length=150)
    prn_number = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username


from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]
    
    GRADUATION_CHOICES = [
        ('degree', 'Degree'),
        ('diploma', 'Diploma'),
        ('post_graduation', 'Post Graduation'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.CharField(max_length=1, choices=YEAR_CHOICES)
    department = models.CharField(max_length=100)
    passout_year = models.IntegerField()
    graduation_type = models.CharField(max_length=20, choices=GRADUATION_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile picture field

    def __str__(self):
        return f"{self.full_name}'s Profile"

    
    
class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    current_working = models.BooleanField(default=False, verbose_name="Currently Working")
    company_name = models.CharField(max_length=150, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Added profile picture field

    def __str__(self):
        return self.full_name

class Post(models.Model):
    POST_TYPE_CHOICES = [
        ('job', 'Job'),
        ('internship', 'Internship'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_type = models.CharField(
        max_length=10,
        choices=POST_TYPE_CHOICES,
        default='Job',  # default value can be 'Job' or 'Internship'
    )
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    qualification = models.CharField(max_length=255, default="Not Specified")

    role_responsibility = models.TextField(default="Not Specified")
    skills = models.CharField(max_length=255,default="Not Specified")
    description = models.TextField()
    closing_date = models.DateField(null=True, blank=True)

    post_date = models.DateField(null=True, blank=True, default=datetime.date.today)

    def __str__(self):
        return f"{self.title} ({self.post_type}) at {self.company_name}"
    

from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"



class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resources/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class FundingInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount_required = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)  # QR Code upload
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title