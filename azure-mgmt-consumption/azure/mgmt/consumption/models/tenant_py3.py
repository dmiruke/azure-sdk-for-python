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

from .resource_py3 import Resource


class Tenant(Resource):
    """An tenant detail resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar billing_profile_name: The Billing Profile name.
    :vartype billing_profile_name: str
    :ivar billing_account_id: The Billing AccountId.
    :vartype billing_account_id: str
    :ivar tenant_id: The TenantId.
    :vartype tenant_id: str
    :ivar billing_account_name: The Billing Account Name.
    :vartype billing_account_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'billing_profile_name': {'readonly': True},
        'billing_account_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'billing_account_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_profile_name': {'key': 'properties.billingProfileName', 'type': 'str'},
        'billing_account_id': {'key': 'properties.billingAccountId', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'billing_account_name': {'key': 'properties.billingAccountName', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Tenant, self).__init__(**kwargs)
        self.billing_profile_name = None
        self.billing_account_id = None
        self.tenant_id = None
        self.billing_account_name = None
