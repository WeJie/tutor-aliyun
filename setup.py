import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), "rt", encoding="utf8") as f:
    readme = f.read()


setup(
    name="tutor-aliyun",
    version="0.0.2",
    url="",
    project_urls={
        "Documentation": "",
        "Code": "https://github.com/WeJie/tutor-aliyun",
        "Issue tracker": "https://github.com/WeJie/tutor-aliyun/issues",
        "Community": "",
    },
    license="AGPLv3",
    author="",
    author_email="",
    description="",
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