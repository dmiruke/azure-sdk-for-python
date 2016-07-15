# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Routing rules for TiP
    #
    class RoutingRule

      include MsRestAzure

      # @return [String] Name of the routing rule. The recommended name would
      # be to point to the slot which will receive the traffic in the
      # experiment.
      attr_accessor :name


      #
      # Mapper for RoutingRule class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'RoutingRule',
          type: {
            name: 'Composite',
            class_name: 'RoutingRule',
            model_properties: {
              name: {
                required: false,
                serialized_name: 'name',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end