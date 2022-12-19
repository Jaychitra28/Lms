from django.test import TestCase
from django.urls import reverse
from tests.courses.test_model_mixin import Modelmixin
from courses.models import Subject, Course, Module
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, User


class TestListView(Modelmixin, TestCase):
    def test_course_list_tamplate_used(self):
        permission = Permission.objects.get(name="Can view course")
        self.user.user_permissions.add(permission)
        self.client.login(username="jai", password="123")
        response = self.client.get((reverse("course:manage_course_list")))
        self.assertTemplateUsed(response, "courses/manage/course/list.html")

    def test_course_DeleteView_tamplate_used(self):
        permission = Permission.objects.get(name="Can delete course")
        self.user.user_permissions.add(permission)
        self.client.login(username="jai", password="123")
        response = self.client.get(
            (reverse("course:delete", args=[self.user.id]))
        )
        self.assertTemplateUsed(response, "courses/manage/course/delete.html")

    def test_module_update_template_used(self):
        self.client.login(username="jai", password="123")
        response = self.client.get(
            reverse("course:module_update", args=[self.course1.pk])
        )
        self.assertTemplateUsed(response, "courses/manage/module/formset.html")

    def test_module_content_list_template_used(self):
        self.create_modules(1)
        self.client.login(username="maddy", password="123")
        response = self.client.get(
            reverse("course:module_content_list", args=[self.course1.pk])
        )
        self.assertTemplateUsed(
            response, "courses/manage/module/content_list.html"
        )
