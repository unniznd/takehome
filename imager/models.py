from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage 
from django.core.files.base import ContentFile


from io import BytesIO
from PIL import Image
import uuid


#upload image with unique filename according to user
def userPath(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4())[:16], ext) # Create Unique filename for image of user
    return '{0}/{1}'.format(instance.user.id, filename)

class Imager(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=userPath)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        
        super(Imager, self).save(*args, **kwargs)
         # Save image
        try:
            img_read = storage.open(self.image.name,"r")
        except Exception:
            
            return None
        
        img = Image.open(img_read) # Open image using self

        # Resize the image to 140x140 maximum
        if img.height > 140 or img.width > 140:
            new_img = (140, 140)
            img.thumbnail(new_img)
            imageBuffer = BytesIO()
            img.save(imageBuffer, img.format)

            imager = Imager.objects.get(pk=self.pk)
            imager.image.save(self.image.name,ContentFile(imageBuffer.getvalue()))
        
        
   