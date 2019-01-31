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


class ReservationRecommendationPropertiesWithAmount(Model):
    """The properties of the reservation recommendation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar look_back_period: The number of days of usage to look back for
     recommendation.
    :vartype look_back_period: str
    :ivar meter_id: The meter id (GUID)
    :vartype meter_id: str
    :ivar sku_name: Sku name of the reserved instance resource.
    :vartype sku_name: str
    :ivar region: Region of the reserved instance resource.
    :vartype region: str
    :ivar term: RI recommendations in one or three year terms.
    :vartype term: str
    :ivar cost_with_no_ri: The total amount of cost without reserved
     instances.
    :vartype cost_with_no_ri: decimal.Decimal
    :ivar recommended_quantity: Recommended quality for reserved instances.
    :vartype recommended_quantity: decimal.Decimal
    :ivar total_cost_with_ri: The total amount of cost with reserved
     instances.
    :vartype total_cost_with_ri: decimal.Decimal
    :ivar net_savings: Total estimated savings with reserved instances.
    :vartype net_savings: decimal.Decimal
    :ivar first_usage_date: The usage date for looking back.
    :vartype first_usage_date: datetime
    """

    _validation = {
        'look_back_period': {'readonly': True},
        'meter_id': {'readonly': True},
        'sku_name': {'readonly': True},
        'region': {'readonly': True},
        'term': {'readonly': True},
        'cost_with_no_ri': {'readonly': True},
        'recommended_quantity': {'readonly': True},
        'total_cost_with_ri': {'readonly': True},
        'net_savings': {'readonly': True},
        'first_usage_date': {'readonly': True},
    }

    _attribute_map = {
        'look_back_period': {'key': 'lookBackPeriod', 'type': 'str'},
        'meter_id': {'key': 'meterId', 'type': 'str'},
        'sku_name': {'key': 'skuName', 'type': 'str'},
        'region': {'key': 'region', 'type': 'str'},
        'term': {'key': 'term', 'type': 'str'},
        'cost_with_no_ri': {'key': 'costWithNoRI', 'type': 'decimal'},
        'recommended_quantity': {'key': 'recommendedQuantity', 'type': 'decimal'},
        'total_cost_with_ri': {'key': 'totalCostWithRI', 'type': 'decimal'},
        'net_savings': {'key': 'netSavings', 'type': 'decimal'},
        'first_usage_date': {'key': 'firstUsageDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(ReservationRecommendationPropertiesWithAmount, self).__init__(**kwargs)
        self.look_back_period = None
        self.meter_id = None
        self.sku_name = None
        self.region = None
        self.term = None
        self.cost_with_no_ri = None
        self.recommended_quantity = None
        self.total_cost_with_ri = None
        self.net_savings = None
        self.first_usage_date = None