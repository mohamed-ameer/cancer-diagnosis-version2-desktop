from urllib import response
from rest_framework import viewsets
from .serializers import *
from cancerDetect.models import *
from rest_framework.response import Response 
from keras.models import load_model
import tensorflow as tf
import numpy as np
import tensorflow as tf
import cv2
from pathlib import Path
import os
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# the input 

def scan(z, num, typeCancer, num2=3):
    img = cv2.imread(str(z))
    img = cv2.resize(img, (num,num))
    img = np.array(img, dtype="float32")
    img = np.reshape(img, (1,num,num, num2))


# Load the TFLite model and allocate tensors.

    interpreter = tf.lite.Interpreter(model_path=typeCancer)
    interpreter.allocate_tensors()

# Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

# Test the model on random input data.
    input_shape = input_details[0]['shape']

    print("*"*50, input_details)
# the input 
    interpreter.set_tensor(input_details[0]['index'], img)

    interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.


# the o/p -= if conditions none or true & a ,b,c,d,.....
    output_data = interpreter.get_tensor(output_details[0]['index'])
    # print('aaaaaaaaaaaaaaaaaaaa')
    # print(output_data)
    # print('aaaaaaaaaaaaaaaaaaaa')
    # print(type(output_data))
    return output_data


class CancerDetectViewSet(viewsets.ModelViewSet):
    queryset = CancerDetect.objects.all()
    serializer_class = CancerDetectSerializer


    def create(self, request, *args, **kwargs): 
        print('sdadsa')
        print(request)
        print(request.data)
        print('sasfdasdfasfasfasfasfas')
        scan_data = request.data
        query = request.query_params.get('type')
        new_scan = CancerDetect.objects.create(picture=scan_data["picture"])  
        new_scan.save()
        cancer_type = ''
        explanation=''
        recommendation=''

        path_img = os.path.join(BASE_DIR, 'media')+'\\'+str(scan_data["picture"])
        if query == 'skin':
            s = scan(path_img, 28, 'skin.tflite') 
            az = str(s)

            x = request.POST.get('has_cancer', False)
            if str(x) == 'true':
                x = True
            if(az.index('1') == 2):
                cancer_type = 'akiec'
                x = True    
            elif(az.index('1') == 5):
                cancer_type = 'basal cell carcinoma'
                explanation='often appears as a slightly transparent bump on the skin, though it can take other forms,occurs when DNA damage from exposure to ultraviolet (UV) radiation'
                recommendation='Make an appointment with your doctor if you observe changes in the appearance of your skin, such as a new growth, a change in a previous growth or a recurring sore.'
                x = True
            elif(az.index('1') == 8):
                cancer_type = 'benign keratosis-like lesions'
                explanation='a common benign (non-cancerous) skin growth. People tend to get more of them as they get older. Seborrheic keratoses are usually brown, black or light tan. The growths (lesions) look waxy or scaly and slightly raised'
                recommendation='Seborrheic keratoses are harmless and not contagious. They dont need treatment, but you may decide to have them removed if they become irritated by clothing or you dont like how they look.See your doctor if the appearance of the growth bothers you or if it gets irritated or bleeds when your clothing rubs against it.'
                x = True
            elif(az.index('1') == 11):
                cancer_type = 'Dermatofibroma'
                explanation='small, harmless growths that appear on the skin.'
                recommendation='Removal is typically the simplest and most successful option, but it requires a surgical procedure.'
                x = True
            elif(az.index('1') == 14):
                cancer_type = 'melanoma'
                explanation='e'
                recommendation='e'
                x = True
            elif(az.index('1') == 17):
                cancer_type = 'melanocytic nevi'
                explanation='y'
                recommendation='y'
                x = True
            elif(az.index('1') == 20):
                cancer_type = 'vasc'
                explanation='j'
                recommendation='j'
                x = True
            else:
                cancer_type = 'no cancer detect'
                explanation=''
                recommendation=''
                x = False
            # new_scan2 = CancerDetail.objects.create(patient_name=scan_data["patient_name"], has_cancer=x,cancer_type=cancer_type, explanation=explanation, recommendation=recommendation)  
            # new_scan2.save()                



            # serializer = CancerDetectSerializer(new_scan)
            # return Response(serializer.data)
        elif query == 'breast':
            s = scan(path_img, 227, 'breast.tflite') 
            az = str(s)
            
            x = request.POST.get('has_cancer', False)
            if str(x) == 'true':
                x = True
            cancer_type = 'akiec'
            if(az.index('9') == 4 or az.index('9') ==5 or az.index('9') ==6 ):
                cancer_type = 'Benign Masses'
                explanation='(non-cancerous) breast conditions are very common, and most women have them. In fact, most breast changes are benign. Unlike breast cancers, benign breast conditions are not life-threatening. But some are linked with a higher risk of getting breast cancer later on. '
                recommendation='Most types of benign breast disease dont require treatment. Your healthcare provider may recommend treatment if you have atypical hyperplasia or a different kind of benign breast disease that increases your future risk of breast cancer. Some benign breast changes may cause signs or symptoms . consult a doctor or a specialist in this case.'
                x = True
            elif(az.index('9') != 4 or az.index('9') !=5 or az.index('9') !=6):
                cancer_type = 'Malignant Masses'
                explanation='tumor that grows in or around the breast tissue, mainly in the milk ducts and glands. A tumor usually starts as a lump or calcium deposit that develops as a result of abnormal cell growth.'
                recommendation='An early detection, frequently medical therapy, such as endocrine therapy or chemotherapy will be recommended first to decrease the size of the tumor in the breast, or decrease the disease and the lymph nodes, and importantly to evaluate the response of the cancer to the treatment'
                x = True
            else:
                cancer_type = 'no cancer detect'
                explanation=''
                recommendation=''
                x = False


        elif query == 'lung':
            s = scan(path_img, 224, 'lung.tflite') 
            az = str(s)
            
            x = request.POST.get('has_cancer', False)
            if str(x) == 'true':
                x = True
            cancer_type = 'akiec'
            if(az.index('0.99') == 13):
                cancer_type = 'Benign'
                explanation='A benign lung tumor is an abnormal growth of tissue that serves no purpose and is found not to be cancerous.'
                recommendation='Adults aged 50 to 80 years who have a 20 pack-year smoking history and currently smoke or have quit within the past 15 years'
                x = True
            elif(az.index('0.99') == 2):
                cancer_type = 'Adenocarcinoma'
                explanation='It falls under the umbrella of non-small cell lung cancer (NSCLC) and has a strong'
                recommendation='Adults aged 50 to 80 years who have a 20 pack-year smoking history and currently smoke or have quit within the past 15 years'
                x = True
            elif(az.index('0.99') == 24):
                cancer_type = 'Squamous Cell Carcinoma'
                explanation='Non-small cell lung carcinoma (NSCLC) makes up approximately 85% of all lung cancers and is characterized by transformed'
                recommendation='Adults aged 50 to 80 years who have a 20 pack-year smoking history and currently smoke or have quit within the past 15 years'
                x = True
            else:
                cancer_type = 'no cancer detect'
                explanation=''
                recommendation=''
                x = False



        elif query == 'colon':
            s = scan(path_img, 128, 'colon.tflite') 
            az = str(s)
            x = request.POST.get('has_cancer', False)
            if str(x) == 'true':
                x = True
            cancer_type = 'akiec'
            if(az.index('0.5') != 2):
                cancer_type = 'Adenocarcinoma'
                explanation='Cancer that forms in the glandular tissue, which lines certain internal organs and makes and releases substances in the body, such as mucus, digestive juices, and other fluids.'
                recommendation='the first line is surgery, it is done to remove cancer and some of the surrounding tissue. Chemotherapy.'
                x = True
            elif(az.index('0.5') == 2):
                cancer_type = 'Benign Tissue'
                explanation='usually discovered because a patient is examined for symptoms—such as rectal bleeding, changes in bowel habits '
                recommendation='Surgery should be performed, They are removed so they can be examined under a microscope to make a diagnosis. Surgery  is the usual treatment.'
                x = True
            else:
                cancer_type = 'no cancer detect'
                explanation=''
                recommendation=''
                x = False


        elif query == 'blood':
            s = scan(path_img, 224, 'blood.tflite') 
            az = str(s)
            print('hehhee')
            print('99999999')
            print(az)
            print(az.index('9.9'))
            print('[[2.3581698e-03 5.3128852e-03 4.0376549e-06 9.9232495e-01]]')
            x = request.POST.get('has_cancer', False)
            if str(x) == 'true':
                x = True
            cancer_type = 'akiec'
            if(az.index('9.9') == 16):
                cancer_type = '[Malignant] Pre-B'
                explanation='B-cell lymphomas are malignant tumors of B-lymphocytes. They arise at all stages of B-cell differentiation, from immature B-lymphocytes in the bone-marrow through to terminally'
                recommendation='Treatment usually depends both on the type of lymphoma and the stage (extent) of the disease Most often, the treatment is chemotherapy (chemo)'
                x = True
            elif(az.index('9.9') == 2):
                cancer_type = 'Benign'
                explanation='are noncancerous growths in the body. They can occur anywhere in the body, grow slowly, and have clear borders. Unlike cancerous tumors, they don’t spread to other parts of the body.'
                recommendation='it’s still a good idea to make an appointment with your doctor as soon as you detect a growth or new symptoms that could indicate a tumor. This includes skin lesions or unusual-looking moles.'
                x = True
            elif(az.index('9.9') == 30):
                cancer_type = '[Malignant] Pro-B'
                explanation='When you have B-cell lymphoma, your body makes too many abnormal B cells. These cells cant fight infections well. They can also spread to other parts of your body.'
                recommendation='B-cell acute lymphoblastic leukemia is a serious condition, but with treatment, remission is possible.'
                x = True
            elif(az.index('9.9') == 44):
                cancer_type = '[Malignant] Early Pre-B'
                explanation='A type of cancer that forms in B cells (a type of immune system cell). B-cell lymphomas may be either indolent (slow-growing) or aggressive (fast-growing)..'
                recommendation='You will likely receive chemotherapy and medication as the first round of treatment. Other treatments will depend on how your body responds to the chemotherapy.'
                x = True
            else:
                cancer_type = 'no cancer detect'
                explanation=''
                recommendation=''
                x = False


        elif query == 'brain':
            s = scan(path_img, 80, 'brain.tflite', 1) 
            az = str(s)
            print('hehhee')
            print('99999999')
            print(az)
            print(az.index('9.9'))
            print('[[2.3581698e-03 5.3128852e-03 4.0376549e-06 9.9232495e-01]]')
            x = request.POST.get('has_cancer', False)
            if str(x) == 'true':
                x = True
            cancer_type = 'akiec'
            if(az.index('1') == 5):
                cancer_type = 'Meningioma'
                explanation='is a tumor that forms on membranes that cover the brain and spinal cord just inside the skull.'
                recommendation='see a doctor;may order a brain scan: an MRI and/or a CT scan. These will allow the doctor to locate the meningioma and determine its size'
                x = True
            elif(az.index('1') == 2):
                cancer_type = 'Glioma'
                explanation='primary brain tumors , can affect your brain function and be life-threatening depending on its location and rate of growth..'
                recommendation='treatment options include surgery, radiation therapy, chemotherapy, targeted therapy and experimental clinical trials.'
                x = True
            elif(az.index('1') == 8):
                cancer_type = 'No Tumor'
                explanation='Normal'
                recommendation='Avoid dangerous radiation: If the body is exposed to some radiation, such as: cancer radiation, nuclear bomb radiation, it leads to cell distortion and disorder.'
                x = True
            elif(az.index('1') == 11):
                cancer_type = 'Pituatary'
                explanation='abnormal growths that develop in your pituitary gland'
                recommendation='If you know that multiple endocrine neoplasia, type 1 (MEN 1) runs in your family, talk to your doctor about periodic tests that may help detect a pituitary tumor early.'
                x = True
            else:
                cancer_type = 'no cancer detect'
                explanation=''
                recommendation=''
                x = False


        return Response({
            'cancer_type': cancer_type,
            'explanation': explanation,
            'recommendation': recommendation 

        })
    


# class CancerDetailViewSet(viewsets.ModelViewSet):
#     queryset = CancerDetail.objects.all()
#     serializer_class = CancerDetailSerializer



