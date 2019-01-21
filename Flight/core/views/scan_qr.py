from django.views.generic import TemplateView


class ScanQr(TemplateView):
    template_name = 'scan_qr_code.html'
