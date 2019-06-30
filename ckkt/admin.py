from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.

from .models import (
    Content, Categories, Messages, CommissionMembers,
    Disciplines, Specialities, Contacts, Clubs
)


def fieldSize(size, rows, cols):
    """
    Changing sizes of the fields CharField and TextField

    :param size: size of the CharField, must be a str
    :param rows: height of the TextField, must be an int
    :param cols: width of the TextField, must be an int
    :return: formfield_overrides
    """

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': str(size)})},
        models.TextField: {'widget': Textarea(attrs={'rows': rows, 'cols': cols})},
    }
    return formfield_overrides


#
# Registration of the fields in the admin panel
#
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["categoryId", "name", "description", ]
    list_display_links = None
    list_editable = ["categoryId", "name", "description", ]

    class Meta:
        model = Categories


class ContentModelAdmin(admin.ModelAdmin):
    """
       Works of the Commission

       It's includes Educational, Methodical works and Graduation project (diploma)
    """

    list_display = ["title", "categoryId", "creationDate", "changingDate", ]  # Display fields
    list_display_links = ["categoryId", "creationDate", "changingDate", ]  # Links on current fields
    list_filter = ["creationDate", "categoryId", ]  # Filter fields
    search_fields = ["title", "article", ]  # Search fields
    list_editable = ["title", ]  # Editable fields

    formfield_overrides = fieldSize(100, 40, 160)

    class Meta:
        model = Content
        fields = '__all__'


class MembersModelAdmin(admin.ModelAdmin):
    list_display = ["categoryId", "name", "position", ]
    list_display_links = ["categoryId", ]
    list_editable = ["name", "position", ]

    formfield_overrides = fieldSize(70, 15, 90)

    class Meta:
        model = CommissionMembers


class MessagesModelAdmin(admin.ModelAdmin):
    list_display = ["name", "themes", "email", "message", "date", ]
    list_filter = ["date", ]
    search_fields = ["name", "themes", "email", "message"]

    formfield_overrides = fieldSize(70, 40, 160)

    class Meta:
        model = Messages


class DisciplinesModelAdmin(admin.ModelAdmin):
    list_display = ["categoryId", "name", "description", ]
    # list_display_links = ["categoryId", ]
    search_fields = ["name", "description", ]
    list_editable = ["name", "description", ]

    formfield_overrides = fieldSize(100, 40, 160)

    class Meta:
        model = Disciplines


class SpecialitiesModelAdmin(admin.ModelAdmin):
    """
       Specialities that are in composition of Commission and manuals on them

    """

    list_display = ["categoryId", "name", "description", ]
    # list_display_links = ["categoryId", ]
    search_fields = ["name", "description", ]
    list_editable = ["name", "description", ]

    formfield_overrides = fieldSize(100, 40, 160)

    class Meta:
        model = Specialities


class ClubsModelAdmin(admin.ModelAdmin):
    list_display = ["categoryId", "name", "description", ]
    list_display_links = None
    search_fields = ["name", "description", ]
    list_editable = ["categoryId", "name", ]

    formfield_overrides = fieldSize(100, 40, 160)

    class Meta:
        model = Disciplines


class ContactsModelAdmin(admin.ModelAdmin):
    list_display = ["categoryId", "title", "contacts", ]
    list_display_links = None
    search_fields = ["title", "contacts", ]
    list_editable = ["categoryId", "title", ]

    formfield_overrides = fieldSize(100, 40, 160)

    class Meta:
        model = Contacts


admin.site.register(Content, ContentModelAdmin)
admin.site.register(Categories, CategoryModelAdmin)
admin.site.register(CommissionMembers, MembersModelAdmin)
admin.site.register(Messages, MessagesModelAdmin)

admin.site.register(Disciplines, DisciplinesModelAdmin)
admin.site.register(Specialities, SpecialitiesModelAdmin)
admin.site.register(Clubs, ClubsModelAdmin)
admin.site.register(Contacts, ContactsModelAdmin)
