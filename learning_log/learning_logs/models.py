from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return the string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
