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

from .sub_resource import SubResource


class RoutingRule(SubResource):
    """A routing rule represents a specification for traffic to treat and where to
    send it, along with health probe information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param route_type: The type of a routing rule. It must be set to Redirect
     for a redirect routing rule. To be backwards-compatible, it is not needed
     for a forwarding routing rule. Possible values include: 'Forwarding',
     'Redirect'
    :type route_type: str or ~azure.mgmt.frontdoor.models.FrontDoorRouteType
    :param frontend_endpoints: Frontend endpoints associated with this rule
    :type frontend_endpoints: list[~azure.mgmt.frontdoor.models.SubResource]
    :param accepted_protocols: Protocol schemes to match for this rule
    :type accepted_protocols: list[str or
     ~azure.mgmt.frontdoor.models.FrontDoorProtocol]
    :param patterns_to_match: The route patterns of the rule.
    :type patterns_to_match: list[str]
    :param custom_forwarding_path: A custom path used to rewrite resource
     paths matched by this rule. Leave empty to use incoming path.
    :type custom_forwarding_path: str
    :param forwarding_protocol: Protocol this rule will use when forwarding
     traffic to backends. Possible values include: 'HttpOnly', 'HttpsOnly',
     'MatchRequest'
    :type forwarding_protocol: str or
     ~azure.mgmt.frontdoor.models.FrontDoorForwardingProtocol
    :param cache_configuration: The caching configuration associated with this
     rule.
    :type cache_configuration: ~azure.mgmt.frontdoor.models.CacheConfiguration
    :param backend_pool: A reference to the BackendPool which this rule routes
     to.
    :type backend_pool: ~azure.mgmt.frontdoor.models.SubResource
    :param enabled_state: Whether to enable use of this rule. Permitted values
     are 'Enabled' or 'Disabled'. Possible values include: 'Enabled',
     'Disabled'
    :type enabled_state: str or
     ~azure.mgmt.frontdoor.models.FrontDoorEnabledState
    :param redirect_configuration: A reference to the redirect routing
     configuration. It is null for a forward-routing rule. But it must not be
     null if the routeType property is set to Redirect.
    :type redirect_configuration:
     ~azure.mgmt.frontdoor.models.RedirectConfiguration
    :param resource_state: Resource status. Possible values include:
     'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled', 'Deleting'
    :type resource_state: str or
     ~azure.mgmt.frontdoor.models.FrontDoorResourceState
    :param name: Resource name.
    :type name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'route_type': {'key': 'properties.routeType', 'type': 'str'},
        'frontend_endpoints': {'key': 'properties.frontendEndpoints', 'type': '[SubResource]'},
        'accepted_protocols': {'key': 'properties.acceptedProtocols', 'type': '[str]'},
        'patterns_to_match': {'key': 'properties.patternsToMatch', 'type': '[str]'},
        'custom_forwarding_path': {'key': 'properties.customForwardingPath', 'type': 'str'},
        'forwarding_protocol': {'key': 'properties.forwardingProtocol', 'type': 'str'},
        'cache_configuration': {'key': 'properties.cacheConfiguration', 'type': 'CacheConfiguration'},
        'backend_pool': {'key': 'properties.backendPool', 'type': 'SubResource'},
        'enabled_state': {'key': 'properties.enabledState', 'type': 'str'},
        'redirect_configuration': {'key': 'properties.redirectConfiguration', 'type': 'RedirectConfiguration'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RoutingRule, self).__init__(**kwargs)
        self.route_type = kwargs.get('route_type', None)
        self.frontend_endpoints = kwargs.get('frontend_endpoints', None)
        self.accepted_protocols = kwargs.get('accepted_protocols', None)
        self.patterns_to_match = kwargs.get('patterns_to_match', None)
        self.custom_forwarding_path = kwargs.get('custom_forwarding_path', None)
        self.forwarding_protocol = kwargs.get('forwarding_protocol', None)
        self.cache_configuration = kwargs.get('cache_configuration', None)
        self.backend_pool = kwargs.get('backend_pool', None)
        self.enabled_state = kwargs.get('enabled_state', None)
        self.redirect_configuration = kwargs.get('redirect_configuration', None)
        self.resource_state = kwargs.get('resource_state', None)
        self.name = kwargs.get('name', None)
        self.type = None
