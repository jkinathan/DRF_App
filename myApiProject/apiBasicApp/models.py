from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TestModel(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True, error_messages={
        "null": "This field can't be null"
    })
    description = models.TextField()
    phone = models.TextField()
    is_alive = models.BooleanField()
    amount = models.CharField(max_length=50)
    slug = models.CharField(max_length=250, editable=False, default="null")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%H:%M:%S')}"
    
    class Meta:
        ordering = ['created_at'] #order tuple since we can add multiple ['-created_at'] -- asc order
        verbose_name_plural = "Test Model"

    # Overriding the default way it is going to save
    def save(self, *args, **kwargs):
        self.slug = f"{self.name} - {self.phone}"
        super().save(*args, **kwargs)

class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel,on_delete=models.CASCADE, related_name="TestContent")
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"
    
    class Meta:
        verbose_name_plural = 'Model X'