from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from AdoptSquad.pets.forms import DogBaseForm, CatBaseForm


class TestPetForm(TestCase):
    def setUp(self):
        image_file = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x02\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x00\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x02\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )
        self.valid_data = {
            'name': 'Test Name',
            'years': 3,
            'months': 4,
            'pet_picture': image_file,
            'personality': 'Playful'
        }

        self.invalid_data_1 = {
            'name': None,
            'years': 3,
            'months': 4,
            'pet_picture': image_file,
            'personality': 'Playful'
        }

        self.invalid_data_2 = {
            'name': 'Test Name',
            'years': 3,
            'months': 4,
            'pet_picture': None,
            'personality': 'Playful'
        }

    def test__form_is_valid__expects_true(self):
        form = CatBaseForm(data=self.valid_data, files={'pet_picture': self.valid_data['pet_picture']})
        self.assertTrue(form.is_valid())

        self.valid_data['leash_trained'] = True
        form = DogBaseForm(data=self.valid_data, files={'pet_picture': self.valid_data['pet_picture']})
        self.assertTrue(form.is_valid())

    def test__form_is_valid__expects_false(self):
        form = CatBaseForm(data=self.invalid_data_1, files={'pet_picture': self.invalid_data_1['pet_picture']})
        self.assertFalse(form.is_valid())

        self.invalid_data_1['leash_trained'] = False
        form = DogBaseForm(data=self.invalid_data_1, files={'pet_picture': self.invalid_data_1['pet_picture']})
        self.assertFalse(form.is_valid())

        form = CatBaseForm(data=self.invalid_data_2, files={'pet_picture': self.invalid_data_2['pet_picture']})
        self.assertFalse(form.is_valid())

        self.invalid_data_2['leash_trained'] = False
        form = DogBaseForm(data=self.invalid_data_2, files={'pet_picture': self.invalid_data_2['pet_picture']})
        self.assertFalse(form.is_valid())
