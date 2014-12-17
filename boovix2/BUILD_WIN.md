wxWidgets
---------
Download and install the Windows installer:
http://www.wxwidgets.org/downloads/
eg. wxMSW-3.0.2-Setup.exe
Install it to third_party/wxwidgets/
(not third_party/wxwidgets/wxWidgets-3.0.2)

Go to third_party/wxwidgets/build/msw/
Open wx_vc12.sln and build Debug/static and Release/static

...

libcurl
-------
Building libcurl with openssl.

The structure is following:
third_party/libcurl/curl/
third_party/libcurl/openssl/

Download curl: http://curl.haxx.se/download.html

Go to curl/projects/

Download openssl: https://www.openssl.org/source/

Install perl (comes with git binaries)

Patch openssl mk1mf.pl script:
http://stackoverflow.com/questions/7680189/openssl-cant-build-in-vc-2010

Run curl/projects/build-openssl.bat vc10 x86 release openssl-1.0.1j\

Move openssl directory. Both curl and openssl should be next to each other
and their names should be like this:
curl/
curl/projects/
openssl/
openssl/build/

Open curl/projects/windows/vc10/lib/libcurl.sln and fed the preprocessor
    with USE_OPENSSL, see: http://stackoverflow.com/questions/197444/

...
