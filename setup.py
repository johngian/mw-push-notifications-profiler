import setuptools

setuptools.setup(
    name="mw_push_notifications_profiler",
    version="0.1",
    package_dir={'mw_push_notifications_profiler': 'src'},
    packages=['mw_push_notifications_profiler'],
    install_requires=["locust", "requests", "python-decouple"],
)
