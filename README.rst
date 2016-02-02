========================
The DataShed Annotations
========================

django-annotations
------------------

Forked from `django-annotations <https://github.com/PsypherPunk/django-annotations>`_
. Django implementation of `annotatorjs Storage <http://annotatorjs.org/>`_.


Implements most of the methods as per the `Core Storage API <http://docs.annotatorjs.org/en/v1.2.x/storage.html#core-storage-api>`_ documentation (``root``, ``index``, ``create``, ``read``, ``update``, ``delete`` and ``search``).

To see a working demo:

.. code:: bash

    virtualenv annotatorjs
    cd annotatorjs
    source bin/activate
    git clone https://github.com/PsypherPunk/django-annotations.git
    cd django-annotations
    pip install -r requirements/base.txt
    ./manage.py migrate
    ./manage.py runserver

A demo. page will then be available at ``/demo``.

enqueue
-------

Simply accepts a ``HTTP POST`` to ``/enqueue``, passing the request body onto an RQ worker. The worked should be started via:

.. code:: bash

    ./manage.py rqworker default

The worker itself is configured via the ``RQ_QUEUES`` settings in ``annotator.settings.base``.

