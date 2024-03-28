from django.contrib import admin
from courses.models import Category, Course, Lesson
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import cloudinary

class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CoursesAdmin(admin.ModelAdmin):
    list_display = ["id","name","created_date","active","updated_date"]
    search_fields = ["name"]
    list_filter = ["id","name","created_date"]
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, course):
        if course.image:
            if type(course.image) is cloudinary.CloudinaryResource:
                return mark_safe(f"<img width='300' src='{course.image.url}' />")
            return mark_safe(f"<img width='300' src='/static/{course.image.name}' />")

    class Media:
        css = {
            'all': ['/static/css/style.css']
        }

# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CoursesAdmin)
admin.site.register(Lesson)