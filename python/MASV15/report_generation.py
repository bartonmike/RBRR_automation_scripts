import csv 
import os
from requests import Session
from requests_ntlm import HttpNtlmAuth
import requests

   
#https://stackoverflow.com/questions/55821047/download-an-ssrs-report-in-python-using-requests

session = requests.Session()
session.auth = HttpNtlmAuth(username='YOUR_SSRS_USERNAME', password='YOUR_SSRS_PASSWORD')
reportServerURL = 'https://YOUR_SSRS_REPORT_SERVER_URL/ReportServer/Pages/ReportViewer.aspx?%2fREPORT_FOLDER%2fREPORT_NAME:Format=PDF&'
#reportIndividualParams = ''
reportGeneralParams = '&SampleIDGroup=1000&SampleIDGroup=1001&SampleIDGroup=1002&SampleIDGroup=1003&SampleIDGroup=1004&SampleIDGroup=1005&SampleIDGroup=1006&SampleIDGroup=1007&SampleIDGroup=1008&SampleIDGroup=1009&SampleIDGroup=1010&SampleIDGroup=1011&SampleIDGroup=1012&SampleIDGroup=1013&SampleIDGroup=1014&SampleIDGroup=1015&SampleIDGroup=1016&SampleIDGroup=1017&SampleIDGroup=1018&SampleIDGroup=1019&SampleIDGroup=1020&SampleIDGroup=1021&SampleIDGroup=1022&SampleIDGroup=1023&SampleIDGroup=1024&SampleIDGroup=1025&SampleIDGroup=1026&SampleIDGroup=1027&SampleIDGroup=1028&SampleIDGroup=1029&SampleIDGroup=1030'

# Chemicals seen in all samplers
reportGeneralParams += '&ParameterReport=217&ParameterReport=348&ParameterReport=415&ParameterReport=529&ParameterReport=674&ParameterReport=721&ParameterReport=889&ParameterReport=942&ParameterReport=1018&ParameterReport=1176&ParameterReport=1355&ParameterReport=1492&ParameterReport=1627&ParameterReport=400113&ParameterReport=400126&ParameterReport=400154&ParameterReport=400197&ParameterReport=400218&ParameterReport=400264&ParameterReport=400301&ParameterReport=400327&ParameterReport=400341&ParameterReport=400359&ParameterReport=400386&ParameterReport=400407&ParameterReport=400432&ParameterReport=400451&ParameterReport=400478&ParameterReport=400502&ParameterReport=400519&ParameterReport=400537&ParameterReport=400561&ParameterReport=400584&ParameterReport=400607&ParameterReport=400629&ParameterReport=400651&ParameterReport=400673&ParameterReport=400694&ParameterReport=400718&ParameterReport=400735&ParameterReport=400759&ParameterReport=400781&ParameterReport=400806&ParameterReport=400824&ParameterReport=400851&ParameterReport=400876&ParameterReport=400902&ParameterReport=400927&ParameterReport=400951&ParameterReport=400978&ParameterReport=401003&ParameterReport=401029&ParameterReport=401054&ParameterReport=401078&ParameterReport=401106&ParameterReport=401129&ParameterReport=401153&ParameterReport=401178&ParameterReport=401204&ParameterReport=401227&ParameterReport=401251&ParameterReport=401279&ParameterReport=401304&ParameterReport=401326&ParameterReport=401351&ParameterReport=401379&ParameterReport=401402&ParameterReport=401428&ParameterReport=401451&ParameterReport=401477&ParameterReport=401503&ParameterReport=401526&ParameterReport=401548&ParameterReport=401573&ParameterReport=401599&ParameterReport=401624&ParameterReport=401651&ParameterReport=401677'

# For chemical specific pages
# Endocrine disruptor chemical page
reportGeneralParams += '&EdParameter1=400341&EdParameter1=400629'

# Pesticide chemical page
reportGeneralParams += '&PesticideParameter1=401029&PesticideParameter1=401351'

# Industrial chemical page
reportGeneralParams += '&IndustrialParameter1=217&IndustrialParameter1=348'

# Pharmaceutical chemical page
reportGeneralParams += '&PharmParameter1=529'

# Flame retardant chemical page
reportGeneralParams += '&FlameRetardantParameter1=721&FlameRetardantParameter1=401029'

# Personal care product chemical page
reportGeneralParams += '&PcpParameter1=401326&PcpParameter1=401624'

# Other general report parameters
# Convert mMol to another unit.
reportGeneralParams += '&MolesConvert=1000000000&'

# Use nanograme or moles to report out
reportGeneralParams += 'NgOrMol=Mol&'

# Cutoff data that is less than a certain value
reportGeneralParams += 'DataCutoff=0.1'

# Open file (switch the comments to run a smaller test batch)
file = 'study_participants.csv'
#file = 'study_participants_test.csv'

with open(#) as file_obj: 
      
    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(file_obj) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:
        #0 is sample_id, 2 is Participant Name, 3 is File Name
        sampleID = row[0]
        participantName = row[2]
        fileName = row[3]
        print (sample_id,participant_name,file_name)
        response = session.get(reportServerURL + 'sampleID=' + sampleID + '&participantName=' + participantName.replace(' ','%20') + reportGeneralParams,stream=True)
        print (response.status_code)
        stiid = ''
        with open('reports\\' + file_name +'.pdf','wb') as pdf:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)
        sampleID = ''
        participantName = ''
        fileName = ''
session.close()
        #print(row[1])  
