from django.test import TestCase
from django.urls import resolve, reverse
from tests.courses.test_model_mixin import Modelmixin
from courses.views import (
    ManageCourseListView,
    CourseDeleteView,
    CourseCreateView,
    CourseUpdateView,
    CourseModuleUpdateView,
    ModuleContentListView,
    ContentCreateUpdateView,
)


class TestUrls(Modelmixin, TestCase):
    def test_Manage_Course_ListView_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:manage_course_list")).func.view_class,
            ManageCourseListView,
        )

    def test_Course_CreateView_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:create")).func.view_class, CourseCreateView
        )

    def test_Course_UpdateView_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:edit", args=[self.id])).func.view_class,
            CourseUpdateView,
        )

    def test_Course_DeleteView_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:delete", args=[self.id])).func.view_class,
            CourseDeleteView,
        )

    def test_course_module_updateview_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:module_update", args=[self.course1.pk])
            ).func.view_class,
            CourseModuleUpdateView,
        )

    def test_module_content_list_view_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:module_content_list", args=[self.course1.pk])
            ).func.view_class,
            ModuleContentListView,
        )

    def test_text_content_create_view_is_resolved(self):
        module = self.create_modules(1).first()
        self.assertEqual(
            resolve(
                reverse(
                    "course:module_content_create", args=[module.id, "text"]
                )
            ).func.view_class,
            ContentCreateUpdateView,
        )

    def test_image_content_create_view_is_resolved(self):
        module = self.create_modules(1).first()
        self.assertEqual(
            resolve(
                reverse(
                    "course:module_content_create", args=[module.id, "image"]
                )
            ).func.view_class,
            ContentCreateUpdateView,
        )

    def test_video_content_create_view_is_resolved(self):
        module = self.create_modules(1).first()
        self.assertEqual(
            resolve(
                reverse(
                    "course:module_content_create", args=[module.id, "video"]
                )
            ).func.view_class,
            ContentCreateUpdateView,
        )

    def test_file_content_create_view_is_resolved(self):
        module = self.create_modules(1).first()
        self.assertEqual(
            resolve(
                reverse(
                    "course:module_content_create", args=[module.id, "file"]
                )
            ).func.view_class,
            ContentCreateUpdateView,
        )
