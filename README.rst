.. image:: https://badge.fury.io/py/tutor-aliyun.svg
    :target: https://pypi.org/project/tutor-aliyun/

Aliyun plugin for `Tutor <https://docs.tutor.overhang.io>`_
============================================================

This is a plugin for `Tutor <https://docs.tutor.overhang.io>`_ that make `tutor k8s` can deploy edx on aliyun kubernetes service.


Installation
------------

This plugin requires tutor>=3.6.0. Also, you should have installed tutor from source, and not from a pre-compiled binary.

::

    pip install tutor-aliyun

Then, to enable this plugin, run::

    tutor plugins enable aliyun 

You will have to re-generate the environment::

    tutor config save

Then deploy to k8s cluster::

    tutor k8s quickstart 

Set true to ALIYUN_USE_NAS_STORAGE in config.yml, if you want to use NAS(Network Attached Storage)::
    ALIYUN_USE_NAS_STORAGE: true

Check if kustomization.yml file is right.::

    kubectl kustomize "$(tutor config printroot)/env"

