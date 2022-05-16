from django.contrib import admin

# Register your models here.
from project.models import Person, Musician, Album, Student, Teacher, Group, GroupStudents

admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(GroupStudents)
# admin.site.register(Group)


@admin.register(Group)
class Groups(admin.ModelAdmin):
    fields = ('title','teacher')
    list_display = ('id', 'title', 'teacher', "list_of_students")

    def list_of_students(self, obj):
        qs = GroupStudents.objects.filter(groups=obj.id)
        res = []
        for x in qs:
            x = str(x)[:-8]
            res.append(x)
        return   res