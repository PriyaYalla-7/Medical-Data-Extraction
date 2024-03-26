from backend.src.parser_generic import MedicalDoc_parse
import re
class PatientDetailsParser(MedicalDoc_parse):
    def __init__(self,text):
        MedicalDoc_parse.__init__(self,text)
    def parse(self):
        return {
            'patient_name': self.get_patient_name(),
            'phone_number':self.get_phoneno(),
            'vaccination': self.vaccination(),
            'medical_problems': self.medical_problems()
        }

    def get_patient_name(self):
        pattern = 'Patient Information(.*?)\(\d{3}\)'
        match = re.findall(pattern, self.text, flags=re.DOTALL)
        name=''
        if match:
            name=self.remove_noise_from_name(match[0])
        return name

    def get_phoneno(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][1]

    def vaccination(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0]

    def medical_problems(self):
        pattern = 'List any Medical Problems .*?:(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def remove_noise_from_name(self,name):
        name = name.replace('Birth Date', '').strip()
        pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [ \d]+)'
        date_matches = re.findall(pattern, name)
        if date_matches:
            dm = date_matches[0][0]
            name = name.replace(dm, '').strip()
        return name

if __name__=='__main__':
    text= '''47/12/2020
                Patient Medical Record
                
                       
                Patient Information Birth Date
                Kathy Crawford May 6 1972
                (737) 988-0851 Weight
                9264 Ash Dr 95
                New York City, 10005 .
                United States Height:
                190
                In Case of Emergency
                m _ eee ee
                Simeone Crawford 9266 Ash Dr
                New York City, New York, 10005
                Home phone United States
                (990) 375-4621
                Work phone
                Genera! Medical History
                
                 
                
                 
                
                Chicken Pox (Varicella):
                
                IMMUNE IMMUNE
                Have you had the Hepatitis B vaccination?
                
                No
                List any Medical Problems (asthma, seizures, headaches):
                
                Migraine'''
    pd= PatientDetailsParser(text)
    print(pd.parse())