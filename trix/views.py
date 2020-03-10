from django.http import JsonResponse
from django.views.generic import View

from trix.forms import AttachmentForm
from .utils import is_valid_image_extension


class AttachmentView(View):
    def post(self, request, *args, **kwargs):
        form = AttachmentForm(self.request.POST, self.request.FILES)

        uploaded_attachment = request.FILES['file']

        if is_valid_image_extension(uploaded_attachment):
            if form.is_valid():
                photo = form.save()
                data = {'valid': 'true', 'url': photo.file.url}
            else:
                data = {'valid': 'false', 'msg': 'not Valid'}
            return JsonResponse(data)
        else:
            data = {'valid': 'false', 'msg': 'file type not Valid'}
            return JsonResponse(data)
