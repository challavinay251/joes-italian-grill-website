from django.db import models
import re


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def get_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            # Convert Google Drive link
            match = re.search(r'/d/(.*?)/', self.image_url)
            if match:
                file_id = match.group(1)
                return f"https://drive.google.com/uc?export=view&id={file_id}"

            return self.image_url

        return "https://via.placeholder.com/400x300?text=No+Image"

    def __str__(self):
        return self.title



class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}⭐)"