from django.db import models

class Strategy(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="strategy_images/", blank=True, null=True)

class Comment(models.Model):
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)