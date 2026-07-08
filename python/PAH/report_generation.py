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

# SumPAH is the 63 PAHs in the method
reportGeneralParams += '&ParameterSumPah=303801&ParameterSumPah=303795&ParameterSumPah=303798&ParameterSumPah=303960&ParameterSumPah=303804&ParameterSumPah=303783&ParameterSumPah=303831&ParameterSumPah=303858&ParameterSumPah=303840&ParameterSumPah=303951&ParameterSumPah=303786&ParameterSumPah=303948&ParameterSumPah=303828&ParameterSumPah=303780&ParameterSumPah=303825&ParameterSumPah=303837&ParameterSumPah=303873&ParameterSumPah=303876&ParameterSumPah=303912&ParameterSumPah=303924&ParameterSumPah=303834&ParameterSumPah=303810&ParameterSumPah=303807&ParameterSumPah=303903&ParameterSumPah=303822&ParameterSumPah=303864&ParameterSumPah=303957&ParameterSumPah=303897&ParameterSumPah=303852&ParameterSumPah=303888&ParameterSumPah=303915&ParameterSumPah=303954&ParameterSumPah=303939&ParameterSumPah=303945&ParameterSumPah=303885&ParameterSumPah=303900&ParameterSumPah=303882&ParameterSumPah=303918&ParameterSumPah=303870&ParameterSumPah=303640&ParameterSumPah=303861&ParameterSumPah=303906&ParameterSumPah=303645&ParameterSumPah=303894&ParameterSumPah=303634&ParameterSumPah=303637&ParameterSumPah=303909&ParameterSumPah=303933&ParameterSumPah=303816&ParameterSumPah=303843&ParameterSumPah=303813&ParameterSumPah=303891&ParameterSumPah=303777&ParameterSumPah=303930&ParameterSumPah=303927&ParameterSumPah=305098&ParameterSumPah=303963&ParameterSumPah=307181&ParameterSumPah=303936&ParameterSumPah=303921&ParameterSumPah=303819&ParameterSumPah=303846&ParameterSumPah=303849&ParameterSumPah=303867'

# The specific PAHs to graph scatterplots of
reportGeneralParams += '&ParameterReport=303780&ParameterReport=303816&ParameterReport=303849'


# Other general report parameters
# Include a graph of the Sum PAHs
reportGeneralParams += '&IncludeSumPah=0'

# Set the denominator
reportGeneralParams += '&Denominator=gram'

# Set the numerator
reportGeneralParams += '&Numerator=picomoles'

# Set the sampler type (air sampler or wristband)
reportGeneralParams += '&SamplerType=wristband'

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

# Open file  
