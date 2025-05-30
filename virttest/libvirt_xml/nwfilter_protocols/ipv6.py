"""
ipv6 protocl support class(es)

http://libvirt.org/formatnwfilter.html#nwfelemsRulesProtoIPv6
"""

from virttest.libvirt_xml import accessors, xcepts
from virttest.libvirt_xml.nwfilter_protocols import base


class Ipv6(base.TypedDeviceBase):
    """
    Create new Ipv6 xml instances

    Properties:

    attrs: libvirt_xml.nwfilter_protocols.Ipv6.Attr instance
    """

    __slots__ = ("attrs",)

    def __init__(self, type_name="file", virsh_instance=base.base.virsh):
        accessors.XMLElementNest(
            "attrs",
            self,
            parent_xpath="/",
            tag_name="ipv6",
            subclass=self.Attr,
            subclass_dargs={"virsh_instance": virsh_instance},
        )
        super(Ipv6, self).__init__(
            protocol_tag="ipv6", type_name=type_name, virsh_instance=virsh_instance
        )

    def new_attr(self, **dargs):
        """
        Return a new Attr instance and set properties from dargs

        :param dargs: dict of attributes
        :return: new Attr instance
        """
        new_one = self.Attr(virsh_instance=self.virsh)
        for key, value in list(dargs.items()):
            setattr(new_one, key, value)
        return new_one

    def get_attr(self):
        """
        Return ipv6 attribute dict

        :return: None if no ipv6 in xml, dict of ipv6's attributes.
        """
        try:
            ipv6_node = self.xmltreefile.reroot("/ipv6")
        except KeyError as detail:
            raise xcepts.LibvirtXMLError(detail)
        node = ipv6_node.getroot()
        ipv6_attr = dict(list(node.items()))

        return ipv6_attr

    class Attr(base.base.LibvirtXMLBase):
        """
        Ipv6 attribute XML class

        Properties:

        srcmacaddr: string, MAC address of sender
        srcmacmask: string, Mask applied to MAC address of sender
        dstmacaddr: string, MAC address of destination
        dstmacaddr: string, Mask applied to MAC address of destination
        srcipaddr: string, Source IP address
        srcipmask: string, Mask applied to source IP address
        dstipaddr: string, Destination IP address
        dstipmask: string, Mask applied to destination IP address
        ip_protocol: string, Layer 4 protocol identifier
        srcportstart: string, Start of range of valid source ports; requires protocol
        srcportend: string, End of range of valid source ports; requires protocol
        dstportstart: string, Start of range of valid destination ports; requires protocol
        dstportend: string, End of range of valid destination ports; requires protocol
        comment: string, text with max. 256 characters
        """

        __slots__ = (
            "srcmacaddr",
            "srcmacmask",
            "dstmacaddr",
            "dstmacmask",
            "srcipaddr",
            "srcipmask",
            "dstipaddr",
            "dstipmask",
            "ip_protocol",
            "srcportstart",
            "srcportend",
            "dstportstart",
            "dstportend",
            "dscp",
            "comment",
        )

        def __init__(self, virsh_instance=base.base.virsh):
            accessors.XMLAttribute(
                "srcmacaddr",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="srcmacaddr",
            )
            accessors.XMLAttribute(
                "srcmacmask",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="srcmacmask",
            )
            accessors.XMLAttribute(
                "dstmacaddr",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="dstmacaddr",
            )
            accessors.XMLAttribute(
                "dstmacmask",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="dstmacmask",
            )
            accessors.XMLAttribute(
                "srcipaddr",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="srcipaddr",
            )
            accessors.XMLAttribute(
                "srcipmask",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="srcipmask",
            )
            accessors.XMLAttribute(
                "dstipaddr",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="dstipaddr",
            )
            accessors.XMLAttribute(
                "dstipmask",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="dstipmask",
            )
            accessors.XMLAttribute(
                "ip_protocol",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="protocol",
            )
            accessors.XMLAttribute(
                "srcportstart",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="srcportstart",
            )
            accessors.XMLAttribute(
                "srcportend",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="srcportend",
            )
            accessors.XMLAttribute(
                "dstportstart",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="dstportstart",
            )
            accessors.XMLAttribute(
                "dstportend",
                self,
                parent_xpath="/",
                tag_name="ipv6",
                attribute="dstportend",
            )
            accessors.XMLAttribute(
                "comment", self, parent_xpath="/", tag_name="ipv6", attribute="comment"
            )

            super(self.__class__, self).__init__(virsh_instance=virsh_instance)
            self.xml = "<ipv6/>"
