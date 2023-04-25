import io
import pprint
from re import sub

TEST_TEMPLATE = '''

from pprint import pprint

import pytest


class TestSai%(CLASS_NAME)s:

    @pytest.mark.dependency(scope='session')
    def test_%(OBJECT_NAME)s_create(self, npu):

        commands = %(CREATE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_%(OBJECT_NAME)s_remove(self, npu):

        commands = %(REMOVE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

'''


def get_object_types():
    return ['SAI_OBJECT_TYPE___', 'SAI_OBJECT_TYPE_ACL_COUNTER', 'SAI_OBJECT_TYPE_ACL_ENTRY', 'SAI_OBJECT_TYPE_ACL_RANGE', 'SAI_OBJECT_TYPE_ACL_TABLE', 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP', 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP_MEMBER', 'SAI_OBJECT_TYPE_ARS', 'SAI_OBJECT_TYPE_ARS_PROFILE', 'SAI_OBJECT_TYPE_BFD_SESSION', 'SAI_OBJECT_TYPE_BRIDGE', 'SAI_OBJECT_TYPE_BRIDGE_PORT', 'SAI_OBJECT_TYPE_BUFFER_POOL', 'SAI_OBJECT_TYPE_BUFFER_PROFILE', 'SAI_OBJECT_TYPE_COUNTER', 'SAI_OBJECT_TYPE_DASH_ACL_GROUP', 'SAI_OBJECT_TYPE_DASH_ACL_RULE', 'SAI_OBJECT_TYPE_DEBUG_COUNTER', 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY', 'SAI_OBJECT_TYPE_DTEL', 'SAI_OBJECT_TYPE_DTEL_EVENT', 'SAI_OBJECT_TYPE_DTEL_INT_SESSION', 'SAI_OBJECT_TYPE_DTEL_QUEUE_REPORT', 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION', 'SAI_OBJECT_TYPE_ENI', 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY', 'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_END', 'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_START', 'SAI_OBJECT_TYPE_FDB_ENTRY', 'SAI_OBJECT_TYPE_FDB_FLUSH', 'SAI_OBJECT_TYPE_FINE_GRAINED_HASH_FIELD', 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE', 'SAI_OBJECT_TYPE_HASH', 'SAI_OBJECT_TYPE_HOST_INTERFACE', 'SAI_OBJECT_TYPE_HOSTIF', 'SAI_OBJECT_TYPE_HOSTIF_PACKET', 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY', 'SAI_OBJECT_TYPE_HOSTIF_TRAP', 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP', 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP', 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY', 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP', 'SAI_OBJECT_TYPE_INSEG_ENTRY', 'SAI_OBJECT_TYPE_IPMC_ENTRY', 'SAI_OBJECT_TYPE_IPMC_GROUP', 'SAI_OBJECT_TYPE_IPMC_GROUP_MEMBER', 'SAI_OBJECT_TYPE_IPSEC', 'SAI_OBJECT_TYPE_IPSEC_PORT', 'SAI_OBJECT_TYPE_IPSEC_SA', 'SAI_OBJECT_TYPE_ISOLATION_GROUP', 'SAI_OBJECT_TYPE_ISOLATION_GROUP_MEMBER', 'SAI_OBJECT_TYPE_L', 'SAI_OBJECT_TYPE_LAG', 'SAI_OBJECT_TYPE_LAG_MEMBER', 'SAI_OBJECT_TYPE_MACSEC', 'SAI_OBJECT_TYPE_MACSEC_FLOW', 'SAI_OBJECT_TYPE_MACSEC_PORT', 'SAI_OBJECT_TYPE_MACSEC_SA', 'SAI_OBJECT_TYPE_MACSEC_SC', 'SAI_OBJECT_TYPE_MAX', 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY', 'SAI_OBJECT_TYPE_MIRROR_SESSION', 'SAI_OBJECT_TYPE_MY_MAC', 'SAI_OBJECT_TYPE_MY_SID_ENTRY', 'SAI_OBJECT_TYPE_NAT_ENTRY', 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER', 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY', 'SAI_OBJECT_TYPE_NEXT_HOP', 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP', 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP', 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MEMBER', 'SAI_OBJECT_TYPE_NULL', 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY', 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY', 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY', 'SAI_OBJECT_TYPE_POLICER', 'SAI_OBJECT_TYPE_PORT', 'SAI_OBJECT_TYPE_PORT_CONNECTOR', 'SAI_OBJECT_TYPE_PORT_POOL', 'SAI_OBJECT_TYPE_PORT_SERDES', 'SAI_OBJECT_TYPE_QOS_MAP', 'SAI_OBJECT_TYPE_QUEUE', 'SAI_OBJECT_TYPE_ROUTE_ENTRY', 'SAI_OBJECT_TYPE_ROUTER_INTERFACE', 'SAI_OBJECT_TYPE_RPF_GROUP', 'SAI_OBJECT_TYPE_RPF_GROUP_MEMBER', 'SAI_OBJECT_TYPE_SAMPLEPACKET', 'SAI_OBJECT_TYPE_SCHEDULER', 'SAI_OBJECT_TYPE_SCHEDULER_GROUP', 'SAI_OBJECT_TYPE_SRV', 'SAI_OBJECT_TYPE_STP', 'SAI_OBJECT_TYPE_STP_PORT', 'SAI_OBJECT_TYPE_SWITCH', 'SAI_OBJECT_TYPE_SWITCH_TUNNEL', 'SAI_OBJECT_TYPE_SYSTEM_PORT', 'SAI_OBJECT_TYPE_TABLE_BITMAP_ROUTER_ENTRY', 'SAI_OBJECT_TYPE_TABLE_META_TUNNEL_ENTRY', 'SAI_OBJECT_TYPE_TAM', 'SAI_OBJECT_TYPE_TAM_COLLECTOR', 'SAI_OBJECT_TYPE_TAM_EVENT', 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION', 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD', 'SAI_OBJECT_TYPE_TAM_INT', 'SAI_OBJECT_TYPE_TAM_MATH_FUNC', 'SAI_OBJECT_TYPE_TAM_REPORT', 'SAI_OBJECT_TYPE_TAM_TEL_TYPE', 'SAI_OBJECT_TYPE_TAM_TELEMETRY', 'SAI_OBJECT_TYPE_TAM_TRANSPORT', 'SAI_OBJECT_TYPE_TUNNEL', 'SAI_OBJECT_TYPE_TUNNEL_MAP', 'SAI_OBJECT_TYPE_TUNNEL_MAP_ENTRY', 'SAI_OBJECT_TYPE_TUNNEL_TERM_TABLE_ENTRY', 'SAI_OBJECT_TYPE_UDF', 'SAI_OBJECT_TYPE_UDF_GROUP', 'SAI_OBJECT_TYPE_UDF_MATCH', 'SAI_OBJECT_TYPE_VIP_ENTRY', 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER', 'SAI_OBJECT_TYPE_VLAN', 'SAI_OBJECT_TYPE_VLAN_MEMBER', 'SAI_OBJECT_TYPE_VNET', 'SAI_OBJECT_TYPE_WRED', 'SAI_OBJECT_TYPE_XXX']


def get_mandatory_attributes(obj_type):
    return ['a', 'b']


def get_obj_name(obj_type):
    return obj_type.replace('SAI_OBJECT_TYPE_', '').lower()


def get_create_command(obj_type):
    obj_name = get_obj_name(obj_type)

    command = {
        'name': obj_name + '_1',
        'op': 'create',
        'type': obj_type
    }

    attributes = []
    for attribute in get_mandatory_attributes(obj_type):
        attributes.append(attribute)
        attributes.append('TODO')
    command["attributes"] = attributes

    return command


def get_remove_command(obj_type):
    command = get_create_command(obj_type)
    command['op'] = 'remove'
    return command


def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return s


def generate_pyetes_test(obj_type):
    obj_name = get_obj_name(obj_type)
    test_file_name = 'test_%s.py' % obj_name
    print(test_file_name)

    with io.open(test_file_name, 'wt', encoding='ascii') as test_file:
        test_file.write(
            TEST_TEMPLATE % {
                'CLASS_NAME': camel_case(obj_name),
                'OBJECT_NAME': obj_name,
                'CREATE_COMMANDS': [get_create_command(obj_type)],
                'REMOVE_COMMANDS': [get_remove_command(obj_type)],
            }
        )


object_dict = {}

object_types = get_object_types()

for obj_type in object_types:
    mandatory_attributes = get_mandatory_attributes(obj_type)
    attr_dict = {}
    for mandatory_attribute in mandatory_attributes:
        attr_dict[mandatory_attribute] = 'TODO'
    object_dict[obj_type] = attr_dict

    generate_pyetes_test(obj_type)


pprint.pprint(object_dict)
