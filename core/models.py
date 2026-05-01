from django.db import models
import re
import re
from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    # Upload image
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    # Google Drive / external URL
    image_url = models.URLField(blank=True, null=True)
    def get_image(self):
        # Uploaded image
        if self.image:
            return self.image.url
        # External or Drive link
        if self.image_url:
            if "drive.google.com" in self.image_url:
                # Format: /d/FILE_ID/
                match = re.search(r'/d/([a-zA-Z0-9_-]+)', self.image_url)
                if match:
                    file_id = match.group(1)
                    return f"https://drive.google.com/uc?export=view&id={file_id}"
                # Format: id=FILE_ID
                match = re.search(r'id=([a-zA-Z0-9_-]+)', self.image_url)
                if match:
                    file_id = match.group(1)
                    return f"https://drive.google.com/uc?export=view&id={file_id}"

            return self.image_url
        # Fallback
        return "https://via.placeholder.com/400x300?text=No+Image"
    def __str__(self):
        return self.title or "Gallery Image"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}⭐)"