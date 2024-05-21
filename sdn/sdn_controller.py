from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3

class SimpleSwitch(app_manager.RyuApp):
OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

def __init__(self, *args, **kwargs):
super(SimpleSwitch, self).__init__(*args, **kwargs)

@set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def packet_in_handler(self, ev):
msg = ev.msg
datapath = msg.datapath
ofproto = datapath.ofproto
parser = datapath.ofproto_parser

in_port = msg.match['in_port']
actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]
out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id, in_port=in_port, actions=actions)
datapath.send_msg(out)