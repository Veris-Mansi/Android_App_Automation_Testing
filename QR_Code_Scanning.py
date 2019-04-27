import zxing

#from qrtools.qrtools import QR
#import qrtools
reader = zxing.BarCodeReader()
barcode = reader.decode("QR_code/qr_2.png")

print(barcode)

