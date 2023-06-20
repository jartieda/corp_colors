from setuptools import setup, find_packages

exec(open('corpcolors/version.py').read())

setup(
    name='corpcolors',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'corpcolors': [
            'templates/admin/base_site.html',
            'static/corpcolors/css/base.css',
            'static/admin/img/calendar-icons.svg',
            'static/admin/img/icon-addlink.svg',
            'static/admin/img/icon-addlink-black.svg',
            'static/admin/img/icon-alert.svg',
            'static/admin/img/icon-calendar.svg',
            'static/admin/img/icon-changelink.svg',
            'static/admin/img/icon-clock.svg',
            'static/admin/img/icon-unknown.svg',
            'static/admin/img/icon-viewlink.svg',
            'static/admin/img/icon-yes.svg',
            'static/admin/img/icon-search.svg',
            'static/admin/img/selector-icons.svg',
            'static/admin/img/sorting-icons.svg',
            'static/admin/img/tooltag-add.svg',
            'static/admin/img/tooltag-arrowright.svg',
        ], },
    install_requires=[
        'Django>=3.2',
    ],
    license='MIT',
    author='Debora Peralta',
    author_email='debora199318@gmail.com.com',
    description='Guia de estilos corporativos aplicables al admin de Django',
    url='https://github.com/Debbiepimpo/corp-colors',
    download_url='https://github.com/Debbiepimpo/corp-colors/archive/%s.tar.gz' % __version__,
)
