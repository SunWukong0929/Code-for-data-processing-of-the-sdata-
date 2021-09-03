import SimpleITK as sitk
import numpy as np
import cv2
 
def convert_from_dicom_to_jpg(img,low_window,high_window,save_path):
  lungwin = np.array([low_window*1.,high_window*1.])
  newimg = (img-lungwin[0])/(lungwin[1]-lungwin[0]) 
  newimg = (newimg*255).astype('uint8')        
  cv2.imwrite(save_path, newimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
 
if __name__ == '__main__':
 

  dcm_image_path = '/DICOM_image/post201901L.dcm'   
  output_jpg_path = 'PNG_image/post201901L.png'
  ds_array = sitk.ReadImage(dcm_image_path)     
  img_array = sitk.GetArrayFromImage(ds_array)  
 
  shape = img_array.shape
  img_array = np.reshape(img_array, (shape[1], shape[2])) #获取array中的height和width
  high = np.max(img_array)
  low = np.min(img_array)
  convert_from_dicom_to_jpg(img_array, low, high, output_jpg_path)  
  print('FINISHED')