from trex_stl_lib.api import *
from scapy.contrib.gtp import GTP_U_Header, GTPPDUSessionContainer

class STLS1(object):

	def create_stream (self, src_IP ,teid):
		return STLStream(
			packet = 
				STLPktBuilder(
					pkt = Ether() / IP(src = src_IP, dst = "10.0.0.1") / UDP(sport=2152, dport=2152) / GTP_U_Header(gtp_type=255, E=1, next_ex=0x85, teid=teid) /
						GTPPDUSessionContainer(type=0, QFI=0, NextExtHdr=0) / IP() / (10*'x')
				),

	mode = STLTXCont())

	def get_streams (self, direction = 0,  **kwargs) :
		# create 1 stream
		sessions = []
		for i in range(101, 121):                #1,10		
			for teid in range(1001,2000) :  #1,1000
				session = [str(i) + ".0.0.10", teid]
				sessions.append(session)
		return [ self.create_stream(session[0], session[1]) for session in sessions ]
		#return [ self.create_stream(10), self.create_stream(100) ]

def register():
    return STLS1()
