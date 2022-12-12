# fast_ip2as
Fast and accurate ip2as.

The ip2as mapping is accomplished by pyasn (https://github.com/hadiasghari/pyasn.git).

In this repository, we just provide a faster and more convenient way to obtain the mapping database. We use the routeviews Prefix-to-AS mappings (pfx2as) for IPv4 and IPv6 provided by CAIDA to generate the database. 

You can download the pfx2as files from https://publicdata.caida.org/datasets/routing/routeviews-prefix2as/

Steps:

1. install 
  pip install pyasn
2. Download pfx2as file from CAIDA
3. Generate the mapping db file
4 Usage
  import pyasn
  asndb = pyasn.pyasn('ipasn.dat')
  asndb.lookup('8.8.8.8')
  # should return: (15169, '8.8.8.0/24'), the origin AS, and the BGP prefix it matches
  asndb.get_as_prefixes(1128)
  # returns ['130.161.0.0/16', '131.180.0.0/16', '145.94.0.0/16'], TU-Delft prefixes
  
