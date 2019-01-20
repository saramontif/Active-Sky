# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# data = [u"geeksforgeeks", u"https://www.geeksforgeeks.org/"]
# qr.add_data(data)
# qr.make(fit=True)
#
# img = qr.make_image(fill_color="black", back_color="white")
# print(img)
# img.save("image.jpg")
from django.http import HttpResponse


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)