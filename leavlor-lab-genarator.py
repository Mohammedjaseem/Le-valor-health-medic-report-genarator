# code for manoor health

from time import time
from unicodedata import name
from datetime import date

# input section starts here 
name   = input("Enter patient  name       : ")
age    = input("Enter patient age         : ")
gender = input("Enter Gender              : ")
refno  = input("Refred by                 : ")
test   = input("Enter the name of the test: ")
today  = date.today()
test   = test.lower()

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

def thanks_footer():
        print("------------------------------------------------------------")
        footer = """


                   
Lab Technician                                        Lab Incharge





    
                    Thanks for choosing Le'valor Health
                           www.levalorhealth.com"""
        print("\n")
        print("\n")
        print(footer)

#test choosing start here
if (test == "cho"):
    # test number 1 ( Lipid test)
    print("\n")
    print("You choosed Cholesterol test ")
    cho     = input("Enter cho level : ")
    chotgl  = input("Enter TGL level :  ")
    choldl  = input("Enter LDL level : ")
    chohdl  = input("Enter HDL level : ")
    chovldl = input("Enter VLDL level: ")
    print("\n")

    print("Cholesterol test")
    print("Cholesterol level:", cho)
    print("TGL level        :", chotgl)
    print("LDL level        :", choldl)
    print("HDL level        :", chohdl)
    print("VLDL level       :", chovldl)
    thanks_footer()

elif (test == "urine"):
    # test number 2 (Urine test)
    print("\n")
    print("You choosed Urine test")
    urineprotein    = input("Enter protein level         : ")
    urinesugar      = input("Enter sugar level           : ")
    urineketone     = input("Enter ketone level          : ")
    urinebilirubin  = input("Enter bilirubin level       : ")
    urinecolor      = input("Enter urine color           : ")
    urineappearance = input("Enter urine appearance      : ")
    urinereactio    = input("Enter urine reaction        : ")
    urinerbc        = input("Enter urine RBC level       : ")
    urinepuscell    = input("Enter urine puscells level  : ")
    urineepithelial = input("Enter urine epithelial level: ")
    urinebacteria   = input("Enter urine bacteria level  : ")
    urineyeast      = input("Enter urine yeast level     : ")
    urinecast       = input("Enter urine cast level      : ")
    urinecrys       = input("Enter urine crystals level  : ")

    genral_det()
    print("Urine test")
    print("Protein level   :", urineprotein)
    print("Sugar level     :", urinesugar)
    print("Ketone level    :", urineketone)
    print("Bilirubin level :", urinebilirubin)
    print("Urine color     :", urinecolor)
    print("Urine appearance:", urineappearance)
    print("Urine reaction  :", urinereactio)
    print("RBC level       :", urinerbc)
    print("Pus cells level :", urinepuscell)
    print("Epithelial level:", urineepithelial)
    print("Bacteria level  :", urinebacteria)
    print("Yeast level     :", urineyeast)
    print("Cast level      :", urinecast)
    print("Crystals level  :", urinecrys)
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

elif (test == "RFT"):
    # test number 4 (RFT test)
    print("\n")
    print("You choosed RFT test")
    rft_total_billi          = input("Enter total RFT Billirubin    : ")
    rft_direct_billi         = input("Enter direct RFT Billirubin   : ")
    rft_indirect_billi       = input("Enter indirect RFT Billirubin : ")
    rft_sgot_ast             = input("Enter Sgot ast                : ")
    rft_sgot_alt             = input("Enter Sgot alt                : ")
    rft_total_protien        = input("Enter total RFT protien       : ")
    rft_albumin              = input("Enter RFT albumin             : ")
    rft_globulin             = input("Enter RFT globulin            : ")
    rft_ag_ratio             = input("Enter RFT ag ratio            : ")
    rft_alkaline_phosphatase = input("Enter RFT alkaline phosphatase: ")
    print("\n")
    
    print("RFT test")
    print("Total RFT Billirubin    :", rft_total_billi)
    print("Direct RFT Billirubin   :", rft_direct_billi)
    print("Indirect RFT Billirubin :", rft_indirect_billi)
    print("Sgot ast                :", rft_sgot_ast)
    print("Sgot alt                :", rft_sgot_alt)
    print("Total RFT protien       :", rft_total_protien)
    print("RFT albumin             :", rft_albumin)
    print("RFT globulin            :", rft_globulin)
    print("RFT ag ratio            :", rft_ag_ratio)
    print("RFT alkaline phosphatase:", rft_alkaline_phosphatase)
    thanks_footer()

else:
    print("\n")
    print("You choosed wrong test ")
    thanks_footer()
 



