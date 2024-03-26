from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import PrescritionParser
from parser_patient_details import PatientDetailsParser
POPPLER_PATH= r'D:\Data Analyst\Medical project (2nd project)\poppler-24.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    full_text = ''
    if len(pages)>0:
        page=pages[0]
        processed_img = util.preprocess_img(page)
        text = pytesseract.image_to_string(processed_img, lang='eng')
        full_text ='\n'+ text
    #return full_text
    # if file_format='prescription':
    #     pass
    # elif file_format='patient_details':
    #     pass
    if file_format=='prescription':
        data_extracted=PrescritionParser(full_text).parse()
    elif file_format=='patient_details':
        data_extracted=PatientDetailsParser(full_text).parse()
    else:
        raise Exception("Invalid document format:{}")

    return data_extracted

if __name__=='__main__':
    data = extract('../resources/patient_details/pd_1.pdf','patient_details')
    print(data)
