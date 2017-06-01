#! /usr/bin/env python
# -*- coding: Utf-8 -*-

##############################################################################
# magoltch lik n9ol fl examen mais had tool ghir bach tkhtaser lwa9t o safé  #
# ila 3andek chi fikra wla chi blan o bghitini n3awnek marhba				 #
# email : jiibl3azz@gmail.com			   				     				 #							
# bonne courage																 #
##############################################################################

from math import pow, ceil, log
from sys import argv
import re
import sys
import os
import base64

oxy4hy4 = '''Q3JlYXRlZCBieSA6IA=='''
oxy4hy4_ = """QmVuWWFoWWEg"""
oxy4hy4_4 = """R29vZCBMdWNrIA=="""
oxy4hy4_3 = "SVNUQSBSTg0K"

class dirbi:
    RCA = '\033[1;32m'
    WAC  = '\033[1;31m'


if argv[1] == "-h" or argv[1] == "--help" :
    print (dirbi.RCA)
    print  "Usage: "+ argv[0] +" ip_address/mask host1 host2 host3 ....."
    print  "exemple: "+ argv[0] +" 192.168.10.0/23 10 5 240 26 "
    print  "Put the names of the biggest ones at least: Site1R3,Site1R1,Site1R2,Site1R0 "
    print base64.b64decode(oxy4hy4) + '\033[31m' + base64.b64decode(oxy4hy4_) + '\033[1;37m' +base64.b64decode(oxy4hy4_3)
    print
    exit(0)



chi_7aja = re.match("^(?:(?:(?:2[0-5][0-5]|1\d{2}|\d{2}|\d)\.){3}(?:[12]\d{2}|\d{2}|\d)\/(?:3[0-2]|[1-2]\d|\d))\
(?:\ \d*)+$", " ".join(argv[1:]))

(HM_Jiib_l3azz, cidr_String_machi_d_dariyat) = sys.argv[1].split('/')
if chi_7aja == None:
    

    addr_ISTA_RN = HM_Jiib_l3azz.split('.')
    cidr_87_139 = int(cidr_String_machi_d_dariyat)

    mask_machi_d_anonymous = [0, 0, 0, 0]
    for i in range(cidr_87_139):
        mask_machi_d_anonymous[i/8] = mask_machi_d_anonymous[i/8] + (1 << (7 - i % 8))

    net = []
    for i in range(4):
        net.append(int(addr_ISTA_RN[i]) & mask_machi_d_anonymous[i])

    broad = list(net)
    brange = 32 - cidr_87_139
    for i in range(brange):
        broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))
        subnet_mask = ".".join(map(str, mask_machi_d_anonymous))
        mask_octet_decimal=subnet_mask.split(".")
        wildcard_octet=[]
        for w_octet in mask_octet_decimal:
          wild_octet=255-int(w_octet)
          wildcard_octet.append(str(wild_octet))    




    print '\033[1;33m'+"\n\t\t\t\aCIDR Calculator"
    print "\t\t\t\a" + base64.b64decode(oxy4hy4) + base64.b64decode(oxy4hy4_) + '\n\t\t\t\a     ' + base64.b64decode(oxy4hy4_4)
    print dirbi.RCA + "Subnet\t\t\t\a:   " , HM_Jiib_l3azz
    print "Subnet mask\t\t\a:   " , ".".join(map(str, mask_machi_d_anonymous))
    print "Network\t\t\t:   " , ".".join(map(str, net))
    print "Broadcast\t\t: "  ,   ".".join(map(str, broad))
    print "Wildcard\t\t: "  ,   ".".join(wildcard_octet)
    exit(0)



khoutna = raw_input("Mettre les noms des plus grands à moins : ")
benyo = khoutna.split(",") 


rassl7maar = """
		<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
		<HTML>
		<HEAD>
    <META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=utf-8">
    <TITLE></TITLE>
    <META NAME="GENERATOR" CONTENT="LibreOffice 4.1.6.2 (Linux)">
    <META NAME="CREATED" CONTENT="20170520;221637000000000">
    <META NAME="CHANGED" CONTENT="20170520;224145000000000">
    <STYLE TYPE="text/css">
    <!--
        @page { size: 8.5in 11in; margin: 0.79in }
        P { margin-bottom: 0.1in; direction: ltr; color: #00000a; line-height: 120%; text-align: left; widows: 2; orphans: 2 }
        P.kan9ra_f_darna { font-family: "Liberation Serif", serif; font-size: 12pt; so-language: en-US }
        P.cjk { font-family: "Noto Sans CJK SC Regular"; font-size: 12pt; so-language: zh-CN }
        P.ctl { font-family: "FreeSans"; font-size: 12pt; so-language: hi-IN }
        TD P { margin-bottom: 0in; direction: ltr; color: #00000a; text-align: left; widows: 2; orphans: 2 }
        TD P.kan9ra_f_darna { font-family: "Liberation Serif", serif; font-size: 12pt; so-language: en-US }
        TD P.cjk { font-family: "Noto Sans CJK SC Regular"; font-size: 12pt; so-language: zh-CN }
        TD P.ctl { font-family: "FreeSans"; font-size: 12pt; so-language: hi-IN }
 	   -->
 	   </STYLE>
		</HEAD>
		<BODY LANG="en-US" TEXT="#00000a" DIR="LTR">
		<TABLE WIDTH=665 CELLPADDING=3 CELLSPACING=0 STYLE="page-break-before: always">
    	<COL WIDTH=88>
   		 <COL WIDTH=89>
   		 <COL WIDTH=89>
  		  <COL WIDTH=89>
  			  <COL WIDTH=89>
  	 	 <COL WIDTH=183>
   			 <TR VALIGN=TOP>
       	 <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Network</P>
       	 </TD>
      	  <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Subnet</P>
      	  </TD>
     	   <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Subnet mask 
            </P>
       	 </TD>
       	 <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
      	      <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Broadcast</P>
       	 </TD>
       	 <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>First address</P>
      	  </TD>
      	  <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
      	      <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Last address hôte</P>
      	  </TD>
      	  <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
      	      <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Number of hosts</P>
          </TD>
          <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>préfixe</P>
          </TD>
          <TD WIDTH=89 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>Masque Générique</P>
          </TD>
    		</TR>
"""




class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() 
    def flush(self) :
        for f in self.files:
            f.flush()




def ch7al(x): 
    z = log(x, 2)  
    if int(z) != z:  
        z = ceil(z)  
    return int(z)  #  2 -=> "x"


def jiiblmask(cidr_87_139):  # ex. 24 -> 255.255.255.0
    karousa_dyal_programing = [0 for i in range(4)]  # creating list of four 0s
    y = int(cidr_87_139 / 8)  # ch7al dyal octets mn 255
    if y > 0:  # ida kan l mask < 8
        for z in range(y):
            karousa_dyal_programing[z] = 255
        karousa_dyal_programing[z + 1] = int(256 - pow(2, 8 - (cidr_87_139 - 8 * y)))
    else:
        karousa_dyal_programing[0] = 256 - pow(2, 8 - cidr_87_139)
    return karousa_dyal_programing


def jib_net(ip_lmard, nmask):  # tjiib network address mn l ip o l mask
    net = [0 for i in range(4)]
    for i in range(4):
        net[i] = int(ip_lmard[i]) & int(nmask[i])  # octet o l  mask
    return net


def awel_adresse(ip_lmard):  # awel adress mn l ip , mask
    addr_ISTA_RN = ip_lmard[:] 
    addr_ISTA_RN[3] = int(addr_ISTA_RN[3]) + 1
    return addr_ISTA_RN


def akhir_adresse(ip_lmard, nmask):  # akhir adress mn l ip , mask
    addr_ISTA_RN = lbaraaaa7(ip_lmard, nmask)
    addr_ISTA_RN[3] -= 1
    return addr_ISTA_RN


def lbaraaaa7(ip_lmard, nmask):  # broadcast adress mn l ip , mask
    net = [0 for i in range(4)]
    for i in range(4):
        net[i] = int(ip_lmard[i]) | 255 - int(nmask[i])  # octet , wildcard mask
    return net


def getnextaddr(ip_lmard, nmask):
    ip_lmard = lbaraaaa7(ip_lmard, nmask)
    for i in range(4):
        if ip_lmard[3 - i] == 255:
            ip_lmard[3 - i] = 0
            if ip_lmard[3 - i - 1] != 255:
                ip_lmard[3 - i - 1] += 1
                break
        else:
            ip_lmard[3 - i] += 1
            break
    return ip_lmard


def norm(ip_lmard):
    addr_ISTA_RN = ip_lmard[:]
    for i in range(len(addr_ISTA_RN)):
        addr_ISTA_RN[i] = str(addr_ISTA_RN[i])
    return ".".join(addr_ISTA_RN)

aala5atrek=raw_input('Appear in a file? Yes (Y) or No (n) : ')

if aala5atrek == "y" or aala5atrek == "Y":
  b3ny4hy4 =raw_input('Filename : ')
  ofppt_0 = open(b3ny4hy4 , 'w')
  ofppt_0.write(rassl7maar)

print '\033[1;33m'+"\n\t\t\t\aVLSM Calculator"
print "\t\t\t\a" + base64.b64decode(oxy4hy4) + base64.b64decode(oxy4hy4_) + '\n\t\t\t\a     ' + base64.b64decode(oxy4hy4_4)


def vlso(ip_lmard, hosts):
    global ch7al_khaaaas, allc
    bits = 0

    for x in range(len(hosts)):
        bits = ch7al(hosts[x] + 2)
        ip_lmard = jib_net(ip_lmard, jiiblmask(int(32 - bits)))
        subnet_mask = norm(jiiblmask(int(32 - bits)))
        mask_octet_decimal=subnet_mask.split(".")
        wildcard_octet=[]
        for w_octet in mask_octet_decimal:
          wild_octet=255-int(w_octet)
          wildcard_octet.append(str(wild_octet))
          wildcard_mask=".".join(wildcard_octet)


        viva_rca = """
    <TR VALIGN=TOP>
        <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%s</P>
        </TD>
        <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%15s</P>
        </TD>
        <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%15s</P>
        </TD>
        <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%15s</P>
        </TD>
        <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%15s</P>
        </TD>
        <TD WIDTH=88 BGCOLOR="#ffffff" STYLE="border-top: 1px solid #000001; border-bottom: 1px solid #000001; border-left: 1px solid #000001; border-right: none; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%-15s</P>
        </TD>
        <TD WIDTH=183 BGCOLOR="#ffffff" STYLE="border: 1px solid #000001; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0.04in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%4d</P>
            </P>
        </TD>
        <TD WIDTH=183 BGCOLOR="#ffffff" STYLE="border: 1px solid #000001; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0.04in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>/%d</P>
            </P>
        </TD>
        <TD WIDTH=183 BGCOLOR="#ffffff" STYLE="border: 1px solid #000001; padding-top: 0.04in; padding-bottom: 0.04in; padding-left: 0.03in; padding-right: 0.04in">
            <P CLASS="kan9ra_f_darna" ALIGN=CENTER>%s</P>
            </P>
        </TD>
    </TR>
                  """ % \
              (benyo[x],
               norm(ip_lmard),
               norm(jiiblmask(int(32 - bits))),
               norm(lbaraaaa7(ip_lmard, jiiblmask(int(32 - bits)))),
               norm(awel_adresse(ip_lmard)),
               norm(akhir_adresse(ip_lmard, jiiblmask(int(32 - bits)))),
               int(pow(2, bits)) - 2,
               32 - bits,
               wildcard_mask)
        


        print(dirbi.RCA + """ 
 Network\t\t\a:\t""" + dirbi.WAC + """  %s""" + dirbi.RCA + """
 Subnet\t\t\t:""" + dirbi.WAC + """\t %15s""" + dirbi.RCA + """
 Subnet mask\t\t: """ + dirbi.WAC +  """\t  %15s""" + dirbi.RCA + """
 Broadcast\t\t:""" + dirbi.WAC + """\t %15s""" + dirbi.RCA + """
 First address\t\t:""" + dirbi.WAC + """\t %15s""" + dirbi.RCA + """
 Last address\t\t:""" + dirbi.WAC + """\t  %-15s""" + dirbi.RCA + """
 Number of hosts\t:""" + dirbi.WAC + """\t%4d""" + dirbi.RCA + """
 Slash\t\t\t:""" + dirbi.WAC + """\t  /%d""" + dirbi.RCA + """
 Wildcard\t\t:""" + dirbi.WAC + """\t  /%s""" + dirbi.RCA + """
                  """) % \
              (benyo[x],
               norm(ip_lmard),
               norm(jiiblmask(int(32 - bits))),
               norm(lbaraaaa7(ip_lmard, jiiblmask(int(32 - bits)))),
               norm(awel_adresse(ip_lmard)),
               norm(akhir_adresse(ip_lmard, jiiblmask(int(32 - bits)))),
               int(pow(2, bits)) - 2,
               32 - bits,
               wildcard_mask)



        ch7al_khaaaas += hosts[x]
        allc += int(pow(2, bits)) - 2
        ip_lmard = getnextaddr(ip_lmard, jiiblmask(int(32 - bits)))


	if aala5atrek == "y" or aala5atrek == "Y":
  		ofppt_0.write(viva_rca)




ip = argv[1].split("/")[0].split(".")   # 192.168.1.0/24 2 8 22 54  ->  ['192','168','1','0']
cidr_87_139 = int(argv[1].split("/")[1])       # 192.168.1.0/24 2 8 22 54  -> str 24
arg = [0 for i in range(len(argv[2:]))] #                2 8 22 54  -> ['2','8','22','54']
mask_machi_d_anonymous = jiiblmask(cidr_87_139)                    #                       24  -> list of int [255,255,255,0]
total_la7asa_capa = 0

for x in range(len(ip)):  # list of str ['192','168','1','0'] ->
    ip[x] = int(ip[x])  # x machi dyal dakchi x dyal intgers(ar9aaam) f  [192,168,1,0]

for x in range(len(argv[2:])):  # list of str ['2','8','22','54'] ->
    arg[x] = int(argv[x + 2])  # list of int [2,8,22,54]

for x in range(len(argv[2:])):
    total_la7asa_capa += int(argv[2:][x])

if total_la7asa_capa > (pow(2, 32 - cidr_87_139) - 2):
    exit("ERROR: Too many hosts")

arg = sorted(arg, reverse=True)  #  [2,8,22,54] -> [54,22,8,1]

ch7al_khaaaas = 0
allc = 0





vlso(jib_net(ip, mask_machi_d_anonymous), arg)

