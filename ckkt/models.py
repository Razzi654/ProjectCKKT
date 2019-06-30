from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# --
# -- Data Base: `ckkt`
# --

#
# Structure of the table `categories`
#
class Categories(models.Model):
    categoryId = models.IntegerField(verbose_name="Id категории", unique=True, null=True)
    name = models.CharField("Имя категории", max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%b/%d/')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#
#  Structure of the table `content`
#
class Content(models.Model):
    title = RichTextUploadingField("Заголовок", config_name='small', blank=True, null=True, max_length=255)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, to_field="categoryId", null=True,
                                   verbose_name="Id категории")
    article = RichTextUploadingField("Текст", blank=True, null=True)
    creationDate = models.DateTimeField("Время публикации объекта", default=timezone.now)
    changingDate = models.DateTimeField("Время последнего изменения объекта", auto_now=True)

    class Meta:
        verbose_name = "Работа ЦК"
        verbose_name_plural = "Работы ЦК"

    # """ Showing fields in the admin panel """
    # For Python 3.x
    def __str__(self):
        return self.title

    # For Python 2.x
    def __unicode__(self):
        return self.title


#
# Structure of the table `commissionMembers`
#
class CommissionMembers(models.Model):
    name = RichTextUploadingField("Имя", config_name='small', blank=True, null=True, max_length=255)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, to_field="categoryId", null=True,
                                   verbose_name="Id категории")
    # articleId =
    position = RichTextUploadingField("Должность", blank=True, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%b/%d/")

    class Meta:
        verbose_name = "Членов комиссии"
        verbose_name_plural = "Члены комиссии"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#
# Structure of the table `messages`
#
class Messages(models.Model):
    name = models.CharField("Имя", max_length=255, editable=False)
    themes = models.CharField("Тема", max_length=255, editable=False)
    email = models.EmailField(max_length=254, editable=False)
    message = models.TextField(editable=False)
    date = models.DateTimeField("Время входящего сообщения", default=timezone.now, editable=False)

    class Meta:
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#
# Structure of the table `disciplines`
#
class Disciplines(models.Model):
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, to_field="categoryId", null=True,
                                   verbose_name="Id категории")
    name = models.CharField("Название дисциплины", max_length=255)
    description = models.TextField("Описание", null=True)

    class Meta:
        verbose_name = ["Дисциплина", "Дисциплин"]
        verbose_name_plural = "Дисциплины"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#
# Structure of the table `specialities`
#
class Specialities(models.Model):
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, to_field="categoryId", null=True,
                                   verbose_name="Категория")
    name = models.CharField("Название специальности", max_length=255)
    description = RichTextUploadingField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#
# Structure of the table `clubs`
#
class Clubs(models.Model):
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, to_field="categoryId", null=True,
                                   verbose_name="Категория")
    name = models.CharField("Название кружка", max_length=255)
    description = RichTextUploadingField("Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Кружки"
        verbose_name_plural = "Кружки"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#
# Structure of the table `contacts`
#
class Contacts(models.Model):
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, to_field="categoryId", null=True,
                                   verbose_name="Категория")
    title = models.CharField("Заголовок", max_length=255, null=True)
    contacts = RichTextUploadingField("Контакты", blank=True, null=True)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
