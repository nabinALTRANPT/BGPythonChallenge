#!/usr/bin/python
#  -*- coding: utf-8 -*-
#exportingtojson
import json

from xml.dom import minidom

from main import data
from lxml import etree, objectify
from lxml.etree import XMLSyntaxError

from main import data

# start xml creation - three files will be created
def validate_xml_files():


    i = 0

    for item in data :
       def create_xml(stringMember , intMember ,filename ):


         root = minidom.Document()



         xml = root.createElement('a')
         xml = root.createElementNS ('http://example.org/types', 'bit:a')
         xml.setAttribute ("xmlns:bit", "http://example.org/types")

         root.appendChild(xml)

         Child = root.createElement('stringMember')
         Child.appendChild(root.createTextNode(stringMember))

         xml.appendChild(Child)

         Child1 = root.createElement ('intMember')
         Child1.appendChild (root.createTextNode ((str(intMember))))
         xml.appendChild (Child1)

         xml_str =root.toprettyxml(indent="\t")
         save_path_file =(filename)

         with open(save_path_file,"w") as f:
            f.write(xml_str)

       create_xml(data[i]['stringMember'] , data[i]['intMember'] ,data[i]['file'] )
       i=i+1

    #validation
    def xml_validator(some_xml_string, xsd_file='/path/to/my_schema_file.xsd'):
           try:
               schema = etree.XMLSchema (file=xsd_file)
               parser = objectify.makeparser (schema=schema)
               objectify.fromstring (some_xml_string, parser)

           except XMLSyntaxError as ex:
               # handle exception here
               print(some_xml_string)
               xsdfile = open (xsd_file)
               for line in xsdfile:
                   print line
               xsdfile.close ()
               print "Oh NO!, my xml file does not validate"
               print str (ex)


    for item in data:
           xml_file = open (item['file'], 'r')
           xml_string = xml_file.read ()
           xml_file.close ()
           xml_validator (xml_string, 'd.xsd')


# end xml creation and validation

#export to json
def exportxmltojson():

    jdata=[
                    {'jfile':'jdata1.json','stringMember':'str1','intMember':1},
                    {'jfile':'jdata2.json','stringMember':'str2','intMember':2},
                    {'jfile':'jdata3.json','stringMember':'str3','intMember':3}
    ]

    i=0
    for item in data:

            jsonString = ['filename' ,'filename' ,'filename']
            doc = minidom.parse(open(item['file']))

            with open (item['file'], 'r') as f:
                xmlString = f.read ()

            stringMemberValue=''
            stringMember = doc.getElementsByTagName("stringMember")
            for x in stringMember:
                stringMemberValue = x.firstChild.nodeValue

            intMemberValue=''
            intMember = doc.getElementsByTagName("intMember")
            for x in intMember:
                intMemberValue = x.firstChild.nodeValue


            jsonString[i] = json.dumps (  {'stringMember':stringMemberValue,'intMember':int(intMemberValue)} )

            def create_json (filename):

                with open (filename, 'w') as f:
                 f.write (jsonString[i])


            create_json(jdata[i]['jfile'])
            i = i + 1

#export complete
def menu():
## Show menu ##
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1.create XML files and validate")
    print ("2. Exported XML Files to JSON")
    print ("3. QUIT")
    print (30 * '-')



     ## Get input ###
    choice = raw_input ('Enter your choice [1-3] : ')
    ### Convert string to int type ##
    choice = int (choice)
    print choice
            ### Take action as per selected menu-option ###
    if choice == 1:
                validate_xml_files ()
                print ("Your three xml file are created and validated Thank you")
                menu()

    elif choice == 2:
                exportxmltojson ()

                print ("XML FILES ARE EXPORTED TO  JSON FILE Thank you")
                menu()

    elif choice == 3:
                print ("QUIT THE PROGRAM")
                quit ()

    else:  ## default ##
                print ("Invalid number. Try again...")
                menu()



if __name__=='__main__':
     menu()





