#Program Ini adalah Program yang digunakan untuk memudahkan anda melakukan Subnetting
#Kelas C = menggunakan prefix 24-30
#Kelas B = menggunakan prefix 16-23
#Kelas A = menggunakan prefix 8-15
#Program ini diselesaikan dengan versi beta pada 10 Oktober 2019 dan disempurnakan hingga 21 Oktober 2019
#Hermawan X-SIJA SMKN 1 Cibinong
import time
def loop():
    ulang = ("Y")
    while ulang=="Y" or ulang=="y":
        print("\n\n"+"="*22,"\n  SUBNETTING MACHINE\n"+"\t by\n"+"hermawansent@gmail.com\n"+"="*22)
        print("1. Subnetting Kelas A\n2. Subnetting Kelas B\n3. Subnetting Kelas C")
        sn_var = input("\nPilih perintah : ")
        #Kelas C
        if sn_var=="3" or sn_var=="c" or sn_var=="C" or sn_var=="kelas c" or sn_var=="KELAS C" or sn_var=="kelas C" or sn_var =="Kelas C":
            def kelas_c():
                while True:
                    try:
                        print("\n"+"="*18,"\nSUBNETTING KELAS C\n"+"="*18)
                        octet_1 = [(input("Masukkan oktet ke-1 : "))]
                        octet_2 = int(input("Masukkan oktet ke-2 : "))
                        octet_3 = int(input("Masukkan oktet ke-3 : "))
                        octet_4 = int(input("Masukkan oktet ke-4 : "))
                        pref = int(input("Masukkan prefix     : "))
                        if (pref<24 or pref>30) or (octet_1>256 or octet_2>256 or octet_3>256 or octet_4>256):
                            try:
                                print("\nIP TIDAK VALID")
                                time.sleep(0.5)
                                print("Mengulangi Program...")
                                time.sleep(1)
                                continue
                            finally:
                                kelas_c()
                                break

                        #Hitung
                        minus = (32-pref)
                        pangkat = (2**minus)
                        print("\nSedang menghitung",end="")
                        time.sleep(0.5)
                        print(".",end="")
                        time.sleep(0.5)
                        print(".",end="")
                        time.sleep(0.5)
                        print(".\n",end="")
                        time.sleep(2)
                        if pangkat > octet_4:
                            print("\nSubnetting dari",str(octet_1)+"."+str(octet_2)+"."+str(octet_3)+"."+str(octet_4)+"/"+str(pref),"adalah : ")
                            octet_4 = 0
                            host = 2**(32-pref)
                            usable_host = (2**(32-pref))-2
                            print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(octet_4), sep = ".")
                            print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(pangkat-1), sep = ".")
                            print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(octet_4+1),sep = ".", end = " - ")
                            print(str(octet_1),str(octet_2),str(octet_3),str(pangkat-2), sep = ".")
                            print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                            print("Host            =",host)
                            print("Availabe Host   =",usable_host)
                        else:
                            print("\nSubnetting dari",str(octet_1)+"."+str(octet_2)+"."+str(octet_3)+"."+str(octet_4)+"/"+str(pref),"adalah : ")
                            if pangkat == 2:
                                net_ip = octet_4//2
                                net2_ip= pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 4:
                                net_ip = octet_4//4
                                net2_ip= pangkat*net_ip 
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 8:
                                net_ip = octet_4//8
                                net2_ip= pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 16:
                                net_ip = octet_4//16
                                net2_ip= pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 32:
                                net_ip = octet_4//32
                                net2_ip = pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                               
                            elif pangkat == 64:
                                net_ip = octet_4//64
                                net2_ip = pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 128:
                                net_ip = octet_4//128
                                net2_ip = pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 256:
                                net_ip = octet_4//256
                                net2_ip = pangkat*net_ip
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip), sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-1), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(net2_ip+1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(octet_3),str(net2_ip+pangkat-2), sep = ".")
                                print("Netmask         = "+"255","255","255",str(256-pangkat),sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                    except ValueError:
                        time.sleep(0.5)
                        print("\nINPUT TIDAK VALID")
                        time.sleep(0.75)
                        print("Mengulangi program...")
                        time.sleep(1)
                        kelas_c()
                        break
                    print("="*28)
                    ulang = input("Ulangi Program? [Y/N] : ")
                    print("="*28)
                    if ulang=="N" or ulang=="n":
                        print("Program diakhiri,",end="")
                        time.sleep(1)
                        print(" Terimakasih telah menggunakan\n",end="")
                        break
                    elif ulang=="y" or ulang=="Y":
                        loop()
                        break
            kelas_c()
                    
        #Kelas B
        elif sn_var=="2" or sn_var=="b" or sn_var=="B" or sn_var=="kelas b" or sn_var=="KELAS B" or sn_var == "Kelas B":
            def kelas_b():
                while True:
                    try:
                        print("\n"+"="*18,"\nSUBNETTING KELAS B\n"+"="*18)
                        octet_1 = int(input("Masukkan oktet ke-1 : "))
                        octet_2 = int(input("Masukkan oktet ke-2 : "))
                        octet_3 = int(input("Masukkan oktet ke-3 : "))
                        octet_4 = int(input("Masukkan oktet ke-4 : "))
                        pref = int(input("Masukkan prefix     : "))
                        if (pref<16 or pref>23)or(octet_1>256 or octet_2>256 or octet_3>256 or octet_4>256):
                            try:
                                print("\nIP TIDAK VALID")
                                time.sleep(0.5)
                                print("\nMengulangi Program...")
                                time.sleep(1)
                                continue
                            finally:
                                kelas_b()
                                break
                        #Hitung
                        minus = (32-(pref+8))
                        pangkat = (2**minus)
                        print("\nSedang menghitung",end="")
                        time.sleep(0.5)
                        print(".",end="")
                        time.sleep(0.5)
                        print(".",end="")
                        time.sleep(0.5)
                        print(".\n",end="")
                        time.sleep(2)
                        if pangkat > octet_3:
                            print("\nSubnetting dari",str(octet_1)+"."+str(octet_2)+"."+str(octet_3)+"."+str(octet_4)+"/"+str(pref),"adalah : ")
                            octet_4 = 255
                            octet_3 = 0
                            bc_var = (pangkat-1)
                            first_var = (octet_3+1)
                            last_var = (octet_4-1)
                            mask_var = (256-pangkat)
                            host = 2**(32-pref)
                            usable_host = (2**(32-pref))-2
                            print("IP Network      = "+str(octet_1),str(octet_2),str(octet_3),"0", sep = ".")
                            print("IP Broadcast    = "+str(octet_1),str(octet_2),str(bc_var),str(octet_4), sep = ".")
                            print("Range IP Client = "+str(octet_1),str(octet_2),str(octet_3),str(first_var),sep = ".", end = " - ")
                            print(str(octet_1),str(octet_2),str(bc_var),str(last_var), sep = ".")
                            print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                            print("Host            =",host)
                            print("Available Host  =",usable_host)
                        else:
                            print("\nSubnetting dari",str(octet_1)+"."+str(octet_2)+"."+str(octet_3)+"."+str(octet_4)+"/"+str(pref),"adalah : ")
                            if pangkat == 2:
                                net_ip = (octet_3//2)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 4:
                                net_ip = (octet_3//4)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 16:
                                net_ip = (octet_3//16)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 32:
                                net_ip = (octet_3//32)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)               
                            elif pangkat == 64:
                                net_ip = (octet_3//64)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 128:
                                net_ip = (octet_3//128)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 256:
                                net_ip = (octet_3//256)
                                net2_ip = (pangkat*net_ip)
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                octet_4 = 255
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(octet_2),str(net2_ip),"0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(octet_2),str(broad),str(octet_4), sep = ".")
                                print("Range IP Client = "+str(octet_1),str(octet_2),str(net2_ip),str(1),sep = ".", end = " - ")
                                print(str(octet_1),str(octet_2),str(broad),str(octet_4 - 1), sep = ".")
                                print("Netmask         = "+"255","255",str(mask_var),"0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                            
                    except ValueError:
                        time.sleep(0.5)
                        print("\nINPUT TIDAK VALID")
                        time.sleep(0.75)
                        print("Mengulangi program...")
                        time.sleep(1)
                        kelas_b()
                        break
                    print("="*28)
                    ulang = input("Ulangi Program? [Y/N] : ")
                    print("="*28)
                    if ulang=="N" or ulang=="n" or ulang=="no" or ulang=="No" or ulang=="NO" or ulang=="nO":
                        print("Program diakhiri,",end="")
                        time.sleep(1)
                        print(" Terimakasih telah menggunakan\n",end="")
                        break
                    elif ulang=="y" or ulang=="Y":
                        loop()
                        break
            kelas_b()
        
        #Kelas A
        elif sn_var=="1" or sn_var=="A" or sn_var=="a" or sn_var=="kelas a" or sn_var=="KELAS A" or sn_var=="Kelas A":
            def kelas_a():
                while True:
                    try:
                        print("\n\n"+"="*18,"\nSUBNETTING KELAS A\n"+"="*18)
                        octet_1 = int(input("Masukkan oktet ke-1 : "))
                        octet_2 = int(input("Masukkan oktet ke-2 : "))
                        octet_3 = int(input("Masukkan oktet ke-3 : "))
                        octet_4 = int(input("Masukkan oktet ke-4 : "))
                        pref = int(input("Masukkan prefix     : "))
                        if (pref<8 or pref>15)or(octet_1>256 or octet_2>256 or octet_3>256 or octet_4>256):
                            try:
                                print("\nIP TIDAK VALID")
                                time.sleep(0.5)
                                print("Mengulangi Program...")
                                time.sleep(1)
                                continue
                            finally:
                                kelas_a()              
                                break  
                        #Hitung
                        minus = (32-(pref+16))
                        pangkat = (2**minus)
                        print("\nSedang menghitung",end="")
                        time.sleep(0.5)
                        print(".",end="")
                        time.sleep(0.5)
                        print(".",end="")
                        time.sleep(0.5)
                        print(".\n",end="")
                        time.sleep(2)
                        if pangkat > octet_2:
                            print("\nSubnetting dari",str(octet_1)+"."+str(octet_2)+"."+str(octet_3)+"."+str(octet_4)+"/"+str(pref),"adalah : ")
                            octet_4 = 255
                            octet_3 = 255
                            bc_var = (pangkat-1)
                            mask_var = (256-pangkat)
                            host = 2**(32-pref)
                            usable_host = (2**(32-pref))-2                            
                            print("IP Network      = "+str(octet_1),"0","0","0", sep = ".")
                            print("IP Broadcast    = "+str(octet_1),str(bc_var),str(octet_3),str(octet_4), sep = ".")
                            print("Range IP Client = "+str(octet_1),"0","0","1",sep = ".", end = " - ")
                            print(str(octet_1),str(bc_var),str(octet_3),str(octet_4-1), sep = ".")
                            print("Netmask         = "+"255",str(mask_var),"0","0",sep=".")
                            print("Host            =",host)
                            print("Availabe Host   =",usable_host)
                        else: 
                            print("\nSubnetting dari",str(octet_1)+"."+str(octet_2)+"."+str(octet_3)+"."+str(octet_4)+"/"+str(pref),"adalah : ")
                            if pangkat == 2:
                                net_ip = octet_2//2
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)
                            elif pangkat == 4:
                                net_ip = octet_2//4
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 8:
                                net_ip = octet_2//8
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                            
                            elif pangkat == 16:
                                net_ip = octet_2//16
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 32:
                                net_ip = octet_2//32
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 64:
                                net_ip = octet_2//64
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 128:
                                net_ip = octet_2//128
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                            elif pangkat == 256:
                                net_ip = octet_2//256
                                net2_ip = pangkat*net_ip
                                broad = (net2_ip+pangkat-1)
                                mask_var = (256-pangkat)
                                host = 2**(32-pref)
                                usable_host = (2**(32-pref))-2                                
                                print("IP Network      = "+str(octet_1),str(net2_ip),"0","0", sep = ".")
                                print("IP Broadcast    = "+str(octet_1),str(broad),"255","255", sep = ".")
                                print("Range IP Client = "+str(octet_1),str(net2_ip),"0","1",sep = ".", end = " - ")
                                print(str(octet_1),str(broad),"255",str(255 - 1), sep = ".")
                                print("Netmask         = "+"255",mask_var,"0","0",sep=".")
                                print("Host            =",host)
                                print("Availabe Host   =",usable_host)                                
                    except ValueError:
                        time.sleep(0.5)
                        print("\nINPUT TIDAK VALID")
                        time.sleep(0.75)
                        print("Mengulangi program...")
                        time.sleep(1)
                        kelas_a()
                        break
                    print("="*28)
                    ulang = input("Ulangi Program? [Y/N] : ")
                    print("="*28)
                    if ulang=="N" or ulang=="n":
                        print("Program diakhiri,",end="")
                        time.sleep(1)
                        print(" Terimakasih telah menggunakan\n",end="")
                        break
                    elif ulang=="y" or ulang=="Y":
                        loop()
                        break
            kelas_a()
        else:
            try:
                print("\nPERINTAH TIDAK VALID")
                time.sleep(0.5)
                print("Mengulangi Program...")
                time.sleep(1)
            finally:
                loop()
                break
        break
loop()