####USER####

class RedditUser(AbstractUser):
    karma = models.IntegerField(default=0)
    email = models.EmailField(max_length=150)

####SUBREDDIT####
class Moderator(models.Model):
    is_moderator = models.BooleanField(default=False)
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class SubReddit(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    subscriber = models.ManyToManyField(RedditUser, related_name='user')
    moderator = models.ManyToManyField(Moderator, related_name='moderator')

    def __str__(self):
        return self.name

####POST#####
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=4000)
    date_created = models.DateField(default=timezone.now)
    author = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    subreddit = models.ForeignKey(SubReddit, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

####COMMENTS####
class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=4000)
    user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    date_created = models.DateField(default=timezone.now)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['-body']
        level_attr = 'mptt_level'

    def __str__(self):
        return self.body