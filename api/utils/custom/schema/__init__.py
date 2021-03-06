from api.utils.custom.schema.aggregation import AggregationSchema
from api.utils.custom.schema.mould import (MouldSchema, MouldBaseSchema, MouldNodeSchema)
from api.utils.custom.schema.user import UserSchema
from api.utils.custom.schema.base import BaseQuerySchema
from api.utils.custom.schema.instance import (InstanceSchema, InstanceNodeSchema, InstanceDetailSchema)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
aggregation_schema = AggregationSchema()
aggregations_schema = AggregationSchema(many=True)
mould_schema = MouldSchema()
moulds_schema = MouldSchema(many=True)
mould_base_schema = MouldBaseSchema()
moulds_base_schema = MouldBaseSchema(many=True)
instance_schema = InstanceSchema()
instances_schema = InstanceSchema(many=True)
base_query_schema = BaseQuerySchema()
mould_node_schema = MouldNodeSchema()
mould_nodes_schema = MouldNodeSchema(many=True)
instance_node_schema = InstanceNodeSchema()
instance_nodes_schema = InstanceNodeSchema(many=True)
instance_detail_schema = InstanceDetailSchema()
instances_detail_schema = InstanceDetailSchema(many=True)


__all__ = [
    'user_schema', 'users_schema', 'aggregation_schema', 'aggregations_schema', 'mould_schema', 'moulds_schema',
    'base_query_schema', 'mould_base_schema', 'moulds_base_schema', 'mould_node_schema', 'mould_nodes_schema',
    'instance_node_schema', 'instance_nodes_schema', 'instance_detail_schema', 'instances_detail_schema',
]
