# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedInstanceUpdate(Model):
    """An update request for an Azure SQL Database managed instance.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param sku: Managed instance sku
    :type sku: ~azure.mgmt.sql.models.Sku
    :ivar fully_qualified_domain_name: The fully qualified domain name of the
     managed instance.
    :vartype fully_qualified_domain_name: str
    :param administrator_login: Administrator username for the managed
     instance. Can only be specified when the managed instance is being created
     (and is required for creation).
    :type administrator_login: str
    :param administrator_login_password: The administrator login password
     (required for managed instance creation).
    :type administrator_login_password: str
    :param subnet_id: Subnet resource ID for the managed instance.
    :type subnet_id: str
    :ivar state: The state of the managed instance.
    :vartype state: str
    :param license_type: The license type. Possible values are
     'LicenseIncluded' and 'BasePrice'.
    :type license_type: str
    :param v_cores: The number of VCores.
    :type v_cores: int
    :param storage_size_in_gb: The maximum storage size in GB.
    :type storage_size_in_gb: int
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'fully_qualified_domain_name': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'fully_qualified_domain_name': {'key': 'properties.fullyQualifiedDomainName', 'type': 'str'},
        'administrator_login': {'key': 'properties.administratorLogin', 'type': 'str'},
        'administrator_login_password': {'key': 'properties.administratorLoginPassword', 'type': 'str'},
        'subnet_id': {'key': 'properties.subnetId', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'license_type': {'key': 'properties.licenseType', 'type': 'str'},
        'v_cores': {'key': 'properties.vCores', 'type': 'int'},
        'storage_size_in_gb': {'key': 'properties.storageSizeInGB', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, sku=None, administrator_login: str=None, administrator_login_password: str=None, subnet_id: str=None, license_type: str=None, v_cores: int=None, storage_size_in_gb: int=None, tags=None, **kwargs) -> None:
        super(ManagedInstanceUpdate, self).__init__(**kwargs)
        self.sku = sku
        self.fully_qualified_domain_name = None
        self.administrator_login = administrator_login
        self.administrator_login_password = administrator_login_password
        self.subnet_id = subnet_id
        self.state = None
        self.license_type = license_type
        self.v_cores = v_cores
        self.storage_size_in_gb = storage_size_in_gb
        self.tags = tags