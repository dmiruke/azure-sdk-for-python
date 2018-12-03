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


class AlertsSummaryGroupItem(Model):
    """Alerts summary group item.

    :param name: Value of the aggregated field
    :type name: str
    :param count: Count of the aggregated field
    :type count: int
    :param groupedby: Name of the field aggregated
    :type groupedby: str
    :param values: List of the items
    :type values:
     list[~azure.mgmt.alertsmanagement.models.AlertsSummaryGroupItem]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'groupedby': {'key': 'groupedby', 'type': 'str'},
        'values': {'key': 'values', 'type': '[AlertsSummaryGroupItem]'},
    }

    def __init__(self, *, name: str=None, count: int=None, groupedby: str=None, values=None, **kwargs) -> None:
        super(AlertsSummaryGroupItem, self).__init__(**kwargs)
        self.name = name
        self.count = count
        self.groupedby = groupedby
        self.values = values