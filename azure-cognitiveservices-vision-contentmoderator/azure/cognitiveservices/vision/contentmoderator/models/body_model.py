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


class BodyModel(Model):
    """BodyModel.

    :param data_representation:  Default value: "URL" .
    :type data_representation: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'data_representation': {'key': 'DataRepresentation', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BodyModel, self).__init__(**kwargs)
        self.data_representation = kwargs.get('data_representation', "URL")
        self.value = kwargs.get('value', None)