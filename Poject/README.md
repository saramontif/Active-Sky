# Django QR Code
[![Latest PyPI version](https://badge.fury.io/py/django-qr-code.svg)](https://badge.fury.io/py/django-qr-code)
[![Documentation Status](https://readthedocs.org/projects/django-qr-code/badge/?version=latest)](http://django-qr-code.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.org/dprog-philippe-docourt/django-qr-code.svg?branch=master)](https://travis-ci.org/dprog-philippe-docourt/django-qr-code)
[![Maintainability](https://api.codeclimate.com/v1/badges/c47e79bf51f6a2bb8264/maintainability)](https://codeclimate.com/github/dprog-philippe-docourt/django-qr-code/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/dprog-philippe-docourt/django-qr-code/badge.svg?branch=master)](https://coveralls.io/github/dprog-philippe-docourt/django-qr-code?branch=master)

This is an application that provides tools for displaying QR codes on your [Django](https://www.djangoproject.com/) site.

This application depends on the [qrcode](https://github.com/lincolnloop/python-qrcode) python library which requires the [Pillow](https://github.com/python-pillow/Pillow) library in order to support the PNG image format.
The Pillow library needs to be installed manually if you want to generate QR codes in PNG format; otherwise, SVG is the only supported format.

This app makes no usage of the Django models and therefore do not use any database.

Only Python >= 3.5 is supported.

## Installation

### Binary Package from PyPi
In order to use this app in a Django project, the simplest way is to install it from [PyPi](https://pypi.python.org/pypi/django-qr-code):
```bash
pip install django-qr-code
```

### From the Source Code
In order to modify or test this app you may want to install it from the source code.

Clone the [GitHub repository](https://github.com/dprog-philippe-docourt/django-qr-code) and then run:
```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
```

## Usage
Start by adding `qr_code` to your `INSTALLED_APPS` setting like this:
```python
INSTALLED_APPS = (
    ...,
    'qr_code',
)
```

You need to load the tags provided by this app in your template with:
```djangotemplate
{% load qr_code %}
```

The source code on [GitHub](https://github.com/dprog-philippe-docourt/django-qr-code) contains a simple demo app. Please check out the [templates folder](https://github.com/dprog-philippe-docourt/django-qr-code/tree/master/qr_code_demo/templates/qr_code_demo) for an example of template, and the [setting](https://github.com/dprog-philippe-docourt/django-qr-code/tree/master/demo_site/settings.py) and [urls](https://github.com/dprog-philippe-docourt/django-qr-code/tree/master/demo_site/urls.py) files for an example of configuration and integration.

### qr_from_text
The tag `qr_from_text` generates an embedded `svg` or `img` tag within the HTML code produced by your template.

The following renders a tiny "hello world" QR code with a `svg` tag:
```djangotemplate
{% qr_from_text "Hello World!" size="T" %}
```
Here is a medium "hello world" QR code with an `img` tag:
```djangotemplate
{% qr_from_text "Hello World!" size="m" image_format="png" error_correction="L" %}
```

The `size` parameter gives the size of each module of the QR code matrix. It can be either a positive integer or one of the following letters:
* t or T: tiny (value: 6)
* s or S: small (value: 12)
* m or M: medium (value: 18)
* l or L: large (value: 30)
* h or H: huge (value: 48)

For PNG image format the size unit is in pixels, while the unit is 0.1 mm for SVG format.

Here is a "hello world" QR code using the version 12:
```djangotemplate
{% qr_from_text "Hello World!" size=8 version=12 %}
```
The `version` parameter is an integer from 1 to 40 that controls the size of the QR code matrix. Set to None to determine this automatically. The smallest, version 1, is a 21 x 21 matrix. The biggest, version 40, is 177 x 177 matrix. The size grows by 4 modules/side.

Here is a "hello world" QR code using a border of 6 modules:
```djangotemplate
{% qr_from_text "Hello World!" size=10 border=6 %}
```
The `border` parameter controls how many modules thick the border should be (the default is 4, which is the minimum according to the specs).

There are 4 error correction levels used for QR codes, with each one adding different amounts of "backup" data
depending on how much damage the QR code is expected to suffer in its intended environment, and hence how much
error correction may be required. The correction level can be configured with the `error_correction` parameter as follow:
* l or L: error correction level L – up to 7% damage
* m or M: error correction level M – up to 15% damage
* q or Q: error correction level Q – up to 25% damage
* h or H: error correction level H – up to 30% damage

Alternatively, you may use the `options` keyword argument with an instance of `QRCodeOptions` as value instead of listing every requested options. Here is a example of view: 
```python
from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions

def myview(request):
    # Build context for rendering QR codes.
    context = dict(
        my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
    )

    # Render the view.
    return render(request, 'myapp/myview.html', context=context)
```

and an example of template for the view above:
```djangotemplate
{% qr_from_text "Hello World!" options=my_options %}
```

### qr_url_from_text
The `qr_url_from_text` tag generates an url to an image representing the QR code. It comes with the same options as `qr_from_text` to customize the image format (SVG or PNG), the size, the border and the matrix size. It also has an additional option **cache_enabled** to disable caching of served image.

The image targeted by the generated URL is served by a view provided in `qr_code.urls`. Therefore you need to include the URLs provided by `qr_code.urls` in your app in order to make this tag work. This can be achieved with something like this:
```python
from django.conf.urls import include, url
from qr_code import urls as qr_code_urls

urlpatterns = [
    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
]
```

A large QR code (version 40) requires 0.7 second to be generated on a powerful machine (2017), and probably more than one second on a really cheap hosting.
The image served by the *qr_code* app can be cached to improve performances and reduce CPU usage required to generate the QR codes.
In order to activate caching, you simply need to declare a cache alias with the setting `QR_CODE_CACHE_ALIAS` to indicate in which cache to store the generated QR codes.

For instance, you may declare an additional cache for your QR codes like this in your Django settings:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'qr-code': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'qr-code-cache',
        'TIMEOUT': 3600
    }
}

QR_CODE_CACHE_ALIAS = 'qr-code'

```

The `QR_CODE_CACHE_ALIAS = 'qr-code'` tells the *qr_code* app to use that cache for storing the generated QR codes.
All QR codes will be cached with the specified *TIMEOUT* when a non empty value is set to `QR_CODE_CACHE_ALIAS`.
If you want to activate the cache for QR codes, but skip the caching for some specific codes, you can use the keyword argument `cache_enabled=False` when using `qr_url_from_text`.

Here is a medium "hello world" QR code that uses an URL to serve the image in SVG format:
```djangotemplate
<img src="{% qr_url_from_text "Hello World!" %}" alt="Hello World!">
```
Here is a "hello world" QR code in version 10 that uses an URL to serve the image in PNG format:
```djangotemplate
<img src="{% qr_url_from_text "Hello World!" size=8 version=10 image_format='png' %}" alt="Hello World!">
```

Here is a "hello world" QR code in version 20 with an error correction level Q (25% of redundant data) that uses an URL to serve the image in SVG format, and disable caching for served image:
```djangotemplate
<img src="{% qr_url_from_text "Hello World!" size=8 version=20 error_correction="Q" cache_enabled=False %}" alt="Hello World!">
```

The default settings protect the URLs that serve images against external requests, and thus against possibly easy DOS attacks.
However, if you are interested in providing those images as a service, there is a setting named `ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER` to open access to some controlled users.
This setting tells who can bypass the random token protection. It can be a boolean value used for any authenticated user, or a callable that takes a user as only parameter.
Note that setting this option to `True` will only accept authenticated users. However, setting this option to a callable that always return `True` (even for anonymous users) will allow anyone to access those URLs from outside your Django app.

Here are the available settings to manage the protection for served images:
```python
QR_CODE_URL_PROTECTION = {
    'TOKEN_LENGTH': 30,                         # Optional random token length for URL protection. Defaults to 20.
    'SIGNING_KEY': 'my-secret-signing-key',     # Optional signing key for URL token. Uses SECRET_KEY if not defined.
    'SIGNING_SALT': 'my-signing-salt',          # Optional signing salt for URL token.
    'ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER': True  # Tells whether a registered user can request the QR code URLs from outside a site that uses this app. It can be a boolean value used for any user or a callable that takes a user as parameter. Defaults to False (nobody can access the URL without the security token).
}
```

### QR Codes for Apps
Aside from generating a QR code from a given text, you can also generate codes for specific application purposes, that a reader can interpret as an action to take: open a mail client to send an email to a given address, add a contact to your phone book, connect to a Wi-Fi, start a SMS, etc.  See [this documentation](https://github.com/zxing/zxing/wiki/Barcode-Contents) about what a QR code can encode.

Django QR Code proposes several utility tags to ease the generation of such codes, without having to build the appropriate text representation for each action you need. This remove the hassle of reading the specifications and handling all the required escaping for reserved chars.

Please note that some commands are common patterns, rather than formal specifications. Therefore, there is no guarantee that all QR code readers will handle them properly.

The following tags targeting apps are available:
* `qr_for_email` and `qr_url_for_email`
* `qr_for_tel` and `qr_url_for_tel`
* `qr_for_sms` and `qr_url_for_sms`
* `qr_for_geolocation` and `qr_url_for_geolocation`
* `qr_for_google_maps` and `qr_url_for_google_maps`
* `qr_for_youtube` and `qr_url_for_youtube`
* `qr_for_google_play` and `qr_url_for_google_play`
* `qr_for_contact` and `qr_url_for_contact`
* `qr_for_wifi` and `qr_url_for_wifi`


You could write a view like this:
```python
from datetime import date
from django.shortcuts import render    
from qr_code.qrcode.utils import ContactDetail, WifiConfig, Coordinates, QRCodeOptions

def index(request):
    # Use a ContactDetail instance to encapsulate the detail of the contact.
    contact_detail = ContactDetail(
        first_name='John',
        last_name='Doe',
        first_name_reading='jAAn',
        last_name_reading='dOH',
        tel='+41769998877',
        email='j.doe@company.com',
        url='http://www.company.com',
        birthday=date(year=1985, month=10, day=2),
        address='Cras des Fourches 987, 2800 Delémont, Jura, Switzerland',
        memo='Development Manager',
        org='Company Ltd',
    )

    # Use a WifiConfig instance to encapsulate the configuration of the connexion.
    wifi_config = WifiConfig(
        ssid='my-wifi',
        authentication=WifiConfig.AUTHENTICATION.WPA,
        password='wifi-password'
    )

    # Build coordinates instances.
    google_maps_coordinates = Coordinates(latitude=586000.32, longitude=250954.19)
    geolocation_coordinates = Coordinates(latitude=586000.32, longitude=250954.19, altitude=500)

    # Build context for rendering QR codes.
    context = dict(
        contact_detail=contact_detail,
        wifi_config=wifi_config,
        video_id='J9go2nj6b3M',
        google_maps_coordinates=google_maps_coordinates,
        geolocation_coordinates=geolocation_coordinates,
        options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
    )

    # Render the index page.
    return render(request, 'qr_code_demo/index.html', context=context)
```

Then, in your template, you can render the appropriate QR codes for the given context:
```djangotemplate
<h3>Add contact '{{ contact_detail.first_name }} {{ contact_detail.last_name }}' to phone book</h3>
{% qr_for_contact contact_detail=contact_detail size='S' %}
<p>or:</p>
{% qr_for_contact contact_detail size='S' %}
<p>or:</p>
{% qr_for_contact contact_detail options=options_example %}

<h3>Configure Wi-Fi connexion to '{{ wifi_config.ssid }}'</h3>
<img src="{% qr_url_for_wifi wifi_config=wifi_config size='T' error_correction='Q' %}">
<p>or:</p>
<img src="{% qr_url_for_wifi wifi_config size='T' error_correction='Q' %}">
<p>or:</p>
<img src="{% qr_url_for_wifi wifi_config options=options_example %}">

<h3>Watch YouTube video '{{ video_id }}'</h3>
{% qr_for_youtube video_id image_format='png' size='T' %}
<p>or:</p>
{% qr_for_youtube video_id options=options_example %}

<h3>Open map at location: ({{ geolocation_coordinates }})</h3>
<img src="{% qr_url_for_geolocation coordinates=geolocation_coordinates %}">
<p>or:</p>
<img src="{% qr_url_for_geolocation latitude=geolocation_coordinates.latitude longitude=geolocation_coordinates.longitude altitude=geolocation_coordinates.altitude %}">
<p>or:</p>
<img src="{% qr_url_for_geolocation latitude=geolocation_coordinates.latitude longitude=geolocation_coordinates.longitude altitude=geolocation_coordinates.altitude options=options_example %}">

<h3>Open Google Maps App at location: ({{ google_maps_coordinates }})</h3>
{% qr_for_google_maps coordinates=google_maps_coordinates %}
<p>or:</p>
{% qr_for_google_maps latitude=google_maps_coordinates.latitude longitude=google_maps_coordinates.longitude %}
<p>or:</p>
{% qr_for_google_maps latitude=google_maps_coordinates.latitude longitude=google_maps_coordinates.longitude options=options_example %}
```

Please check-out the [demo application](#demo-application) to see more examples.

## Notes

### Image Formats
The SVG is the default image format.
It is a vectorial format so it can be scaled as wanted.
However, it has two drawbacks. The size is not given in pixel, which can be problematic if the design of your website relies on a fixed width (in pixels).
The format is less compact than PNG and results in a larger HTML content. Note that a base64 PNG is less compressible than a SVG tag, so it might not matter that much of you use HTML compression on your web server.

SVG has [broad support](http://caniuse.com/#feat=svg) now and it will work properly on any modern web browser.

### qr_from_text vs qr_url_from_text
The tag `qr_url_from_text` has several advantages over `qr_from_text`, despite the fact that it requires a bit more of writing:
* the generated HTML code does not contain heavy inline image data (lighter and cleaner content)
* the generated images can be cached (served with a separate HTML request)
* the HTML tag used to render the QR code is always an `<img>` tag, which may simplify CSS handling
* the HTML tag embedding the image is not generated for you, which allows for customization of attributes (*height*, *width*, *alt*)
* the page can be loaded asynchronously, which improves responsiveness
* you can provide links to QR codes instead of displaying them, which is not possible with `qr_from_text`

One disadvantage of `qr_url_from_text` is that it increases the number of requests to the server (one request to serve the page containing the URL and another to request the image.

Be aware that serving image files (which are generated on the fly) from an URL can be abused and lead to DOS attack pretty easily, for instance by requesting very large QR codes from outside your application.
This is the reason why the associated setting `ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER` in `QR_CODE_URL_PROTECTION` defaults to completely forbid external access to the API. Be careful when opening external access.

### QR Codes Caching
Caching QR codes reduces CPU usage, but the usage of `qr_url_from_text` (which caching depends on) increases the number of requests to the server (one request to serve the page containing the URL and another to request the image).

Moreover, be aware that the largest QR codes, in version 40 with a border of 4 modules and rendered in SVG format, have a size of ~800 KB.
Be sure that your cache options are reasonable and can be supported by your server(s), especially for in-memory caching.

Note that even without caching generated QR codes, the app will return a *HTTP 304 Not Modified* status code whenever the same QR code is requested again by the same user.

## Demo Application
If you want to try this app, you may want to use the demo application shipped alongside the source code.

Get the source code from [GitHub](https://github.com/dprog-philippe-docourt/django-qr-code), follow the [installation instructions](#from-the-source-code) above, and run the `runserver` command of Django:
```bash
python manage.py runserver
```
The demo application should be running at <http://127.0.0.1:8000/>.

If you have [Docker Compose](https://docs.docker.com/compose/) installed, you can simply run the following from a terminal (this will save you the burden of setting up a proper python environment):
```bash
cd scripts
./run-demo-app.sh
```
The demo application should be running at <http://127.0.0.1:8910/>.

## Testing
Get the source code from [GitHub](https://github.com/dprog-philippe-docourt/django-qr-code), follow the [installation instructions](#from-the-source-code) above, and run the `test` command of Django:
```bash
python manage.py test
```
This will run the test suite with the locally installed version of Python and Django.

If you have [Docker Compose](https://docs.docker.com/compose/) installed, you can simply run the following from a terminal (this will save you the burden of setting up a proper python environment):
```bash
cd scripts
./run-tests.sh
```
This will run the test suite with all supported versions of Python and Django. The test results are stored within `tests_result.txt`.