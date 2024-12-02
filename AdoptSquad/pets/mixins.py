class CatBaseViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_type'] = 'cat'

        return context


class DogBaseViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pet_type'] = 'dog'

        return context
