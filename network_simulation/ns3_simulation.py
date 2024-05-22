import ns.core
import ns.network
import ns.internet
import ns.point_to_point
import ns.applications

def main():
    ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
    ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)

    nodes = ns.network.NodeContainer()
    nodes.Create(2)

    pointToPoint = ns.point_to_point.PointToPointHelper()
    pointToPoint.SetDeviceAttribute("DataRate", ns.network.DataRateValue(ns.network.DataRate("5Mbps")))
    pointToPoint.SetChannelAttribute("Delay", ns.network.TimeValue(ns.core.Seconds(2)))

    devices = pointToPoint.Install(nodes)

    stack = ns.internet.InternetStackHelper()
    stack.Install(nodes)

    address = ns.internet.Ipv4AddressHelper()
    address.SetBase(ns.network.Ipv4Address("10.1.1.0"), ns.network.Ipv4Mask("255.255.255.0"))

    interfaces = address.Assign(devices)

    echoServer = ns.applications.UdpEchoServerHelper(9)
    serverApps = echoServer.Install(nodes.Get(1))
    serverApps.Start(ns.core.Seconds(1.0))
    serverApps.Stop(ns.core.Seconds(10.0))

    echoClient = ns.applications.UdpEchoClientHelper(interfaces.GetAddress(1), 9)
    echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(1))
    echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(1.0)))
    echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(1024))

    clientApps = echoClient.Install(nodes.Get(0))
    clientApps.Start(ns.core.Seconds(2.0))
    clientApps.Stop(ns.core.Seconds(10.0))

    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

if __name__ == '__main__':
    main()
