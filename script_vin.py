import xml.etree.ElementTree as ET
import time;

tree = ET.parse('C:/vin/vins/366.xml')
root = tree.getroot()

 
for child in root: 
 for element in child:
   #print(element[1].tag)
   #print(element[1].text) 
   #print(element[1].attrib)
   vin_value = element[1].attrib['vin']
   print('Here is the vin value' ,':' , element[1].attrib['vin'])
   print(vin_value)

curr_time = time.strftime("%Y%m%d-%H%M%S")   
file = open("C:/Users/Akhilesh.Gairola/Desktop/pyhton/output/vin_output_" "_" + curr_time + ".txt", "w") 
file.write("The vin value is :" + vin_value) 
file.close() 
