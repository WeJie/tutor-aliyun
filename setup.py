import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()


setup(
    name="tutor-aliyun",
    version="0.0.2",
    url="https://github.com/WeJie/tutor-aliyun",
    project_urls={
        "Documentation": "https://github.com/WeJie/tutor-aliyun",
        "Code": "https://github.com/WeJie/tutor-aliyun",
        "Issue tracker": "https://github.com/WeJie/tutor-aliyun/issues",
        "Community": "https://github.com/WeJie/tutor-aliyun",
    },
    license="AGPLv3",
    author="weijie",
    author_email="wejie00@foxmail.com",
    description="Aliyun plugin for Tutor, for deploying edx instance to aliyun by tutor",
    long_description=readme,
    packages=["tutoraliyun"],
    include_package_data=True,
    python_requires=">=3.5",
    entry_points={"tutor.plugin.v0": ["aliyun = tutoraliyun.plugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
