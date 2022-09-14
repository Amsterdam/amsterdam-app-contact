import mimetypes
from django.http import HttpResponse
from amsterdam_app_backend.settings import BASE_DIR


def static(request):
    path = request.path
    save_path = path.replace('..', '')
    filepath = '{base_dir}{save_path}'.format(base_dir=BASE_DIR, save_path=save_path)
    mimetype = mimetypes.guess_type(filepath, strict=True)[0]
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return HttpResponse(content, content_type=mimetype, status=200)
    except Exception as error:
        pass

    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        return HttpResponse(content, content_type=mimetype, status=200)
    except Exception as error:
        pass
    return HttpResponse(status=404)
