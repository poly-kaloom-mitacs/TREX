from trex_stl_lib.api import *
from scapy.contrib.gtp import GTP_U_Header, GTPPDUSessionContainer

class STLS1(object):

	def create_stream (self):
		return STLStream(
			packet = 
				STLPktBuilder(
					pkt = Ether() / IP(src = "10.0.0.10", dst = "10.0.0.1") / UDP(sport=2152, dport=2152) / GTP_U_Header(gtp_type=255, E=1, next_ex=0x85, teid=12) /
						GTPPDUSessionContainer(type=0, QFI=10, NextExtHdr=0) / IP() / (10*'x')
				),

	mode = STLTXCont())

	def get_streams (self, direction = 0,  **kwargs) :
		# create 1 stream
		return [ self.create_stream() ]

def register():
    return STLS1()
