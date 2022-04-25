# code for manoor health report card

from time import time
from typing import Counter
from unicodedata import name
from datetime import date

# input section starts here 
name   = input("Enter patient  name       : ")
age    = int(input("Enter patient age         : "))
gender = input("Enter Gender              : ")
refno  = input("Refred by                 : ")
test   = input("Enter the name of the test/pacakage: ")
today  = date.today()
gender = gender.lower()
test   = test.lower()


#functions defined here

#genral detailes on test
def genral_det():
            print("\n")
            print("-------------------------------------------------------------------")
            print("Le'valor Health                   Patinet Name : " + name )
            print("Manoor, Edappal, Kerala, India    Gender       : " + gender)
            print("Mob: +91 8086 5000 23             Age          :",age)
            print("Web: www.levalorhealth.com        Date         :", today)
            print("mail:info@levalorhealth.com       Referd by    :", refno)
            print("--------------------------------------------------------------------")
            print("\n")

def error():
           print("\n")
           print(" Something went wrong")
           print(" please contact Mr.Mohammed Jaseem ")
           print(" Mob  : +91 8086  5000  23")
           print(" Mail : mail@mohammedjaseem.me")
           print(" Web  : www.mohammedjaseem.me")

def thanks_footer():
        print("------------------------------------------------------------------")
        footer = """


                   
Lab Technician                                        Lab Incharge





    
                    Thanks for choosing Le'valor Health
                           www.levalorhealth.com"""
        print("\n")
        print("\n")
        print(footer)
        
# Funtions delared ends here

#Single test's start here 

#suagr test start here
if test == "sugar":
        print("\n")
        print("""
            Please Choose type of test:
                 1. Fasting blood sugar - fbs
                 2. Post prandial blood sugar - ppbs
                 3. Random blood sugar - rbs
                 4. 2 Sugar test  - 2sug""")
        print("\n")
        sugartype = input("Enter the type of sugar test: ")
        sugartype = sugartype.lower()
        print("\n")
        if sugartype == "fbs":
            fbs = input("Enter the fbs value: ")
            genral_det()
            print("\n")
            print("     Investigation        Patinet Value    Refrence Value")
            print("-------------------------------------------------------------")
            print("  Fasting blood sugar      ",fbs,"mg/dl      70 - 110mg/dl")   
            thanks_footer()    

        elif sugartype == "ppbs":
            ppbs = input("Enter the ppbs value: ")
            genral_det()
            print("\n")
            print("     Investigation           Patinet Value    Refrence Value")
            print("-------------------------------------------------------------")
            print("  Post prandial blood sugar  ",ppbs,"mg/dl      70 - 140mg/dl")
            thanks_footer() 
            
        elif sugartype == "rbs":
            rbs = input("Enter the rbs value: ")
            genral_det()
            print("\n")
            print("     Investigation           Patinet Value    Refrence Value")
            print("-------------------------------------------------------------")
            print("  Random blood sugar        ",rbs,"mg/dl        80 - 140mg/dl")
            thanks_footer() 
        
        elif sugartype == "2sug":
            ppbs2 = input("Enter the ppbs value: ")
            fbs2  = input("Enter the fbs value: ")
            genral_det()
            print("\n")
            print("     Investigation           Patinet Value    Refrence Value")
            print("-------------------------------------------------------------")
            print("  Fasting blood sugar        ",fbs2,"mg/dl       70 - 110mg/dl")
            print("  Post prandial blood sugar  ",ppbs2,"mg/dl       70 - 140mg/dl")
            thanks_footer() 
        
        else:
            error()  

#cholesterol test start here
elif test == "chol":
        chovalue = input("Enter the cholestrol value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("  Cholesterol               ",chovalue,"mg/dl         <200 Desirable")
        print("                                               200 - 230 Border Line")
        print("                                               > 230 High mg/dl")
        thanks_footer()

#triglyceridetest start here
elif test == "tgl":
        tglvalue = input("Enter the triglyceride value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("  Triglyceride              ",tglvalue,"mg/dl         80 - 200 mg/dl")
        thanks_footer()

#urea test start here
elif test == "urea":
        urea = input("Enter the urea value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("  Urea                      ",urea,"mg/dl         16.6 - 48.5 mg/dl")
        thanks_footer()

#creatinine test start here
elif test == "cre":
        cre = input("Enter the creatinine value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        if gender == "male":
            print("  Creatinine                ",cre,"mg/dl         0.7 - 1.2 mg/dl")
        else:
            print("  Creatinine                ",cre,"mg/dl         0.5 - 0.9 mg/dl")
        thanks_footer()

#uricacid test start here
elif test == "uric":
        uric = input("Enter the uric acid value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        if gender == "male":
            print("  Uric Acid                 ",uric,"mg/dl         3.7 - 7.0 mg/dl")
        else:
            print("  Uric Acid                 ",uric,"mg/dl         2.4 - 5.7 mg/dl")
        thanks_footer()

#Liver Funstion test start here
elif test == "bil":
        bil = float(input("Enter the Total bilirubin value: "))
        dbill = float(input("Enter the Direct bilirubin value: "))
        ibill = bil - dbill
        ibill = round(ibill,2)
        genral_det()
        print("\n")
        print("                      Bilirubin")
        print("                      ---------")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("  Total Bilirubin           ",bil,"mg/dl         0.2 - 1.0 mg/dl")
        print("  Direct Bilirubin          ",dbill,"mg/dl         0.0 - 0.2 mg/dl")
        print("  Indirect Bilirubin        ",ibill,"mg/dl         0.0 - 1.0 mg/dl")
        thanks_footer()

#sgot test start here
elif test == "sgot":
        sgot = input("Enter the SGOT value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     SGOT                   ",sgot,"IU/L        5.0 - 35.0 IU/L")
        thanks_footer()

#sgpt test start here
elif test == "sgpt":
        sgpt = input("Enter the SGPT value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     SGPT                   ",sgpt,"IU/L        5.0 - 35.0 IU/L")
        thanks_footer()

#Total Protine test start here
elif test == "pro":
        pro = input("Enter the Total Protine value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Total Protine           ",pro,"gr/dl         6.0 - 8.0 gr/dl")
        thanks_footer()
    
#albumin test start here
elif test == "alb":
        alb = input("Enter the Albumin value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Albumin                 ",alb,"gr/dl         2.5 - 5.5 gr/dl")
        thanks_footer()

#alkaline phos test start here
elif test == "alp":
        alkp = input("Enter the Alkaline Phosphate value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        if age <= 17:
            print("     Alkaline Phosphate      ",alkp,"IU/L         104 - 390 IU/L")
        else:
            print("     Alkaline Phosphate      ",alkp,"IU/L         25 - 140 IU/L")
        thanks_footer()

#haemoglobin test start here
elif test == "hb":
        hb = input("Enter the Haemoglobin value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        if gender == "male":
            print("     Haemoglobin             ",hb,"gr/dl         13.0 - 17.0 gr/dl")
        else:
            print("     Haemoglobin             ",hb,"gr/dl         12.0 - 15.0 gr/dl")
        thanks_footer()

#esr test start here
elif test == "esr":
        esr = input("Enter the ESR value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     ESR                     ",esr,"mm/Hour         <20 mm/Hour")
        thanks_footer()

#calcium test start here
elif test == "cal":
        cal = input("Enter the Calcium value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Calcium                  ",cal,"""mg/dl        Children 0 - 10 days 7.6 - 10.4 mg/dI
                                               Children 10 days - 2 years 9.0 - 11.0
                                               Children 2 - 12 years 8.8 - 10.8 mg/dl
                                               Children 12 - 18 years 8.4 - 10.2 mg/
                                               Adults 18 - 60 years 8.6 - 10.0 mg/dI
                                               Adults 60 -90 years 8.8 - 10.2 mg/dI
                                               Adults > 90 years 8.2 - 9.6 mg/dI""")
        thanks_footer()

#rafactor test start here
elif test == "ra":
        ra = input("Enter the R-A-Factor value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     R-A-Factor              ",ra,"IU/ml         Upto 20 IU/ml")
        thanks_footer()

#sodium test start here
elif test == "sod":
        sod = input("Enter the Sodium value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Sodium                  ",sod,"mEq/L         135 - 155 mEq/L")
        thanks_footer()

#potassium test start here
elif test == "pot":
        pot = input("Enter the Potassium value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Potassium               ",pot,"mEq/L         3.5 - 5.6 mEq/L")
        thanks_footer()

#urine pregnancy test start here
elif test == "upt":
        urine = input("Enter the Urine Pregnancy value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Urine Pregnancy         ",urine)
        thanks_footer()

#HIV test start here
elif test == "hiv":
        hiv = input("Enter the HIV value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     HIV                     ",hiv)
        thanks_footer()

#hbsag test start here
elif test == "hbsag":
        hbsag = input("Enter the HbsAg value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     HbsAg                   ",hbsag)
        thanks_footer()

#hcv test start here
elif test == "hcv":
        hcv = input("Enter the HCV value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     HCV                     ",hcv)
        thanks_footer()

#vdrl test start here
elif test == "vdrl":
        vdrl = input("Enter the VDRL value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     VDRL                    ",vdrl)
        thanks_footer()

#blood pressure test start here
elif test == "bp":
        sys = input("Enter the Systolic value: ")
        dia = input("Enter the Diastolic value: ")
        genral_det()
        print("\n")
        print("     Investigation           Patinet Value    Refrence Value")
        print("-------------------------------------------------------------")
        print("     Systolic                ",sys,"mmHg         <120 mmHg")
        print("     Diastolic               ",dia,"mmHg         <80 mmHg")
        thanks_footer()


#Grouptest choosing start here
elif (test == "lip"):
    # test number 1 ( Lipid test)
    print("\n")
    print("You choosed Lipid profile test ")
    cho     = float(input("Enter cho level : "))
    chotgl  = float(input("Enter TGL level : "))
    chohdl  = float(input("Enter HDL level : "))
    chovldl = chotgl/5 # VLDL = TGL/5
    choldl  = cho - chohdl - chovldl # LDL = CHO - HDL - VLDL
    print("\n")

    genral_det()
    print("                           LIPID PROFIE")
    print("                           ------------")
    print("\n")
    print("     Investigation        Patinet Value    Refrence Value")
    print("-------------------------------------------------------------")
    print("Cholesterol level       : ", cho," mg/dl   130 - 200 mg/dl")
    print("TGL level               : ", chotgl," mg/dl   80  - 200 mg/dl")
    print("LDL level               : ", choldl," mg/dl   Less than 160 mg/dl")
    print("HDL level               : ", chohdl,"  mg/dl   Above 40 mg/dl")
    print("VLDL level              : ", chovldl,"  mg/dl   Below 40 mg/dl")
    thanks_footer()

elif (test == "urine"):
    # test number 2 (Urine test)
    print("\n")
    print("You choosed Urine test")
    urinecolor      = input("Enter urine color           : ")
    urineappearance = input("Enter urine appearance      : ")
    urinereaction   = input("Enter urine reaction        : ")
    urinesugar      = input("Enter urine sugar level     : ")
    urineprotein    = input("Enter protein level         : ")
    print("\n")
    print ("Microscopic examination of urine")
    print("\n")
    urinepuscell    = input("Enter urine puscells level  : ")
    urinerbc        = input("Enter urine RBC level       : ")
    urineepithelial = input("Enter urine epithelial level: ")
    urinecast       = input("Enter urine cast level      : ")
    urinecrys       = input("Enter urine crystals level  : ")
    urinebacteria   = input("Enter urine bacteria level  : ")

    genral_det()
    print("                           Urine Routine")
    print("                           -------------")
    print("\n")
    print("     Investigation        Patinet Value ")
    print("----------------------------------------")
    print("Urine color               :", urinecolor)
    print("Urine appearance          :", urineappearance)
    print("Urine reaction            :", urinereaction)
    print("Urine sugar               :", urinesugar)
    print("Urine protein             :", urineprotein)
    print("Urine pusscells           :", urinepuscell)
    print("Urine RBC                 :", urinerbc)
    print("Urine epithelial          :", urineepithelial)
    print("Urine cast                :", urinecast)
    print("Urine crystals            :", urinecrys)
    print("Urine bacteria            :", urinebacteria)
    thanks_footer()


elif (test == "lft"):
    # test number 3 (LFT test)
    print("\n")
    print("You choosed LIVER FUNCTIONAL TEST")
    lft_total_billi          = input("Enter total LFT Billirubin    : ")
    lft_direct_billi         = input("Enter direct LFT Billirubin   : ")
    lft_sgot_ast             = float(input("Enter Sgot ast                : "))
    lft_sgpt_alt             = float(input("Enter Sgpt alt                : "))
    lft_total_protien        = float(input("Enter total LFT protien       : "))
    lft_albumin              = float(input("Enter LFT albumin             : "))
    lft_alkaline_phosphatase = float(input("Enter LFT alkaline phosphatase: "))

    #auto calculations
    lft_indirect_billi       = float(lft_total_billi) - float(lft_direct_billi)
    lft_indirect_billi       = round(lft_indirect_billi,2)
    lft_globulin             = float(lft_total_protien) - float(lft_albumin)
    lft_globulin             = round(lft_globulin,2)
    lft_ag_ratio_calc        = float(lft_albumin) / float(lft_globulin)
    lft_ag_ratio_calc        = round(lft_ag_ratio_calc,2)
    
    genral_det()
    print("                    LIVER FUNCTIONAL TEST")
    print("                    ---------------------")
    print("\n")
    print("     Investigation        Patinet Value    Refrence Value")
    print("-------------------------------------------------------------")
    print("Total Billirubin        :    ", lft_total_billi,"mg/dl      0.2 - 1.0 mg/dl")
    print("Direct Billirubin       :    ", lft_direct_billi,"mg/dl      0.0 - 0.2 mg/dl")
    print("Indirect Billirubin     :    ", lft_indirect_billi,"mg/dl      0.0 - 1.0 mg/dl")
    print("Sgot (ast)              :    ", lft_sgot_ast, "iu/L      05 - 35 iu/L")
    print("Sgpt (alt)              :    ", lft_sgpt_alt, "iu/L      05 - 35 iu/L")
    print("Total protien           :    ", lft_total_protien, "gr/dl      6 - 8 gr/dl")
    print("Albumin                 :    ", lft_albumin, "gr/dl      2.5 - 5.5 gr/dl")
    print("Globulin                :    ", lft_globulin, "gr/dl      1.5 -  3.5 gr/dl")
    print("Alkaline phosphatase    :    ", lft_alkaline_phosphatase, "iu/L     25 - 140 iu/L")
    print("A/g ratio               :    ", lft_ag_ratio_calc )
    thanks_footer()

elif (test == "rft"):
    # test number 4 (RFT test)
    print("\n")
    print("You choosed RFT test")
    rft_blood_urea           = float(input("Enter blood urea level        : "))
    rft_blood_creatinine     = input("Enter blood creatinine level  : ")
    rft_uric_acid            = input("Enter uric acid level         : ")
    print("\n")
    
    genral_det()
    print("               Renal Function Test")
    print("               -------------------")
    print("\n")
    print("     Investigation        Patinet Value    Refrence Value")
    print("-------------------------------------------------------------")
    print("Blood Urea level       :  ",rft_blood_urea,"mg/dl       16.6 - 48.5 mg/dl")
    if (gender == "male"):
            print("Blood Creatinine level :   ",rft_blood_creatinine,"mg/dl       0.7 - 1.2 mg/dl")
            print("Uric Acid level        :   ",rft_uric_acid,"mg/dl       3.7 - 7.0 mg/dl")
    else:
            print("Blood Creatinine level :   ",rft_blood_creatinine,"mg/dl       0.5 - 0.9 mg/dl")
            print("Uric Acid level        :   ",rft_uric_acid,"mg/dl       2.4 - 5.7 mg/dl")
    thanks_footer()

elif (test == "cbc"):
    # test number 5 (CBC test)
    print("\n")
    print("You choosed CBC test")
    cbc_hb                  = input("Enter Hb level                : ")
    cbc_wbc                 = input("Enter WBC level               : ")
    print("\n")
    print("Differential Counts")
    print("-------------------")
    cbc_neutrophils         = input("Enter neutrophils level       : ")
    cbc_lymphocytes         = input("Enter lymphocytes level       : ")
    cbc_eosinophils         = input("Enter eosinophils level       : ")
    cbc_monocytes           = input("Enter monocytes level         : ")
    cbc_basophils           = input("Enter basophils level         : ")
    cbc_rbc                 = input("Enter RBC level               : ")
    cbc_platelets           = input("Enter platelets level         : ")
    cbc_pcv                 = input("Enter pcv level               : ")
    cbc_mcv                 = input("Enter mcv level               : ")
    cbc_mch                 = input("Enter mch level               : ")
    cbc_mchc                = input("Enter mchc level              : ")
    cbc_esr                 = input("Enter esr level               : ")

    genral_det()
    print("               Complete blood count")
    print("               --------------------")
    print("\n")
    print("     Investigation        Patinet Value              Refrence Value")
    print("----------------------------------------------------------------------")
    if (gender == "male"):
        print("Haemoglobin            :  ",cbc_hb,"grams/dl            13.0 - 17.0 grams/dl")
    else:
        print("Haemoglobin level      :  ",cbc_hb,"grams/dl               12.0 - 15.0 grams/dl") 
    print("Total WBC Count        :  ",cbc_wbc,"/cumm               4000 - 11000/cumm")
    print("\n")
    print("Differential Counts")
    print("-------------------")
    print("Neutrophils            :  ",cbc_neutrophils,"%                   40 - 70%")
    print("Lymphocytes            :  ",cbc_lymphocytes,"%                   20 - 40%")
    print("Eosinophils            :  ",cbc_eosinophils,"%                    0 - 5%")
    print("Monocytes              :  ",cbc_monocytes,"%                     0 - 2%")
    print("Basophils              :  ",cbc_basophils,"%                     0-1%")
    if (gender == "male"):
        print("RBC                    :  ",cbc_rbc,"million/cumm        4.5 - 6.0 million/cumm")
    else:
        print("RBC                    :  ",cbc_rbc,"million/cumm               4.0 - 5.5 million/cumm") 
    print("Platelets              :  ",cbc_platelets,"Lakhs/cumm           1.5 - 4.5 Lakhs/cumm")
    print("PCV (Hct)              :  ",cbc_pcv,"%                   40 - 60%")
    print("MCV                    :  ",cbc_mcv," fl                 83 - 101 fl")
    print("MCH                    :  ",cbc_mch," Pg                 27 - 33 Pg")
    print("MCHC                   :  ",cbc_mchc," g/dl               30 - 36 g/dl")
    print("ESR                    :  ",cbc_esr,"mm/hour               < 20 mm/hour")
    thanks_footer()

# package test's start here
elif (test == "pkg"):
    print(""" 
    You choosed package test
    1. 500  - Genaral Health Checkup
    2. 700  - Masater Health Checkup
    3. 1000 - Executive Health Checkup
    4. 1500 - Diabetic Health Checkup
    5. 2500 - Post Covid Health Checkup
    """)
      
    package_test = int(input("Enter your choice : "))
    if (package_test == 500):
        print("\n")
        print("Genaral Health Checkup")
        print("--------------------")
        print("Enter details for cbc test")
        cbc_hb                  = input("Enter Hb level                : ")
        cbc_wbc                 = input("Enter WBC level               : ")
        print("\n")
        print("Differential Counts")
        print("-------------------")
        cbc_neutrophils         = input("Enter neutrophils level       : ")
        cbc_lymphocytes         = input("Enter lymphocytes level       : ")
        cbc_eosinophils         = input("Enter eosinophils level       : ")
        cbc_monocytes           = input("Enter monocytes level         : ")
        cbc_basophils           = input("Enter basophils level         : ")
        cbc_rbc                 = input("Enter RBC level               : ")
        cbc_platelets           = input("Enter platelets level         : ")
        cbc_pcv                 = input("Enter pcv level               : ")
        cbc_mcv                 = input("Enter mcv level               : ")
        cbc_mch                 = input("Enter mch level               : ")
        cbc_mchc                = input("Enter mchc level              : ")
        cbc_esr                 = input("Enter esr level               : ")
        print("\n")
        #2suagr input here
        print("Enter Values of 2 sugar test")
        print("----------------------------")
        fbs2  = input("Enter the fbs value: ")
        ppbs2 = input("Enter the ppbs value: ")
        print("\n")
        
        #lipid profile input here
        print("Enter values of Lipid profile test")
        print("----------------------------------")
        cho     = float(input("Enter cho level : "))
        chotgl  = float(input("Enter TGL level : "))
        chohdl  = float(input("Enter HDL level : "))
        chovldl = chotgl/5 # VLDL = TGL/5
        choldl  = cho - chohdl - chovldl # LDL = CHO - HDL - VLDL
        print("\n")

        #rft input here
        print("Enter values of RFT test")
        print("------------------------")
        rft_blood_urea           = float(input("Enter blood urea level        : "))
        rft_blood_creatinine     = input("Enter blood creatinine level  : ")
        rft_uric_acid            = input("Enter uric acid level         : ")
        print("\n")

        #rtf input here
        print("Enter values of LFT test")
        print("------------------------")
        lft_total_billi          = input("Enter total LFT Billirubin    : ")
        lft_direct_billi         = input("Enter direct LFT Billirubin   : ")
        lft_sgot_ast             = float(input("Enter Sgot ast                : "))
        lft_sgpt_alt             = float(input("Enter Sgpt alt                : "))
        lft_total_protien        = float(input("Enter total LFT protien       : "))
        lft_albumin              = float(input("Enter LFT albumin             : "))
        lft_alkaline_phosphatase = float(input("Enter LFT alkaline phosphatase: "))

            #auto calculations in rft
        lft_indirect_billi       = float(lft_total_billi) - float(lft_direct_billi)
        lft_indirect_billi       = round(lft_indirect_billi,2)
        lft_globulin             = float(lft_total_protien) - float(lft_albumin)
        lft_globulin             = round(lft_globulin,2)
        lft_ag_ratio_calc        = float(lft_albumin) / float(lft_globulin)
        lft_ag_ratio_calc        = round(lft_ag_ratio_calc,2)

        #urien routine input here
        print("Enter values of urien routine test")
        print("----------------------------------")
        urinecolor      = input("Enter urine color           : ")
        urineappearance = input("Enter urine appearance      : ")
        urinereaction   = input("Enter urine reaction        : ")
        urinesugar      = input("Enter urine sugar level     : ")
        urineprotein    = input("Enter protein level         : ")
        print("\n")

        print ("Microscopic examination of urine")
        print ("--------------------------------")
        print("\n")
        urinepuscell    = input("Enter urine puscells level  : ")
        urinerbc        = input("Enter urine RBC level       : ")
        urineepithelial = input("Enter urine epithelial level: ")
        urinecast       = input("Enter urine cast level      : ")
        urinecrys       = input("Enter urine crystals level  : ")
        urinebacteria   = input("Enter urine bacteria level  : ")
        print("\n")

        #bp input here
        print("Enter values of BP test")
        sys = input("Enter the Systolic value: ")
        dia = input("Enter the Diastolic value: ")

        #package print start here
        genral_det()
        print("               Genaral Health Check up")
        print("               -----------------------")
        print("\n")
        print("     Investigation        Patinet Value              Refrence Value")
        print("----------------------------------------------------------------------")
        if (gender == "male"):
            print("Haemoglobin            :  ",cbc_hb,"grams/dl            13.0 - 17.0 grams/dl")
        else:
            print("Haemoglobin level      :  ",cbc_hb,"grams/dl               12.0 - 15.0 grams/dl") 
        print("Total WBC Count        :  ",cbc_wbc,"/cumm               4000 - 11000/cumm")
        print("\n")
        print("Differential Counts")
        print("-------------------")
        print("Neutrophils            :  ",cbc_neutrophils,"%                   40 - 70%")
        print("Lymphocytes            :  ",cbc_lymphocytes,"%                   20 - 40%")
        print("Eosinophils            :  ",cbc_eosinophils,"%                    0 - 5%")
        print("Monocytes              :  ",cbc_monocytes,"%                     0 - 2%")
        print("Basophils              :  ",cbc_basophils,"%                     0-1%")
        if (gender == "male"):
            print("RBC                    :  ",cbc_rbc,"million/cumm        4.5 - 6.0 million/cumm")
        else:
            print("RBC                    :  ",cbc_rbc,"million/cumm               4.0 - 5.5 million/cumm") 
        print("Platelets              :  ",cbc_platelets,"Lakhs/cumm           1.5 - 4.5 Lakhs/cumm")
        print("PCV (Hct)              :  ",cbc_pcv,"%                   40 - 60%")
        print("MCV                    :  ",cbc_mcv," fl                 83 - 101 fl")
        print("MCH                    :  ",cbc_mch," Pg                 27 - 33 Pg")
        print("MCHC                   :  ",cbc_mchc," g/dl               30 - 36 g/dl")
        print("ESR                    :  ",cbc_esr,"mm/hour               < 20 mm/hour")
        print("\n")

        print("Blood Sugar")
        print("------------")
        print("Fasting blood sugar    :  ",fbs2,"mg/dl       70 - 110mg/dl")
        print("Postprandial bloodsugar:  ",ppbs2,"mg/dl       70 - 140mg/dl")
        print("\n")

        print("Lipid Profile")
        print("-------------")
        print("Cholesterol level      : ", cho," mg/dl   130 - 200 mg/dl")
        print("TGL level              : ", chotgl," mg/dl   80  - 200 mg/dl")
        print("LDL level              : ", choldl," mg/dl   Less than 160 mg/dl")
        print("HDL level              : ", chohdl,"  mg/dl   Above 40 mg/dl")
        print("VLDL level             : ", chovldl,"  mg/dl   Below 40 mg/dl")
        print("\n")

        print("Renal Function Test")
        print("--------------------")
        print("Blood Urea level       :  ",rft_blood_urea,"mg/dl       16.6 - 48.5 mg/dl")
        if (gender == "male"):
            print("Blood Creatinine level  :   ",rft_blood_creatinine,"mg/dl       0.7 - 1.2 mg/dl")
            print("Uric Acid level         :   ",rft_uric_acid,"mg/dl       3.7 - 7.0 mg/dl")
        else:
            print("Blood Creatinine level  :   ",rft_blood_creatinine,"mg/dl       0.5 - 0.9 mg/dl")
            print("Uric Acid level         :   ",rft_uric_acid,"mg/dl       2.4 - 5.7 mg/dl")
        print("\n")

        print("Liver function test")
        print("--------------------")
        print("Total Billirubin        :    ", lft_total_billi,"mg/dl      0.2 - 1.0 mg/dl")
        print("Direct Billirubin       :    ", lft_direct_billi,"mg/dl      0.0 - 0.2 mg/dl")
        print("Indirect Billirubin     :    ", lft_indirect_billi,"mg/dl      0.0 - 1.0 mg/dl")
        print("Sgot (ast)              :    ", lft_sgot_ast, "iu/L      05 - 35 iu/L")
        print("Sgpt (alt)              :    ", lft_sgpt_alt, "iu/L      05 - 35 iu/L")
        print("Total protien           :    ", lft_total_protien, "gr/dl      6 - 8 gr/dl")
        print("Albumin                 :    ", lft_albumin, "gr/dl      2.5 - 5.5 gr/dl")
        print("Globulin                :    ", lft_globulin, "gr/dl      1.5 -  3.5 gr/dl")
        print("Alkaline phosphatase    :    ", lft_alkaline_phosphatase, "iu/L     25 - 140 iu/L")
        print("A/g ratio               :    ", lft_ag_ratio_calc )
        print("\n")

        print("Urine Routine")
        print("--------------")
        print("Urine color             :", urinecolor)
        print("Urine appearance        :", urineappearance)
        print("Urine reaction          :", urinereaction)
        print("Urine sugar             :", urinesugar)
        print("Urine protein           :", urineprotein)
        print("Urine pusscells         :", urinepuscell)
        print("Urine RBC               :", urinerbc)
        print("Urine epithelial        :", urineepithelial)
        print("Urine cast              :", urinecast)
        print("Urine crystals          :", urinecrys)
        print("Urine bacteria          :", urinebacteria)
        print("\n")

        print("Blood Pressure")
        print("--------------")
        print("Systolic                :",sys,"mmHg         <120 mmHg")
        print("iastolic                :",dia,"mmHg         <80 mmHg")
        thanks_footer()

else:
    error()
    
    
 



