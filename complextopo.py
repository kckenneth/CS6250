from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom

# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        #TODO: Create your Mininet Topology here!
        # Host, Link, Ethernet, WiFi, 3G link configuration
        hostConfig = {'cpu': cpu}
        linkConfig = {'bw': 25, 'delay': '2ms', 'loss': 0,
                      'max_queue_size': max_queue_size}
        wifiConfig = {'bw': 10, 'delay': '6ms', 'loss':3,
                      'max_queue_size': max_queue_size}
        threeGConfig = {'bw': 3, 'delay': '10ms', 'loss': 8,
                      'max_queue_size': max_queue_size}

        # Hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        h1 = self.addHost('h1', **hostConfig)
        h2 = self.addHost('h2', **wifiConfig)
        h3 = self.addHost('h3', **threeGConfig)

        # Wire receiver
        self.addLink(h1, s1, port1=0, port2=1, **linkConfig)
        self.addLink(s1, s2, port1=2, port2=1, **linkConfig)
        self.addLink(s2, s3, port1=2, port2=1, **linkConfig)

        self.addLink(s3, h2, port1=2, port2=0, **wifiConfig)

        self.addLink(s2, s4, **linkConfig)

        self.addLink(s4, h3, **threeGConfig)
