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


Check if kustomization.yml file is right.::

    kubectl kustomize "$(tutor config printroot)/env"

