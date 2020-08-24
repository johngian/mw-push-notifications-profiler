import setuptools

setuptools.setup(
    name="mw_push_profiler",
    version="0.1",
    packages=setuptools.find_packages(),
    install_requires=["locust", "requests", "python-decouple"],
)
