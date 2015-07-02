from setuptools import setup

setup(
    name="queueit",
    version="1.2",
    author="Anton P. Linevich",

    packages=['queueit'],

    install_requires=[
        'beanstalkc',
    ],

    entry_points={
        'console_scripts': [
            'q-peek = queueit:main',
            'q-peek-ready = queueit:main',
            'q-peek-delayed = queueit:main',
            'q-peek-buried = queueit:main',
            'q-get = queueit:main',
            'q-kick = queueit:main',
            'q-put = queueit:main',
            'q-stat = queueit:main',
            'q-wrapper = queueit:main'
        ]
    }
)
