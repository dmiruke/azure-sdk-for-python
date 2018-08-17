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


class Email(Model):
    """Email Address details.

    :param detected: Detected Email Address from the input text content.
    :type detected: str
    :param sub_type: Subtype of the detected Email Address.
    :type sub_type: str
    :param text: Email Address in the input text content.
    :type text: str
    :param index: Index(Location) of the Email address in the input text
     content.
    :type index: int
    """

    _attribute_map = {
        'detected': {'key': 'Detected', 'type': 'str'},
        'sub_type': {'key': 'SubType', 'type': 'str'},
        'text': {'key': 'Text', 'type': 'str'},
        'index': {'key': 'Index', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Email, self).__init__(**kwargs)
        self.detected = kwargs.get('detected', None)
        self.sub_type = kwargs.get('sub_type', None)
        self.text = kwargs.get('text', None)
        self.index = kwargs.get('index', None)