# sdn_topology.py

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

def run_topology():
    net = Mininet(controller=RemoteController, link=TCLink)

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)

    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    s1 = net.addSwitch('s1')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.start()
    c0.start()
    s1.start([c0])

    CLI(net)
    net.stop()

if __name__ == '__main__':
    run_topology()
