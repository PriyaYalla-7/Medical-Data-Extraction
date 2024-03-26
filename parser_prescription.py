from backend.src.parser_generic import MedicalDoc_parse
import re
class PrescritionParser(MedicalDoc_parse):
    def __init__(self,text):
        MedicalDoc_parse.__init__(self,text)
    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address':self.get_field('patient_address'),
            'medicines' : self.get_field('medicines'),
            'directions' : self.get_field('directions'),
            'refill': self.get_field('refill')
        }
    def get_field(self,field):
        patient_dict={
            'patient_name': { 'pattern' : 'Name:(.*)Date', 'flags':0} ,
            'patient_address':{'pattern' : 'Address:(.*)\n','flags':0} ,
            'medicines':{'pattern' : 'Address:[^\n]*(.*)Directions','flags':re.DOTALL} ,
            'directions': {'pattern' : 'Directions:(.*)Refill','flags':re.DOTALL} ,
            'refill' :{'pattern' : 'Refill:(.*)','flags':0}
        }

        patient_obj=patient_dict.get(field)
        if patient_obj:
            match = re.findall(patient_obj['pattern'], self.text,patient_obj['flags'])
            if len(match) > 0:
                return match[0].strip()


    # def get_name(self):
    #     pattern = 'Name:(.*)Date'
    #     match = re.findall(pattern, self.text)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    # def get_address(self):
    #     pattern = 'Address:(.*)\n'
    #     match = re.findall(pattern, self.text)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    # def get_medicines(self):
    #     pattern = 'Address:[^\n]*(.*)Directions'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    # def get_directions(self):
    #     pattern = 'Directions:(.*)Refill'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match)>0:
    #         return match[0].strip()
    #
    # def refill(self):
    #     pattern = 'Refill:(.*)'
    #     match = re.findall(pattern, self.text, flags=re.DOTALL)
    #     if len(match)>0:
    #         return match[0].strip()

if __name__=='__main__':
    doc_text= ''' Dr John >mith, M.D
                2 Non-Important street,
                New York, Phone (900)-323- ~2222
                
                Name:  Virat Kohli Date: 2/05/2022
                
                Address: 2 cricket blvd, New Delhi
                
                | Omeprazole 40 mg
                
                Directions: Use two tablets daily for three months
                
                Refill: 3 times'''
    pp = PrescritionParser(doc_text)
    print(pp.parse())
