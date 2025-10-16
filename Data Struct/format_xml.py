import xml.etree.ElementTree as ET
import pandas as pd
#file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = "anh"
second.text = "pham"
third.text = '20'

#create a new XML file
mydata1 = ET.ElementTree(employee)

#ghi vao file
with open("employee.xml", 'wb') as file:
    mydata1.write(file)

#doc fie XML
tree = ET.parse("employee.xml")

#lay phan tu goc
root = tree.getroot()

columns = ["firstname", "lastname", "age"]

#khoi tao 1 datafram trong
dataframe = pd.DataFrame(columns=columns)

#lap lai qua tung node 
for node in root:
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text
    age = node.find("age").text
    row_df = pd.DataFrame([[firstname, lastname, age]], columns=columns)

    dataframe = pd.concat([dataframe, row_df], ignore_index=True)

print(dataframe)