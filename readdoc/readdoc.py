from docx import Document
import csv
import glob

docDatas = []
for docName in glob.glob("wenben/*.docx"):
    doc = Document(docName)
    beigao = ""
    susongTime = ""
    panjueTime = ""
    for para in doc.paragraphs:
        if "被告" in para.text and "：" in para.text:
            colonIdx = para.text.find("：")
            if colonIdx is -1:
                beigao = para.text
            else:
                beigao = para.text[colonIdx + 1:]
            continue
        elif "20" in para.text:
            liAnIdx = para.text.find("20")
            susongTime = para.text[liAnIdx : liAnIdx + 11]
            print(susongTime)
            continue
        elif para.text.startswith("二〇"):
            panjueTime = para.text
            continue
    docDatas.append([docName[7:-5], beigao, susongTime, panjueTime])

with open('result.csv', mode='w') as result_file:
    result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    result_writer.writerow(["判决书", "被告", "诉讼发生时间", "判决时间"])
    for row in docDatas:
        result_writer.writerow(row)
