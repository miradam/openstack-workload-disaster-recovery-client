Python bindings to the OpenStack Dragon API
===========================================

This is a client for the OpenStack Dragon API. There's a Python API (the
``dragonclient`` module), and a command-line script (``dragon``). Each
implements 100% of the OpenStack Dragon API.

See the `OpenStack CLI guide`_ for information on how to use the ``dragon``
command-line tool. You may also want to look at the
`OpenStack API documentation`_.

.. _OpenStack CLI Guide: http://docs.openstack.org/cli/quick-start/content/
.. _OpenStack API documentation: http://docs.openstack.org/api/

This code is a fork of Openstack's Heatclient

python-dragonclient is licensed under the Apache License like the OpenStack projects.


.. contents:: Contents:
   :local:

Command-line API
----------------

Installing this package gets you a shell command, ``cinder``, that you
can use to interact with any Rackspace compatible API (including OpenStack).

You'll need to provide your OpenStack username and password. You can do this
with the ``--os-username``, ``--os-password`` and  ``--os-tenant-name``
params, but it's easier to just set them as environment variables::

    export OS_USERNAME=openstack
    export OS_PASSWORD=yadayada
    export OS_TENANT_NAME=myproject

You will also need to define the authentication url with ``--os-auth-url``
and the version of the API with ``--os-volume-api-version``.  Or set them as
environment variables as well::

    export OS_AUTH_URL=http://example.com:8774/v1.1/
    export OS_VOLUME_API_VERSION=1

If you are using Keystone, you need to set the OS_AUTH_URL to the keystone
endpoint::

    export OS_AUTH_URL=http://example.com:5000/v2.0/

Since Keystone can return multiple regions in the Service Catalog, you
can specify the one you want with ``--os-region-name`` (or
``export OS_REGION_NAME``). It defaults to the first in the list returned.

You'll find complete documentation on the shell by running
``dragon help``::

    usage: dragon [--debug] [--os-username <auth-user-name>]
                  [--os-password <auth-password>]
                  [--os-tenant-name <auth-tenant-name>] [--os-auth-url <auth-url>]
                  [--os-region-name <region-name>] [--service-type <service-type>]
                  [--service-name <service-name>]
                  [--volume-service-name <volume-service-name>]
                  [--endpoint-type <endpoint-type>]
                  [--os-volume-api-version <compute-api-ver>]
                  [--os-cacert <ca-certificate>] [--retries <retries>]
                  <subcommand> ...

    Command-line interface to the OpenStack Dragon API.
	Please see doc section in Dragon project
