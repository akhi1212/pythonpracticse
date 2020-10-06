import xml.etree.ElementTree as ET
import time;

tree = ET.parse('C:/vin/vins/366.xml')
root = tree.getroot()

for child in root: 
 for element in child:
   #print(element[1].tag)
   #print(element[1].text) 
   #print(element[1].attrib)
   print('Here is the vin value' ,':' , element[1].attrib['vin'])
   print('Here is the bestMakeName value' ,':' ,element.attrib['bestMakeName'])
   print('Here is the bestModelName value' ,':' ,element.attrib['bestModelName'])
   print('Here is the bestStyleName value' ,':' ,element.attrib['bestStyleName'])
   print('Here is the styleid value' ,':' ,element[2].attrib['id'])
   print('Here is the styleid value' ,':' ,element[2].attrib)
   vin_value = element[1].attrib['vin']
   bestMakeName = element.attrib['bestMakeName']
   bestModelName = element.attrib['bestModelName']
   bestStyleName = element.attrib['bestStyleName']
   styleid = element[2].attrib['id']


   
curr_time = time.strftime("%Y%m%d-%H%M%S")   
file = open("C:/Users/Akhilesh.Gairola/Desktop/pyhton/output/allvalue_output_" "_" + curr_time + ".txt", "w") 
file.write("The vin value is :" + vin_value + "\n") 
file.write("The bestMakeName value is :" + bestMakeName + "\n") 
file.write("The bestModelName value is :" + bestModelName + "\n") 
file.write("The  bestStyleName value is :" + bestStyleName + "\n") 
file.write("The  styleid value is :" + styleid + "\n") 
file.close()    