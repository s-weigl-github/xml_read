#########################
###  write datasets to a xml file
###  Sebastian Weigl
###  ver.02 alpha - 19.02.2014
#########################
#import urllib.request
#from xml.etree.ElementTree import parse

import xml.etree.cElementTree as ET

root = ET.Element("liste")

doc = ET.SubElement(root, "person")

field1 = ET.SubElement(doc, "field1")
field1.set("name", "node1")
field1.text = "some value1"

field2 = ET.SubElement(doc, "field2")
field2.set("name", "node2")
field2.text = "some value2"

field3 = ET.SubElement(doc, "field3")
field3.set("name", "node3")
field3.text = "some value3"

field4 = ET.SubElement(doc, "field4")
field4.set("name", "node4")
field4.text = "some value4"

field5 = ET.SubElement(doc, "field5")
field5.set("name", "node5")
field5.text = "some value5"

field6 = ET.SubElement(doc, "field6")
field6.set("name", "node6")
field6.text = "some value6"

field7 = ET.SubElement(doc, "field7")
field7.set("name", "node7")
field7.text = "some value7"

field8 = ET.SubElement(doc, "field8")
field8.set("name", "node8")
field8.text = "some value8"

tree = ET.ElementTree(root)
tree.write("filename.xml")

## E-o-F
