from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
   
    def __str__(self):
        return self.title
# class Post_version(models.Model):
#     post=models.ForeignKey(Post, on_delete=models.CASCADE)
#     title=models.CharField(max_length=200)
#     desc=models.TextField()
#     version=models.IntegerField(null=True)
class Version(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='versions')
    version_number = models.IntegerField()
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.post.title} - Version {self.version_number}"

