
from rest_framework import serializers
from project.models import Group, GroupStudents, Teacher, Student


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title')



class GroupStudentsserializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudents
        fields = ('student',)





class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'teacher', 'groups')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # print(representation['groups'])
        # representation['student'] = GroupStudentsserializer(
        #     instance.groups.all(), many=True
        # ).data
        representation['teacher'] = TeacherSerializer(Teacher.objects.get(id=instance.teacher.id)).data
        keys = []
        for i in representation['groups']:
            keys.append(GroupStudentsserializer(GroupStudents.objects.get(id=i)).data)
        res = []
        for x in keys:
            res.append(StudentSerializer(Student.objects.get(id=x['student'])).data)
        representation['groups'] = res
        return representation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'