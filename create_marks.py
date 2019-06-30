#Project : cis_systems
#Developer : George Sakellariou
#Date :2019-06-29

import pandas
import qrcode
def read_csv(filename):
    return pandas.read_csv(filename)

def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def write_qr_code(filename,img):
    with open(filename,'wb') as qr_image:
        img.save(qr_image)
        qr_image.close()

if __name__=='__main__':
    data =read_csv('test_data.csv')
    print(data.iloc[0])
    img=create_qr_code(data.iloc[0])
    write_qr_code('test_qr.png',img)