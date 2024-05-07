# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 23:41:04 2023

@author: Zikra
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
SVM_model = pickle.load(open('AS_model1.sav', 'rb'))
st.set_page_config(layout="wide")
selected= option_menu(
    menu_title=None,
    options=["Home","Behind your backpain","Backsplaining AS","BackStory of AS","Get Tested ASap","Locate a Rheumatologist","Healthy Back Tips"],
    icons=["house","back","book","pen","pencil","map","star"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "1!important", "background-color": "rgb(129, 216, 208)"},
       "icon": {"color": "black", "font-size": "18px"}, 
       "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "white","font":"sans serif"},
       "nav-link-selected": {"background-color": "rgb(129, 216, 208)"},}
    )
if selected =="Home":
    st.video('Recording 2023-04-07 170431.mp4')
    col1,col2,col3 =st.columns(3)
    with col1:
        st.image("https://www.thegoodbody.com/wp-content/uploads/2022/08/7-5-percent-of-the-worlds-population-suffers-from-low-back-pain.png")
    with col2:
        st.image("https://www.thegoodbody.com/wp-content/uploads/2022/08/37-percent-say-back-pain-has-affected-their-sleep.png")
    with col3:
        st.image("https://www.thegoodbody.com/wp-content/uploads/2022/08/back-pain-is-one-of-the-most-common-reasons-for-missing-work.png")
if selected =="Behind your backpain":
    st.header('Behind your backpain')
    st.text("Your backpain could be either mechanical or inflammatory.Check out the difference.")
    col1,col2,col3=st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.image("https://pbs.twimg.com/media/DdctsURV0AUfrK3?format=jpg&name=900x900")
    with col3:
        st.write('')
    st.subheader('Mechanical back pain and inflammatory back pain are two types of back pain that have different causes and characteristics.')
    st.write('''Mechanical back pain is caused by the degeneration or injury of the structures in the back, such as the
               bones, muscles, ligaments, and discs. It is often triggered by physical activity or movement and is
               usually localized to a specific area. The pain may be sharp or dull and may worsen with certain movements
               orpositions. Mechanical back pain may also cause stiffness, limited range of motion, and muscle spasms.''')
    st.write('''Inflammatory back pain, on the other hand, is caused by inflammation in the spinal joints or other
               structures in the back. It is usually not triggered by physical activity or movement and may be present
               even at rest. The pain may be deep and aching, and may be worse in the morning or after prolonged periods
               of inactivity. Inflammatory back pain may also be accompanied by other symptoms, such as fatigue, fever,
               weight loss, and joint swelling.''')
    st.subheader('How can you distinguish if your backpain is mechanical or inflammatory?')
    st.write('''Distinguishing between mechanical back pain and inflammatory back pain can be challenging, as both types
               of back pain can have similar symptoms. However, there are some key differences that can help you
               differentiate between the two:''')
    st.write(''' *Timing:* Mechanical back pain is usually triggered by physical activity or movement, whereas inflammatory
               back pain may be present even at rest or in the morning.''')
    st.write('''*Location:* Mechanical back pain is usually localized to a specific area, whereas inflammatory back pain
               can be diffuse and affect multiple areas of the back.''')
    st.write('''*Duration:* Mechanical back pain typically lasts a few days to a few weeks, whereas inflammatory back pain
               can last for several months or even years.''')
    st.write('''*Symptoms:* Inflammatory back pain may be accompanied by other symptoms such as fatigue, fever, weight
               loss,and joint swelling, which are not typically present with mechanical back pain.''')
    st.write('''*Age:* Inflammatory back pain is more common in younger adults, typically under the age of 40, whereas
               mechanical back pain is more common in older adults.''')
    st.write('''If you suspect that you have inflammatory back pain, it is important to see a healthcare professional for
               an accurate diagnosis and appropriate treatment. Your healthcare provider may perform a physical exam,
               take a medical history, order imaging tests such as X-rays or MRI, and/or perform blood tests to check for
               markers of inflammation. They may also refer you to a specialist, such as a rheumatologist, for further
               evaluation and treatment.''')
if selected =="Backsplaining AS":
    st.header('Backsplaining AS')
    st.subheader('The Disease-')
    st.write('''Ankylosing Spondylitis (AS) (ank-ee-lo-zing spon-dee-li-tus), is a chronic inflammatory disease that
               mainly affects the back, causing inflammation of the spine. It is a form of arthritis that causes chronic
               back pain. It is a lifelong condition. In more advanced cases this inflammation can lead to ankylosis
               (new bone formation in the spine), causing sections of spine to fuse in a fixed, immobile position. AS
               can also cause inflammation, pain and stiffness in other areas of the body such as the shoulders, hips,
               ribs, heels ,small joints of the hands and feet. The hallmark feature of ankylosing spondylitis is the
               involvement of the sacroiliac joints(joints at the base of the spine) during the progression of the
               disease.''')
    st.subheader('Causes-')
    st.write('''Ankylosing Spondylosis is an autoimmune disease, the exact cause of which is unknown. It is more
               frequent in young males under 40 years. Females can also be affected. This condition is more frequent in
               genetically susceptible individuals who are HLA-B27 positive.
               Ankylosing Spondylitis is an autoimmune disease which causes inflammation in the back. Often
               misunderstood as back pain, it basically originates in the sacroiliac joint, the joint at the base of the
               spine. Ankylosing Spondylitis has no known specific cause, though genetic factors seem to be involved. In
               particular, people with a gene called HLA-B27 are at greater risk of developing AS. About 95% of people
               who have AS have a variation of HLA-B27 gene present.''')
    st.subheader('The Indicators of AS are:')
    st.write('● Age onset: before 40 years.')
    st.write('● Lower Back Pain for more than 3 months.')
    st.write('● Pain in the ankle, heel, hip, lower back, neck or shoulders.')
    st.write('● Morning Stiffness for more than 30 mins.')
    st.write('● Gets worse on rest, improves on movement.')
    st.write('● Inflammation in eyes-(Uveitis).')
    st.write('● A rigid spine.')
    st.subheader('How is Ankylosing Spondylitis diagnosed?')
    st.write('● Correct History Taking-factors like age, gender, lifestyle (smoking, etc)')
    st.write('● Blood tests- ESR levels, CRP levels and HLA-B27 test')
    st.write('● Imaging Scans- MRI of spine, sacroiliac joint. For diagnosis of AS, correct history taking is the key.')
    st.image("https://creakyjoints.org//wp-content/uploads/2019/04/0419_AS-Facts-1024x683.jpg")
    st.subheader('Statistics-')
    st.write('''In India, the prevalence of AS is around 0.2-1.4%. It is estimated that nearly 30-40 lakh people in India
               suffer from AS. It results in serious impairment of movement impacting quality of life. AS is often
               misunderstood as back pain. There has been an alarming increase of AS among young Indian adults in their
               late twenties and early thirties. AS affects 1 in 100 of the adult population and it is particularly
               prevalent in men.''')
    st.write('''A recent study conducted in 100 patients in Pune, Maharashtra, has revealed that close to 70% of AS
               patients are misdiagnosed for the initial 3 years and more, worsening their condition. The clinical study
               published in the Indian Journal of Rheumatology analyzed different factors related to Ankylosing
               Spondylitis and examined the experience of these patients with delayed diagnosis and impact on work
               productivity.''')
    st.subheader('The Problem- Delayed Diagnosis')
    st.write('''Delayed diagnosis emerged as a significant challenge for the majority of patients. The reason for late
               diagnosis is not being able to reach a specialist (rheumatologist) after the onset of the symptoms. Only
               12% of people visited a rheumatologist for the initial assessment of AS. The rest continued seeking
               treatment for back pain, one of the key symptoms of AS. 
               Although a delayed diagnosis of AS is a globally recognized problem, Data from the study suggests that 58% of the patients visited three different
               specialists before reaching a rheumatologist. Only 31% of patients were correctly diagnosed, while others
               had a difficult road to diagnosis with incorrect assessment as pain due to sedentary life, bad posture or
               pregnancy-induced pain, mechanical injury, etc. before they consulted with a rheumatologist. These
               findings correlate with the lack of awareness and misinformation among the masses about AS and the
               associated symptoms of back pain.''')
    st.write('''People with long term Ankylosing Spondylitis is a progessive disease that can cause a curved, stiff,
               immovable back. Ankylosing spondylitis is often misdiagnosed or diagnosed in later stages. AS is often
               misunderstood as normal back pain or is misdiagnosed as Rheumatoid Arthritis (RA). The symptoms of RA and
               AS are similar but AS originates clearly from the sacroiliac joint. AS is the spondylitis of the spine.
               The problem of delayed diagnosis is that it can take approximately 14 years before it is correctly
               diagnosed. Delayed diagnosis can lead to delayed treatment and worsens the condition. AS is manageable,
               the patients need to follow routine consultation and treatment plans with a rheumatologist.''')
    st.write('''Ankylosing Spondylitis cases are rare but on rise. There has been an alarming increase in AS cases among
               young Indians. But lack of awareness, misdiagnosis, or delayed diagnosis can lead to bad prognosis of the
               disease. As the diagnosis and treatment is delayed, the disease can progress and lead to a deformed
               spine. Early Diagnosis of AS is necessary and we hope that our project will help in this regard.
               As we surveyed AS, we found stories of painful journeys of patients with delayed diagnosis. We hope that the
               fast evolving technology will be helpful in early detection of disease.''')
    st.write('And next time, if someone suffers from a prolonged back pain, he/she must not ignore it as a normal back pain. But instead, get tested as early as possible.')
    st.text(' “Ankylosing Spondylitis" may sound scary but it is manageable.')
if selected == "BackStory of AS":
    st.header('Why My Back is Killing Me?')
    st.text('The following is based on actual cases:')
    st.subheader('Mysterious Back Pain Attack!')
    st.write(''' So, we are on case to help a victim of chronic back pain, to investigate why his/her back is killing him/her. The victim ,let’s say, XYZ, is a thirty year old ,living with chronic pain since late teens. That’s back and hip pain that sometimes comes and goes, it gets so bad that the victim wakes up at night in agony. First thing in the morning is waking up with a stiff body and often also experiences a brain fog. And there comes mornings when a vicious unexplained attack of backpain strikes.
               Let’s put on our detective glasses to find out why is the back killing him/her?''')
    st.subheader('A Series of Back Pain Misdiagnoses')
    st.write('''80% of adults have lower backpain in their lives. But the question is what’s wrong with this back that are causing these endless attacks. Something is aggravating this victim’s spine and we have to figure out what it is so that the victim can deal with it. Otherwise, it is just a matter of time before his/her back strikes again
               So for this episode, the victim says he/she slept all right and woke up in misery maybe he/she strained his/her back in his/her sleep. Maybe. 
               But that doesn’t explain he/she felt bad since late teens and why is he/she often so fatigued and can’t think straight. He/ she has seen dozens of doctors and no one has a good explanation.
               The victim has visited physicians, orthopedics, neurologists, spinal surgeons and many more. From rheumatoid arthritis to fibromyalgia, no one has clear explanation of it.
               Its time we crack this back attack.''')     
    st.subheader('The Usual Suspects')
    st.write('Let’s check the usual suspects.')
    st.write('*-The old, soft mattress*')
    st.write('Could be the reason of waking up in distress at night. But the victim also replaced it lately. But still same issues')
    st.write('*-A heavy box strain*')
    st.write('Could be strain after lifting a heavy object. But the strain of that kind shouldn’t last for more than a few weeks.')
    st.write('*-An old injury*')
    st.write('But this is something that is not so convincing to be the culprit of all the symptoms. Not without more evidence')
    st.write('*-Fibromyalgia-A catch-all diagnosis for musculoskeletal pain*')
    st.write('But, in it you have pain all over the body, and the victim’s pain is localized.')
    st.write('These were not enough to solve the case.')
    st.write('Lets dive deeper, let’s look to other such unsolved cases in past.')
    st.subheader('A Sinister Pattern of Back Pain')
    st.write(' All these symptoms are heard before. If we could just find a pattern, we can solve this.')
    st.write('Lets check the case files. Almost all the files involve people who had back problems relatively early in life. If they strain their back from an injury or fall, their pain would be more consistent and it wont last for more than 3 months. It’s a sure sign they need to see a doctor, but  so many doctors miss the real story.')
    st.write(' “I first had symptoms in high school and my dad and brother both had back and joint pains too.” ')
    st.write(' “Id wake up in the middle of the night in agony” ')
    st.write(' “It seemed like my pain got better with exercise and worse with rest” ')
    st.write(' “Exercise made it better, rest made it worse” ')
    st.write('Oh, there is pattern. We need to decode.')
    st.write('We need a special joint doctor!')
    st.subheader('Cracking up the Back Pain Mystery')
    st.write('We should hear it from a Rheumatologist -a special joint doctor.')
    st.write(' “This pain is different from normal mechanical back pain. After seeing the symptoms and a through physical examination, I’m strongly suspecting that this is inflammatory. There is a name to this, it is called Ankylosing Spondylitis (ank-ee-lo-zing spon-dee-li-tus), in short AS.')
    st.write('AS is a type of chronic arthritis that causes inflammation of the spine. It typically starts in early adulthood and if left untreated it can cause the bones in the spine to fuse together. Patients with AS tend to have chronic back pain which lasts more than 3 months. The pain can wake them up in the middle of the night and they feel very stiff when they wake up in  the morning. Rest makes it worse, Exercise makes it better”')
    st.write('Is there a cure to this?')
    st.write(' “Not yet, but we do have medications that can minimize symptoms and ease the flare-ups. But the most important is to come to a rheumatologists and get diagnosed ASAP.” ')
    st.write(' “Ankylosing Spondylitis is a type of chronic back pain which is inflammatory in nature. But it is manageable. We can help the victim get better”')
    st.write('After all this investigation, we finally know why the victims back is killing him/her and he/she knows about his/her problem and finally he/she can move along with life.')
    st.text('*Case Closed*')
    col1,col2,col3=st.columns(3)
    with col1:
        st.write('')
    with col2:
         st.image("https://i.pinimg.com/originals/cf/f6/c6/cff6c608ffabdc395db2f7c57742f522.jpg")
    with col3:
        st.write('')
if selected =="Get Tested ASap":
    st.warning('''Warning-This is just a basic test to detect Ankylosing Spondylitis made by using machine learning algorithm.This is not the final diagnosis of your backpain cause.
                The stages of Ankylosing Spondylitis diagnosis are:-
                ● Correct History Taking-factors like age, gender, lifestyle (smoking, etc)
                ● Blood tests- ESR levels, CRP levels and HLA-B27 test
                ● Imaging Scans- MRI of spine, sacroiliac joint.
                For diagnosis of AS, correct history taking is the key.This test is just the first step towards diagnosing AS''')
    # loading the saved models
    col1,col2,col3=st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.title('The AS Test') 
    with col3:
        st.write('')
    SVM_model = pickle.load(open('C:/Users/Zikra/AS project/AS_model1.sav', 'rb')) 

    
        #getting input data from the user
        #sex,age,as_hist,bpscore,jpscore,vas_fatigue,smoking,redeyes,stf,pain_relief
    with st.form("form1"):
            options=["1","0"]
            sex = st.selectbox('Select your Gender[1.Male, 0.Female]:', ['']+options, format_func=lambda x: 'Select an option' if x == '' else x)
            age=st.text_input(label='Enter Your Age:')
            as_hist=st.selectbox('Does anyone in your family suffers from AS or any kind of Arthritis? 1. YES  0. NO', ['']+options, format_func=lambda x: 'Select an option' if x == '' else x)
            bpscore=st.slider("On a scale of 0 to 10,rate your Backpain [Backpain consistent for more than 3 months]:",0,10)
            jpscore=st.slider("On a scale of 0 to 10,rate your Jointpain [pain in joints like knee,ankle or in the neck,back or buttocks region]:",0,10)
            vas_fatigue=st.slider("On a scale of 0 to 10,how much do you think would be your fatigue:",0,10)
            smoking=st.selectbox('Do you Smoke? 1. YES   0. NO', ['']+options, format_func=lambda x: 'Select an option' if x == '' else x)
            redeyes=st.selectbox('Do you have inflammation or redness in eyes? 1. YES   0. NO', ['']+options, format_func=lambda x: 'Select an option' if x == '' else x)
            stf=st.selectbox('Does your body feel Stiff for more than 30 mins in the morning after waking up? 1. YES   0. NO', ['']+options, format_func=lambda x: 'Select an option' if x == '' else x)
            pain_relief=st.selectbox('Does your pain gets better with movement and Exercise and worse with Rest? 1. YES   0. NO', ['']+options, format_func=lambda x: 'Select an option' if x == '' else x)
           
            submit=st.form_submit_button('Submit')
            if submit:
                if sex=='' or age=='' or as_hist=='' or vas_fatigue=='' or smoking=='' or redeyes=='' or stf=='' or pain_relief=='':
                    st.warning('Please select appropriate option for all fields')
          
        #code for prediction
    diagnosis=''
    
        #creating a button for prediction
    if st.button('Test Results'):
            SVM_prediction = SVM_model.predict([[sex,age,as_hist,bpscore,jpscore,vas_fatigue,smoking,redeyes,stf,pain_relief]])
            if (SVM_prediction[0] == 1):
                diagnosis='You might have AS'
                st.info('You have signs of inflammatory back pain.You are likely to have Ankylosing Spondylitis.But dont panic,verify this by visiting a nearby rheumatologist.The rheumatologists will examine you and suggest you some tests.These will confrim whether you have AS or not.')
            else:
                diagnosis='You are less likely to have AS'
                st.info('You have signs of mechanical back pain.You are less at risk to have AS.But it could be something else.Visit an Orthopedic or a Rheumatologists near you.')
    
    st.success(diagnosis)
  
        
if selected =="Locate a Rheumatologist":
    st.title('Locate a Rheumatologist near you')
    st.write("A Rheumatologist is a specialized Doctor who treats auto-immune diseases,diseases related to inflammatory backpain, like Ankylosing Spondylitis and others.")
    components.iframe("https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d120640.48259543694!2d72.87603182996148!3d19.106994317516204!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1srheumatologist%20near%20me!5e0!3m2!1sen!2sin!4v1680959396821!5m2!1sen!2sin" )
    
if selected =="Healthy Back Tips":
    st.header('Healthy Back Tips')
    col1,col2,col3=st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.image("https://www.neurosurg.org/editor-uploads/website-2266/tips-to-prevent-spine-problems-infographic-neuroscience-specialists-1643094664.jpg")
    with col3:
        st.write('')
    col1,col2,col3=st.columns(3)
    with col1:
         st.write('')
    with col2:
         st.image("https://www.eihmd.com/wp-content/uploads/2018/12/tips-for-healthy-spine.jpg")
    with col3:
         st.write('')
        
     
   
