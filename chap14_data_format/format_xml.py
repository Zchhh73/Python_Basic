#
import xml.etree.ElementTree as ET

'''
tree = ET.parse('note.xml')
print(type(tree))
root = tree.getroot()
print(root)
print(root.tag)   

for index, child in enumerate(root):
    print('第{0}个{1}元素，属性：{2}'.format(index,child.tag,child.attrib))
    for i, child_child in enumerate(child):
        print('标签:{0}，内容:{1}'.format(child_child.tag,child_child.text))
'''
# XPath方法
tree = ET.parse('note.xml')
root = tree.getroot()

node = root.find('./Note')
print(node.tag, node.attrib)
node = root.find('./Note/CDate')
print(node.text)
node = root.find('./Note/CDate/..')
print(node.tag, node.attrib)

node = root.find('.//CDate')
print(node.text)

node = root.find('./Note[@id]')
print(node.tag, node.attrib)

node = root.find("./Note[@id='2']")
print(node.tag, node.attrib)

node = root.find("./Note[3]")
print(node.tag, node.attrib)

node = root.find("./Note[last()-1]")
print(node.tag, node.attrib)

node = root.findall("./Note")
print(node[1].attrib)