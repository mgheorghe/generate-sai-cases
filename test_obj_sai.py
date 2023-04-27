import io
import pprint
from re import sub

import networkx as nx
from pyvis.network import Network

SAI_CODE_LOCATION = r'/home/ubuntuserver/dinesh/SAI/'
SAI_CODE_LOCATION = r'C:/github-keysight/SAI'

TEST_TEMPLATE = '''
from pprint import pprint

import pytest


class TestSai%(CLASS_NAME)s:
    # %(COMMENT)s

    @pytest.mark.dependency(scope='session')
    def test_%(OBJECT_NAME)s_create(self, npu):

        commands = %(CREATE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_%(OBJECT_NAME)s_remove(self, npu):

        commands = %(REMOVE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'

'''


def get_object_types():
    return [
        'SAI_OBJECT_TYPE___',
        'SAI_OBJECT_TYPE_ACL_COUNTER',
        'SAI_OBJECT_TYPE_ACL_ENTRY',
        'SAI_OBJECT_TYPE_ACL_RANGE',
        'SAI_OBJECT_TYPE_ACL_TABLE',
        'SAI_OBJECT_TYPE_ACL_TABLE_GROUP',
        'SAI_OBJECT_TYPE_ACL_TABLE_GROUP_MEMBER',
        'SAI_OBJECT_TYPE_ARS',
        'SAI_OBJECT_TYPE_ARS_PROFILE',
        'SAI_OBJECT_TYPE_BFD_SESSION',
        'SAI_OBJECT_TYPE_BRIDGE',
        'SAI_OBJECT_TYPE_BRIDGE_PORT',
        'SAI_OBJECT_TYPE_BUFFER_POOL',
        'SAI_OBJECT_TYPE_BUFFER_PROFILE',
        'SAI_OBJECT_TYPE_COUNTER',
        'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
        'SAI_OBJECT_TYPE_DASH_ACL_RULE',
        'SAI_OBJECT_TYPE_DEBUG_COUNTER',
        'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY',
        'SAI_OBJECT_TYPE_DTEL',
        'SAI_OBJECT_TYPE_DTEL_EVENT',
        'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
        'SAI_OBJECT_TYPE_DTEL_QUEUE_REPORT',
        'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
        'SAI_OBJECT_TYPE_ENI',
        'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
        'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_END',
        'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_START',
        'SAI_OBJECT_TYPE_FDB_ENTRY',
        'SAI_OBJECT_TYPE_FDB_FLUSH',
        'SAI_OBJECT_TYPE_FINE_GRAINED_HASH_FIELD',
        'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
        'SAI_OBJECT_TYPE_HASH',
        'SAI_OBJECT_TYPE_HOST_INTERFACE',
        'SAI_OBJECT_TYPE_HOSTIF',
        'SAI_OBJECT_TYPE_HOSTIF_PACKET',
        'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY',
        'SAI_OBJECT_TYPE_HOSTIF_TRAP',
        'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
        'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
        'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
        'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
        'SAI_OBJECT_TYPE_INSEG_ENTRY',
        'SAI_OBJECT_TYPE_IPMC_ENTRY',
        'SAI_OBJECT_TYPE_IPMC_GROUP',
        'SAI_OBJECT_TYPE_IPMC_GROUP_MEMBER',
        'SAI_OBJECT_TYPE_IPSEC',
        'SAI_OBJECT_TYPE_IPSEC_PORT',
        'SAI_OBJECT_TYPE_IPSEC_SA',
        'SAI_OBJECT_TYPE_ISOLATION_GROUP',
        'SAI_OBJECT_TYPE_ISOLATION_GROUP_MEMBER',
        'SAI_OBJECT_TYPE_L',
        'SAI_OBJECT_TYPE_LAG',
        'SAI_OBJECT_TYPE_LAG_MEMBER',
        'SAI_OBJECT_TYPE_MACSEC',
        'SAI_OBJECT_TYPE_MACSEC_FLOW',
        'SAI_OBJECT_TYPE_MACSEC_PORT',
        'SAI_OBJECT_TYPE_MACSEC_SA',
        'SAI_OBJECT_TYPE_MACSEC_SC',
        'SAI_OBJECT_TYPE_MAX',
        'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
        'SAI_OBJECT_TYPE_MIRROR_SESSION',
        'SAI_OBJECT_TYPE_MY_MAC',
        'SAI_OBJECT_TYPE_MY_SID_ENTRY',
        'SAI_OBJECT_TYPE_NAT_ENTRY',
        'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
        'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
        'SAI_OBJECT_TYPE_NEXT_HOP',
        'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
        'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP',
        'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MEMBER',
        'SAI_OBJECT_TYPE_NULL',
        'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
        'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
        'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
        'SAI_OBJECT_TYPE_POLICER',
        'SAI_OBJECT_TYPE_PORT',
        'SAI_OBJECT_TYPE_PORT_CONNECTOR',
        'SAI_OBJECT_TYPE_PORT_POOL',
        'SAI_OBJECT_TYPE_PORT_SERDES',
        'SAI_OBJECT_TYPE_QOS_MAP',
        'SAI_OBJECT_TYPE_QUEUE',
        'SAI_OBJECT_TYPE_ROUTE_ENTRY',
        'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
        'SAI_OBJECT_TYPE_RPF_GROUP',
        'SAI_OBJECT_TYPE_RPF_GROUP_MEMBER',
        'SAI_OBJECT_TYPE_SAMPLEPACKET',
        'SAI_OBJECT_TYPE_SCHEDULER',
        'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
        'SAI_OBJECT_TYPE_SRV',
        'SAI_OBJECT_TYPE_STP',
        'SAI_OBJECT_TYPE_STP_PORT',
        'SAI_OBJECT_TYPE_SWITCH',
        'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
        'SAI_OBJECT_TYPE_SYSTEM_PORT',
        'SAI_OBJECT_TYPE_TABLE_BITMAP_ROUTER_ENTRY',
        'SAI_OBJECT_TYPE_TABLE_META_TUNNEL_ENTRY',
        'SAI_OBJECT_TYPE_TAM',
        'SAI_OBJECT_TYPE_TAM_COLLECTOR',
        'SAI_OBJECT_TYPE_TAM_EVENT',
        'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
        'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
        'SAI_OBJECT_TYPE_TAM_INT',
        'SAI_OBJECT_TYPE_TAM_MATH_FUNC',
        'SAI_OBJECT_TYPE_TAM_REPORT',
        'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
        'SAI_OBJECT_TYPE_TAM_TELEMETRY',
        'SAI_OBJECT_TYPE_TAM_TRANSPORT',
        'SAI_OBJECT_TYPE_TUNNEL',
        'SAI_OBJECT_TYPE_TUNNEL_MAP',
        'SAI_OBJECT_TYPE_TUNNEL_MAP_ENTRY',
        'SAI_OBJECT_TYPE_TUNNEL_TERM_TABLE_ENTRY',
        'SAI_OBJECT_TYPE_UDF',
        'SAI_OBJECT_TYPE_UDF_GROUP',
        'SAI_OBJECT_TYPE_UDF_MATCH',
        'SAI_OBJECT_TYPE_VIP_ENTRY',
        'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
        'SAI_OBJECT_TYPE_VLAN',
        'SAI_OBJECT_TYPE_VLAN_MEMBER',
        'SAI_OBJECT_TYPE_VNET',
        'SAI_OBJECT_TYPE_WRED',
        'SAI_OBJECT_TYPE_XXX',
    ]


def get_all_attributes(obj_type):
    obj_name = get_obj_name(obj_type)
    block_start = 'typedef enum _sai_%s_attr_t' % obj_name
    block_end = '} sai_%s_attr_t;' % obj_name

    dictionary = {}

    import os

    for root, dirs, files in os.walk(SAI_CODE_LOCATION):
        for file in files:
            if file.endswith('.h'):
                start_copy = False
                is_attribute = False
                attr_block_start = False
                with io.open(
                    os.path.join(root, file), 'rt', encoding='utf-8'
                ) as h_file:
                    for text_line in h_file:
                        if block_start in text_line:
                            print(os.path.join(root, file))
                            start_copy = True
                        if block_end in text_line:
                            start_copy = False
                        if start_copy:
                            if attr_block_start:
                                if '@type' in text_line:
                                    o_type = text_line.replace('* @type', '').strip()
                                if '@flags' in text_line:
                                    flags = text_line.replace('* @flags', '').strip()
                                if '@objects' in text_line:
                                    objects = []
                                    for parent in (
                                        text_line.replace('* @objects', '')
                                        .strip()
                                        .split(',')
                                    ):
                                        objects.append(parent.strip())
                                        if flags:
                                            if 'MANDATORY_ON_CREATE' in flags:
                                                G.add_edge(
                                                    obj_type.replace(
                                                        'SAI_OBJECT_TYPE_', ''
                                                    ),
                                                    parent.strip().replace(
                                                        'SAI_OBJECT_TYPE_', ''
                                                    ),
                                                )
                                if '@allownull' in text_line:
                                    allownull = text_line.replace(
                                        '* @allownull', ''
                                    ).strip()
                                if '@default' in text_line:
                                    default = text_line.replace(
                                        '* @default', ''
                                    ).strip()

                            if is_attribute:
                                attribute = (
                                    text_line.split('=')[0].replace(',', '').strip()
                                )
                                if attribute != '':
                                    dictionary[attribute] = {}
                                    dictionary[attribute]['type'] = o_type
                                    dictionary[attribute]['flags'] = flags
                                    dictionary[attribute]['objects'] = objects
                                    dictionary[attribute]['allownull'] = allownull
                                    dictionary[attribute]['default'] = default
                                    # print(attribute)
                                    # print(dictionary[attribute])
                                o_type = None
                                flags = None
                                objects = None
                                allownull = None
                                default = None
                                is_attribute = False

                            if '/**' in text_line:
                                attr_block_start = True
                                o_type = None
                                flags = None
                                objects = None
                                allownull = None
                                default = None
                            if '*/' in text_line:
                                attr_block_start = False
                                is_attribute = True

    # pprint.pprint(dictionary)
    return dictionary


def select_mandatory_attributes(all_attributes):
    mandatory = {}
    for attribute in all_attributes.keys():
        if all_attributes[attribute]['flags'] is not None:
            if 'MANDATORY_ON_CREATE' in all_attributes[attribute]['flags']:
                mandatory[attribute] = all_attributes[attribute]

    pprint.pprint(mandatory)
    return mandatory


def get_obj_name(obj_type):
    return obj_type.replace('SAI_OBJECT_TYPE_', '').lower()


def get_create_command(obj_type):
    obj_name = get_obj_name(obj_type)

    command = {'name': obj_name + '_1', 'op': 'create', 'type': obj_type}

    attributes = []
    mandatory_attributes = select_mandatory_attributes(get_all_attributes(obj_type))
    for attribute in mandatory_attributes.keys():
        attributes.append(attribute)
        if 'type' in mandatory_attributes[attribute].keys():
            if 'sai_uint16_t' == mandatory_attributes[attribute]['type']:
                attributes.append('10')
            elif 'sai_uint32_t' == mandatory_attributes[attribute]['type']:
                attributes.append('10')
            elif 'sai_uint64_t' == mandatory_attributes[attribute]['type']:
                attributes.append('10')
            elif (
                'sai_bridge_type_t' == mandatory_attributes[attribute]['type']
            ):  # Fail: SAI_STATUS_NOT_IMPLEMENTED
                attributes.append('SAI_BRIDGE_TYPE_1Q')
            elif 'sai_meter_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_METER_TYPE_PACKETS')
            elif 'sai_policer_mode_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_POLICER_MODE_SR_TCM')
            elif (
                'sai_tam_transport_type_t' == mandatory_attributes[attribute]['type']
            ):  # Fail# SAI_STATUS_NOT_SUPPORTED
                attributes.append('SAI_TAM_TRANSPORT_TYPE_TCP')
            elif (
                'sai_s8_list_t' == mandatory_attributes[attribute]['type']
            ):  # Error: not sure of the values
                attributes.append('2:10,11')
            elif 'sai_debug_counter_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_DEBUG_COUNTER_TYPE_PORT_IN_DROP_REASONS')
            elif (
                'sai_dtel_event_type_t' == mandatory_attributes[attribute]['type']
            ):  # Fail: SAI_STATUS_NOT_SUPPORTED
                attributes.append('SAI_DTEL_EVENT_TYPE_FLOW_STATE')
            elif 'sai_qos_map_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_QOS_MAP_TYPE_DOT1P_TO_TC')
            elif (
                'sai_qos_map_list_t' == mandatory_attributes[attribute]['type']
            ):  # Error: not sure of the values
                attributes.append('2:10,11')
            elif (
                'sai_u32_list_t' == mandatory_attributes[attribute]['type']
            ):  # Error: not sure of the values
                attributes.append('2:10,11')
            elif 'sai_acl_stage_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_ACL_STAGE_INGRESS')
            elif (
                'bool' == mandatory_attributes[attribute]['type']
            ):  # Error: fails for true and false
                attributes.append('true')
            elif 'sai_next_hop_group_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_NEXT_HOP_GROUP_TYPE_DYNAMIC_UNORDERED_ECMP')
            elif 'sai_buffer_pool_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_BUFFER_POOL_TYPE_INGRESS')
            elif (
                'sai_macsec_direction_t' == mandatory_attributes[attribute]['type']
            ):  # Fail: SAI_STATUS_NOT_IMPLEMENTED
                attributes.append('SAI_MACSEC_DIRECTION_EGRESS')
            elif 'sai_mac_t' == mandatory_attributes[attribute]['type']:
                attributes.append('00:00:00:00:00:00')
            elif (
                'sai_my_sid_entry_endpoint_behavior_t'
                == mandatory_attributes[attribute]['type']
            ):  # fails due to unknown reason
                attributes.append('SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_E')
            elif (
                'sai_next_hop_group_map_type_t'
                == mandatory_attributes[attribute]['type']
            ):  # fails due to unknown reason
                attributes.append(
                    'SAI_NEXT_HOP_GROUP_MAP_TYPE_FORWARDING_CLASS_TO_INDEX'
                )
            elif (
                'sai_hostif_user_defined_trap_type_t'
                == mandatory_attributes[attribute]['type']
            ):
                attributes.append('SAI_HOSTIF_USER_DEFINED_TRAP_TYPE_END')
            elif 'sai_tunnel_map_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN')
            elif (
                'sai_tunnel_type_t' == mandatory_attributes[attribute]['type']
            ):  # Fail: SAI_STATUS_NOT_IMPLEMENTED
                attributes.append('SAI_TUNNEL_TYPE_IPINIP')
            elif 'sai_acl_stage_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_ACL_STAGE_INGRESS')
            elif (
                'sai_fdb_entry_type_t' == mandatory_attributes[attribute]['type']
            ):  # fails due to unknown reason
                attributes.append('SAI_FDB_ENTRY_TYPE_DYNAMIC')
            elif 'sai_acl_range_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_ACL_RANGE_TYPE_L4_SRC_PORT_RANGE')
            elif 'sai_u32_range_t' == mandatory_attributes[attribute]['type']:
                attributes.append('10,20')
            elif (
                'sai_isolation_group_type_t' == mandatory_attributes[attribute]['type']
            ):
                attributes.append('SAI_ISOLATION_GROUP_TYPE_PORT')
            elif 'sai_macsec_direction_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_MACSEC_DIRECTION_EGRESS')
            elif (
                'sai_hostif_trap_type_t' == mandatory_attributes[attribute]['type']
            ):  # fails due to unknown reason
                attributes.append('SAI_HOSTIF_TRAP_TYPE_START')
            elif (
                'sai_packet_action_t' == mandatory_attributes[attribute]['type']
            ):  # fails due to unknown reason
                attributes.append('SAI_PACKET_ACTION_DROP')
            elif 'sai_tam_report_type_t' == mandatory_attributes[attribute]['type']:
                attributes.append('SAI_TAM_REPORT_TYPE_SFLOW')
            elif (
                'sai_switch_hardware_access_bus_t'
                == mandatory_attributes[attribute]['type']
            ):
                attributes.append('SAI_SWITCH_HARDWARE_ACCESS_BUS_MDIO')
            else:
                attributes.append(mandatory_attributes[attribute]['type'])
        else:
            attributes.append('TODO')
    command['attributes'] = attributes

    return command


def get_remove_command(obj_type):
    command = get_create_command(obj_type)
    command['op'] = 'remove'
    return command


def camel_case(s):
    s = sub(r'(_|-)+', ' ', s).title().replace(' ', '')
    return s


def generate_comment(obj_type):
    mandatory_attributes = select_mandatory_attributes(get_all_attributes(obj_type))
    if len(mandatory_attributes) == 0:
        return 'object with no attributes'
    else:
        parents = []
        for attribute in mandatory_attributes.keys():
            if 'objects' in mandatory_attributes[attribute].keys():
                if mandatory_attributes[attribute]['objects'] is not None:
                    parents.extend(mandatory_attributes[attribute]['objects'])
        if len(parents) == 0:
            return 'object with no parents'
        else:
            return 'object with parent %s' % (' '.join(parents))


def generate_pyetes_test(obj_type):
    obj_name = get_obj_name(obj_type)
    test_file_name = 'test_%s.py' % obj_name
    # print(test_file_name)

    with io.open(test_file_name, 'wt', encoding='ascii') as test_file:
        test_file.write(
            TEST_TEMPLATE
            % {
                'CLASS_NAME': camel_case(obj_name),
                'OBJECT_NAME': obj_name,
                'CREATE_COMMANDS': [get_create_command(obj_type)],
                'REMOVE_COMMANDS': [get_remove_command(obj_type)],
                'COMMENT': generate_comment(obj_type),
            }
        )


object_dict = {}
object_types = get_object_types()

G = nx.DiGraph()
nt = Network('1300px', '2500px', notebook=True)

for obj_type in object_types:
    G.add_node(obj_type.replace('SAI_OBJECT_TYPE_', ''))
    generate_pyetes_test(obj_type)

nt.from_nx(G)
nt.show('nx.html')
