# generate-sai-cases

```
git clone https://github.com/opencomputeproject/SAI.git



```


## phase 1:
run all tests - results 100% fail

## phase 2:
run all tests on by one

## phase 3:
run only the test cases that have no mandatory attributes

| TEST CASE                           | RESULT | COMMENT |
|-------------------------------------|---|---|
| test_ars.py                         |   |   |
| test_ars_profile.py                 |   |   |
| test_counter.py                     |   |   |
| test_dash_acl_group.py              |   |   |
| test_dash_acl_rule.py               |   |   |
| test_direction_lookup_entry.py      |   |   |
| test_dtel.py                        |   |   |
| test_dtel_int_session.py            |   |   |
| test_dtel_report_session.py         |   |   |
| test_eni.py                         |   |   |
| test_eni_ether_address_map_entry.py |   |   |
| test_extensions_range_end.py        |   |   |
| test_extensions_range_start.py      |   |   |
| test_fdb_flush.py                   |   |   |
| test_hash.py                        |   |   |
| test_hostif_trap_group.py           |   |   |
| test_host_interface.py              |   |   |
| test_inbound_routing_entry.py       |   |   |
| test_inseg_entry.py                 |   |   |
| test_ipmc_group.py                  |   |   |
| test_l.py                           |   |   |
| test_lag.py                         |   |   |
| test_max.py                         |   |   |
| test_my_mac.py                      |   |   |
| test_nat_entry.py                   |   |   |
| test_nat_zone_counter.py            |   |   |
| test_null.py                        |   |   |
| test_outbound_ca_to_pa_entry.py     |   |   |
| test_outbound_routing_entry.py      |   |   |
| test_pa_validation_entry.py         |   |   |
| test_route_entry.py                 |   |   |
| test_rpf_group.py                   |   |   |
| test_scheduler.py                   |   |   |
| test_srv.py                         |   |   |
| test_stp.py                         |   |   |
| test_table_bitmap_router_entry.py   |   |   |
| test_table_meta_tunnel_entry.py     |   |   |
| test_tam.py                         |   |   |
| test_tam_event_threshold.py         |   |   |
| test_tam_math_func.py               |   |   |
| test_udf_match.py                   |   |   |
| test_vip_entry.py                   |   |   |
| test_virtual_router.py              |   |   |
| test_vnet.py                        |   |   |
| test_wred.py                        |   |   |


## phase 4:
in cases that require mandatory attributes put proper values for those attributes
identify how to do int, list ,......

## phase 5:
run all cases that have mandatory attributes but do not have a parent (depedency on other object)

## phase 6:
create depedency graph between SAI objects

## phase 7:
run all cases that have depedency on other attributes but those depdencies are on objects from other cases that already passed in phase 1-6
