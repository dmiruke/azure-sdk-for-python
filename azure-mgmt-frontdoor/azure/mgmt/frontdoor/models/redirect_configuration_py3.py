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


class RedirectConfiguration(Model):
    """The configuration for a redirect routing rule. This object is needed only
    if the type property of RoutingRule is set to Redirect. .

    :param redirect_type: The redirect type the rule will use when redirecting
     traffic. Possible values include: 'Moved', 'Found', 'TemporaryRedirect',
     'PermanentRedirect'
    :type redirect_type: str or
     ~azure.mgmt.frontdoor.models.FrontDoorRedirectProtocol
    :param destination_protocol: The protocol of the destination where the
     traffic is forwarded to. Possible values include: 'MatchRequest', 'Http',
     'Https'
    :type destination_protocol: str or
     ~azure.mgmt.frontdoor.models.FrontDoorDestinationProtocol
    :param destination_host: If left blank, then we will use the incoming host
     as the destination host.
    :type destination_host: str
    :param destination_path: Path cannot be empty and must start with /.
    :type destination_path: str
    :param destination_fragment: Fragment is the part of the URL that comes
     after #. Do not include the #.
    :type destination_fragment: str
    :param preserve_path: Indicates whether the path is preserved. Possible
     values include: 'Yes', 'No'
    :type preserve_path: str or
     ~azure.mgmt.frontdoor.models.FrontDoorPreservePath
    :param preserve_query_string: Indicates whether the query string is
     preserved. Possible values include: 'Yes', 'No'
    :type preserve_query_string: str or
     ~azure.mgmt.frontdoor.models.FrontDoorPreserveQueryString
    :param extra_query_string: Any string to be added to the query string in
     the destination URL. ? and & will be added automatically so do not include
     them.
    :type extra_query_string: str
    """

    _attribute_map = {
        'redirect_type': {'key': 'redirectType', 'type': 'str'},
        'destination_protocol': {'key': 'destinationProtocol', 'type': 'str'},
        'destination_host': {'key': 'destinationHost', 'type': 'str'},
        'destination_path': {'key': 'destinationPath', 'type': 'str'},
        'destination_fragment': {'key': 'destinationFragment', 'type': 'str'},
        'preserve_path': {'key': 'preservePath', 'type': 'str'},
        'preserve_query_string': {'key': 'preserveQueryString', 'type': 'str'},
        'extra_query_string': {'key': 'extraQueryString', 'type': 'str'},
    }

    def __init__(self, *, redirect_type=None, destination_protocol=None, destination_host: str=None, destination_path: str=None, destination_fragment: str=None, preserve_path=None, preserve_query_string=None, extra_query_string: str=None, **kwargs) -> None:
        super(RedirectConfiguration, self).__init__(**kwargs)
        self.redirect_type = redirect_type
        self.destination_protocol = destination_protocol
        self.destination_host = destination_host
        self.destination_path = destination_path
        self.destination_fragment = destination_fragment
        self.preserve_path = preserve_path
        self.preserve_query_string = preserve_query_string
        self.extra_query_string = extra_query_string
