from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from AdoptSquad.pets.models import Dog, Cat


class TestPetDeleteView(TestCase):
    def setUp(self):
        image_file = SimpleUploadedFile(
            name='test_image.gif',
            content=b'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x00\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;',
            content_type='image/gif'
        )

        self.dog = Dog.objects.create(
            name='Test Name1',
            years=3,
            months=4,
            pet_picture=image_file,
            personality='Playful',
            leash_trained=True
        )

        self.cat = Cat.objects.create(
            name='Test Name2',
            years=3,
            months=4,
            pet_picture=image_file,
            personality='Playful'
        )

    def test__cat_delete_redirect(self):
        response = self.client.post(reverse('cats-delete', args=[self.cat.pk]))

        self.assertRedirects(response, reverse('cats-list'))

        self.assertFalse(Cat.objects.filter(id=self.cat.pk).exists())

    def test__dog_delete_redirect(self):
        response = self.client.post(reverse('dogs-delete', args=[self.dog.pk]))

        self.assertRedirects(response, reverse('dogs-list'))

        self.assertFalse(Dog.objects.filter(id=self.dog.pk).exists())
