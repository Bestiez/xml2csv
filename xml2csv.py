import xml.etree.ElementTree as ET
import csv
from xml.dom.minidom import parseString
import lxml.etree
import io


class xml_converter():
    @staticmethod
    def header_rows():
        tree = ET.parse("files/xml_file.xml")
        root = tree.getroot()
        Resident_data = open('files/csv_file.csv', 'w')
        # create the csv writer object
        csvwriter = csv.writer(Resident_data)
        resident_head = []
        # print (root)
        doc = lxml.etree.parse("files/xml_file.xml")
        # count = doc.xpath('count(///pc)')
        # print (count)
        count_header = 1
        for member, elem in ET.iterparse("files/xml_file.xml", events=('start', 'end')):
            # print(member)
            # print(elem)
            country_list = []
            header = []
            if count_header == 1:
                # header = []
                # header.append('country')
                header.append('example_headID')
                header.append('name')
                header.append('m')
                header.append('mId')
                header.append('markId')
                header.append('type')
                header.append('location')
                header.append('device')
                header.append('placards')
                header.append('stop')
                header.append('gearId')
                '''
                header.append('community')
                header.append('county')
                header.append('code')
                header.append('size')
                header.append('s')
                '''
                with open('files/csv_file.csv', 'a', newline='') as csvfile:
                    wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
                    # add column varibles that should be written to the csv file
                    wtr.writerow(header)
                count_header = count_header + 1

            # name0 = member.get('country')
            # country_list.append(name0)

            if elem.tag == 'example' and member == 'end':
                for i in elem.findall('example_head'):
                    name1 = i.get('example_headId')
                    country_list.append(name1)

                    name2 = i.find('name').text
                    country_list.append(name2)
                    # print(name2)
                    name3 = i.find('m').text
                    country_list.append(name3)
                    # print(name3)
                    name4 = i.find('m').get('mId')
                    country_list.append(name4)
                    # print(name4)
                    for mark in i.findall('markerId'):
                        name5 = mark.find('markId').text
                        name6 = mark.find('markId').get('type')
                    country_list.append(name5)
                    country_list.append(name6)
                    name7 = i.find('location').text
                    country_list.append(name7)
                    name8 = i.find('lineup').get('device')
                    country_list.append(name8)

                    # print(name8)
                    doc_pcs = lxml.etree.parse('files/xml_file.xml')
                    # count=doc.getElementsByTagName("pc").length
                    counter_pcs = 1
                    pcs_list = [country_list[0], country_list[1], country_list[2], country_list[3], country_list[4],country_list[5], country_list[6], country_list[7]]
                    for post in i.findall('placards'):
                        count_pcs = int(doc_pcs.xpath('count(./example_head[@example_headId="{0}"]/placards/placard)'.format(country_list[0])))
                        # count_pcs = int(doc.xpath('count(./example_head/placards/placard)'))
                        # print(count_pcs)
                        count1_pcs = count_pcs
                        while count_pcs >= 1:
                            # print(count_pcs)
                            # print(post.text)
                            # print(post[-count_pcs].text)
                            # if count_pcs == count1_pcs:
                            #     country_list.append(post[-count_pcs].text)

                            if counter_pcs == 1:
                                country_list.append(post[-count_pcs].text)
                                # print(country_list)
                                with io.open('files/csv_file.csv', 'a', newline='') as csvfile:
                                    wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
                                    # add column varibles that should be written to the csv file
                                    # wtr.writerow(header)
                                    wtr.writerow(country_list)
                                counter_pcs = counter_pcs + 1
                            else:
                                pcs_list.append(post[-count_pcs].text)
                                # print(pcs_list)
                            count_pcs = count_pcs - 1
                            with io.open('files/csv_file.csv', 'a', newline='') as csvfile:
                                wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
                                # add column varibles that should be written to the csv file
                                # wtr.writerow(header)
                                # print(pcs_list)
                                if pcs_list.__len__() == 8:
                                    pass
                                else:
                                    # print(pcs_list)
                                    wtr.writerow(pcs_list)
                            pcs_list = [country_list[0], country_list[1], country_list[2], country_list[3],country_list[4], country_list[5], country_list[6], country_list[7]]
                            # print(name8)
                    doc_station = lxml.etree.parse('files/xml_file.xml')
                    # count=doc.getElementsByTagName("pc").length
                    counter_station = 1
                    stop_list = [country_list[0], country_list[1], country_list[2], country_list[3], country_list[4],country_list[5], country_list[6], country_list[7], '']
                    gearId_list = [country_list[0], country_list[1], country_list[2], country_list[3],country_list[4], country_list[5], country_list[6], country_list[7],country_list[8], '']
                    for post_station in i.findall('lineup'):
                        count_station = int(doc_station.xpath('count(./example_head[@example_headId="{0}"]/lineup/station)'.format(country_list[0])))
                        count_stop = int(doc_station.xpath('count(./example_head[@example_headId="{0}"]/lineup/station/stop)'.format(country_list[0])))
                        if count_station >= 1:
                            for poster_station in post_station.findall('station'):
                                print(poster_station.get('gearId'))
                                gearId_list.append(poster_station.get('gearId'))
                                if count_stop >= 1:
                                    for stop_station in post_station.findall('stop'):
                                        stop_list.append(stop_station.find('stop').text)
                                    print(stop_list)


                                with io.open('files/csv_file.csv', 'a', newline='') as csvfile:
                                    wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
                                    # add column varibles that should be written to the csv file
                                    wtr.writerow(stop_list)
                                    wtr.writerow(gearId_list)
                                    if pcs_list.__len__() == 9:
                                        pass
                                    else:
                                        # print(pcs_list)
                                        wtr.writerow(pcs_list)
                                    stop_list = [country_list[0], country_list[1], country_list[2], country_list[3],country_list[4], country_list[5], country_list[6], country_list[7], '']
                                    gearId_list = [country_list[0], country_list[1], country_list[2], country_list[3],country_list[4], country_list[5], country_list[6], country_list[7],country_list[8], '']

                            pcs_list = [country_list[0], country_list[1], country_list[2], country_list[3],country_list[4], country_list[5], country_list[6], country_list[7],country_list[8]]
                            count_station = count_station - 1
                            # print(count_station)
                    country_list = []


"""            #postal codes
            name8 = member.find('location').text
            country_list.append(name8)
            name9 = member.find('lineup').get('device')
            country_list.append(name9)

            for mark1 in member.find('example_head').find('asServed').findall('a'):
                name21 = mark1.find('community').text
                name22 = mark1.find('county').text
                name23 = mark1.find('a').get('code')
                name24 = mark1.find('a').get('size')
                name25 = mark1.find('s').text
            country_list.append(name21)
            country_list.append(name22)
            country_list.append(name23)
            country_list.append(name24)
            country_list.append(name25)

            with io.open('on_char_example_cable_20170725.csv','a',newline='') as csvfile:
                wtr = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
                # add column varibles that should be written to the csv file
                #wtr.writerow(header)
                wtr.writerow(country_list)

"""

if __name__ == '__main__':
    xml_converter.header_rows()
