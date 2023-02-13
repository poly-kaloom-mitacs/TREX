# SETUP GUIDE :


## 1. Install Cisco TRex

1/ Create Trex directory 

```bash
mkdir -p /opt/trex
```

2/ Move to Trex directory 

```bash
cd /opt/trex/v2.XX/
```
3/ Download the lqst version of Trex

```bash
wget --no-cache --no-check-certificate https://trex-tgn.cisco.com/trex/release/latest
```
4/ Untar the tar file

```bash
tar -xzvf latest
```
## 2. Setup NIC ports DPDK drivers

1/ Move to Trex directory 

```bash
cd /opt/trex/v2.XX/
```
2/ Identify the ports:

```bash
./dpdk_setup_ports.py -s
```
3/ Insert the kernel driver and bind NIC ports
```bash
modprobe uio
insmod ko/src/igb_uio.ko
./dpdk_nic_bind.py -b igb_uio #add 2 port Ids
```
## 3. Create a configuration file for TRex

in etc/trex_cfg.yaml:

```bash
- version: 2
  port_limit: 2
  # use ./dpdk_nic_bind.py -s to know the NIC intefraces Ids
  interfaces: ['01:00.0', '01:00.1']
  port_info:
    # MAC for NIC
    - src_mac: '<Interface1 MAC >'
      dest_mac: '<DST MAC 1>'
    - src_mac: '<Interface2 MAC>'
      dest_mac: '<DST MAC 2>'
```

## 4. Running tests
1/ Run TRex server :
```bash
sudo ./t-rex-64 -i
```
2/ Run TRex console
```bash
# in other terminal
./trex-console
```
3/ Start the traffic on port 0 at 8gbs
```
# for 1 flow 
trex> start -f stl/AGF_stream/gtpu_1flow_simple.py -m 8gbps -p 0

#for multiple flows
trex> start -f stl/AGF_stream/gtpu_multiple_streams.py -m 8gbps -p 0 
```
