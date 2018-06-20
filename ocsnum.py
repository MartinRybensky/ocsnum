#!/usr/bin/python
# -*- coding: utf-8 -*-


# license Creative Commons BY-NC-SA 3.0
# Created by Martin Rybensky

__version__ = '1.0'
__author__ = 'Martin Rybensky'

import os
import sys

user_input = 0
vystup = ''




def radjednotek(vstup):
        # pokud je ve vloženém čísle v řádu jednotek nula, vrací false
        if int(str(vstup)[-1]) == 0:
                return False
        else:
                return True


def raddesitek(vstup):
        # pokud je ve vloženém čísle v řádu desítek nula, vrací false  
        try:
		if int(str(vstup)[-2]) != 0:
                	return True
		else: 
			return False
        except:
                return False


def radstovek(vstup):
        # pokud je ve vloženém čísle v řádu stovek nula, vrací false           
        if int(str(vstup)[-3]) == 0:
                return False
        else:
                return True

def radtisicu(vstup):
        # pokud je ve vloženém čísle v řádu tisíců nula, vrací false           
        if int(str(vstup)[-4]) == 0:
                return False
        else:
                return True

def raddesetitisicu(vstup):
        # pokud je ve vloženém čísle v řádu tisíců nula, vrací false           
        if int(str(vstup)[-5]) == 0:
                return False
        else:
                return True

def radstatisicu(vstup):
        # pokud je ve vloženém čísle v řádu tisíců nula, vrací false           
        if int(str(vstup)[-6]) == 0:
                return False
        else:
                return True

def radmilionu(vstup):
        # pokud je ve vloženém čísle v řádu tisíců nula, vrací false           
        if int(str(vstup)[-7]) == 0:
                return False
        else:
                return True

def raddesetimilionu(vstup):
        # pokud je ve vloženém čísle v řádu tisíců nula, vrací false           
        if int(str(vstup)[-8]) == 0:
                return False
        else:
                return True

def radstamilionu(vstup):
        # pokud je ve vloženém čísle v řádu tisíců nula, vrací false           
        if int(str(vstup)[-9]) == 0:
                return False
        else:
                return True

def jednotka_na_slovo(vstup): 
	
	vystup = ''

	if vstup == 1:
		vystup = 'ѥдинъ'
	elif vstup == 2:
		vystup = 'дъва'
	elif vstup == 3:
		vystup = 'трьѥ'
	elif vstup == 4:
		vystup = 'четꙑре'
	elif vstup == 5:
		vystup = 'пѧть'
	elif vstup == 6:
		vystup = 'шесть'
	elif vstup == 7:
		vystup = 'седмь'
	elif vstup == 8:
		vystup = 'осмь'
	elif vstup == 9:
		vystup = 'девѧть'
	elif vstup == 10:
		vystup = 'десѧть'
		
	return vystup


def cislo_na_slovo(vstup):
	
	slovnivyjadreni = ''

	if vstup <= 10:
		slovnivyjadreni = jednotka_na_slovo(vstup)			
	elif vstup < 100:	
		slovnivyjadreni = desitka_na_slovo(vstup)
	elif vstup < 1000:
		slovnivyjadreni = stovka_na_slovo(vstup)
	elif vstup < 10000:
		slovnivyjadreni = tisicovka_na_slovo(vstup)
	else:
		slovnivyjadreni = "тьма"
	return slovnivyjadreni


def desitka_na_slovo(vstup):
	i = " и "

	c10 = " на десѧте"
	c20 = "дъва десѧти"
	c30 = "трьѥ десѧте"
	c40 = "четꙑре десѧте"
	c50 = "пѧть десѧтъ"
	c60 = "шесть десѧтъ"
	c70 = "седмь десѧтъ"
	c80 = "осмь десѧтъ"
	c90 = "девѧть десѧтъ"

	slovnivyjadreni = ""
	jednotka = int(str(vstup)[-1:])


	if vstup <= 10:
		slovnivyjadreni = jednotka_na_slovo(vstup)
		
	elif vstup < 20:
		slovnivyjadreni = jednotka_na_slovo(jednotka)+c10
				
	elif vstup < 30:
		if vstup == 20:
			slovnivyjadreni = c20
		else:
			slovnivyjadreni = c20+i+jednotka_na_slovo(jednotka)
					
	elif vstup < 40:
		if vstup == 30:
			slovnivyjadreni = c30
		else:		
			slovnivyjadreni = c30+i+jednotka_na_slovo(jednotka)		
					
	elif vstup < 50:
		if vstup == 40:
			slovnivyjadreni = c40
		else:
			slovnivyjadreni = c40+i+jednotka_na_slovo(jednotka)
				
	elif vstup < 60:
		if vstup == 50:
			slovnivyjadreni = c50
		else:		
			slovnivyjadreni = c50+i+jednotka_na_slovo(jednotka)
				
	elif vstup < 70:
		if vstup == 60:
			slovnivyjadreni = c60
		else:		
			slovnivyjadreni = c60+i+jednotka_na_slovo(jednotka)				
	elif vstup < 80:
		if vstup == 70:
			slovnivyjadreni = c70
		else:		
			slovnivyjadreni = c70+i+jednotka_na_slovo(jednotka)
		
	elif vstup < 90:
		if vstup == 80:
			slovnivyjadreni = c80
		else:
			slovnivyjadreni = c80+i+jednotka_na_slovo(jednotka)
					
	elif vstup < 100:
		if vstup == 90:
			slovnivyjadreni = c90
		else:
			slovnivyjadreni = c90+i+jednotka_na_slovo(jednotka)	

	
	return slovnivyjadreni


def stovka_na_slovo(vstup):
	slovnivyjadreni = ''	
	try:
		stovka = int(str(vstup)[-3])
	except:
		stovka = 0
	try:
		desitka = int(str(vstup)[-2:])
	except:
		desitka = int(str(vstup)[-1:])

	tecka = " • "

		
	if raddesitek(vstup) == False and radjednotek(vstup) == False:
		i = ""
	elif desitka < 20:
		i = " и "
	elif raddesitek(vstup) == False:
		i = " и "
	elif radjednotek(vstup) == False:
		i = " и "
	else:
		i = tecka
	


	if stovka == 1:
		slovnivyjadreni = "съто"+i+desitka_na_slovo(desitka)
	elif stovka == 2:
		slovnivyjadreni = "дъвѣ сътѣ"+i+desitka_na_slovo(desitka)
	elif stovka == 3:
		slovnivyjadreni = "три съта"+i+desitka_na_slovo(desitka)
	elif stovka == 4:
		slovnivyjadreni = "четꙑри съта"+i+desitka_na_slovo(desitka)	
	elif stovka >= 5:
		slovnivyjadreni = jednotka_na_slovo(stovka)+" сътъ"+i+desitka_na_slovo(desitka)
	else:
		if desitka > 0:
			slovnivyjadreni = desitka_na_slovo(desitka)
		else:
			slovnivyjadreni = ''
	
	
	return slovnivyjadreni



def tisicovka_na_slovo(vstup):
	slovnivyjadreni = ''
        tisicovka = int(str(vstup)[-4])
        stovka = int(str(vstup)[-3:])
        desitka = int(str(vstup)[-2:])

	tecka = " • "
	'''
	print 'debug'
	print 'tisicovka: '+str(tisicovka)
	print 'stovka: '+str(stovka)
	print 'desitka: '+str(desitka)
	'''

        # 1000
        if radstovek(vstup) == False and raddesitek(vstup) == False and radjednotek(vstup) == False:
                i = ""
        # 1030
        elif radstovek(vstup) == False and raddesitek(vstup) and radjednotek(vstup) == False:
                i = " и "
        # 1100
        elif radstovek(vstup) and raddesitek(vstup) == False and radjednotek(vstup) == False :
                i = " и "
        # 1001
        elif radstovek(vstup) == False and raddesitek(vstup) == False and radjednotek(vstup):
                i = " и "
        # 1016 
        elif radstovek(vstup) == False and raddesitek(vstup) and radjednotek(vstup) and desitka < 20:
                i = " и "
        else: 
                i = tecka
       

	if tisicovka == 1:
  		slovnivyjadreni = "тꙑсѫщи"+i+stovka_na_slovo(stovka)
        elif tisicovka == 2:
              	slovnivyjadreni = "дъвѣ тꙑсѫщи"+i+stovka_na_slovo(stovka)
        elif tisicovka == 3:
              	slovnivyjadreni = "три тꙑсѫщѧ"+i+stovka_na_slovo(stovka)
        elif tisicovka == 4:
              	slovnivyjadreni = "четꙑри тꙑсѫщѧ"+i+stovka_na_slovo(stovka)
        elif tisicovka <= 9:
		slovnivyjadreni = jednotka_na_slovo(tisicovka)+" тꙑсѫщь"+i+stovka_na_slovo(stovka)
                
        return slovnivyjadreni





def prevodcisla(vstup,pismo):
	
	stscislovka = ""

	if pismo == "hlaholice":
                jednotka = jednotka_na_hlah(int(str(vstup)[-1]))
                desitka = desitka_na_hlah(vstup)
                stovka = stovka_na_hlah(vstup)
     


	elif pismo == "cyrilice":
		jednotka = jednotka_na_cyr(int(str(vstup)[-1]))
		desitka = desitka_na_cyr(vstup)
		#stovka = stovka_na_cyr(vstup)			

	'''
		ROZSAH 1 - 99

	'''
        # pokud je zadané číslo menší nebo rovno 10
        if vstup <= 10:
                if pismo == "hlaholice":
                        jednotka = jednotka_na_hlah(vstup)
                elif pismo == "cyrilice":
                        jednotka = jednotka_na_cyr(vstup)
                
                stscislovka = jednotka

        # pokud je zadané číslo větší než 10 a zároveň menší než 20    
        elif vstup < 20:
                if pismo == "hlaholice":
                        jednotka = jednotka_na_hlah(int(str(vstup)[-1]))
                        desitka = "ⰹ" # rovnou se doplní 10                    
                elif pismo == "cyrilice":
                        jednotka = jednotka_na_cyr(int(str(vstup)[-1]))
                        desitka = "і"; # rovnou se doplní 10
                
                stscislovka = jednotka+desitka

        # pokud je zadané číslo větší nebo rovno 20 a zároveň menší než 100
        elif vstup < 100:
                if pismo == "hlaholice":
                        desitka = desitka_na_hlah(vstup) # písmenko odpovídajícím desítce je nutno nejprve zjistit funkcí
                        jednotka = jednotka_na_hlah(int(str(vstup)[-1]))
                elif pismo == "cyrilice":
                        desitka = desitka_na_cyr(vstup) # písmenko odpovídajícím desítce je nutno nejprve zjistit funkcí
                        jednotka = jednotka_na_cyr(int(str(vstup)[-1]))
                
                # pokud je v řádu jednotek nula
                if radjednotek(vstup) == False:
                        stscislovka = desitka

                # pokud není   
                else:
                        stscislovka = desitka+jednotka
                
	# pokud je zadané číslo větší nebo rovno 100 a zároveň menší než 1000	
	elif vstup < 1000:
		if pismo == "hlaholice":
			jednotka = jednotka_na_hlah(int(str(vstup)[-1]))
			desitka = desitka_na_hlah(vstup)
			stovka = stovka_na_hlah(vstup)
		elif pismo == "cyrilice":
			jednotka = jednotka_na_cyr(int(str(vstup)[-1]))
			desitka = desitka_na_cyr(vstup)
			stovka = stovka_na_cyr(vstup)															
				
		if int(str(vstup)[-2]) == 1:  # pokud je v řádu desítek 1 (u -náct je jiný systém než u následujících desítek)
				
			if pismo == "hlaholice":
				desitka = "ⰹ" # rovnou se doplní 10
			elif pismo == "cyrilice":
				desitka == "і" # rovnou se doplní 10
		
			stscislovka = stovka+jednotka+desitka
					
		else: # všechny ostatní desítky
			
			stscislovka = stovka+desitka+jednotka

	elif vstup < 10000:
		carka = "҂"

                if pismo == "hlaholice":
                        jednotka = jednotka_na_hlah(int(str(vstup)[-1]))
                        desitka = desitka_na_hlah(vstup)
                        stovka = stovka_na_hlah(vstup)
                        # hack kvůli tisícům v hlaholici, protože mají vyhrazený vlastní znak
                        if(int(str(vstup)[-4])) == 1:
                                tisicovka = "ⱍ"
                                carka = ""
                        elif(int(str(vstup)[-4])) == 2:
                                tisicovka = "ⱎ"
                                carka = ""
                        elif(int(str(vstup)[-4])) == 3:
                                tisicovka = "ⱏ"
                                carka = ""
                        elif(int(str(vstup)[-4])) == 4:
                                tisicovka = "ⱑ"
                                carka = ""
                        elif(int(str(vstup)[-4])) == 5:
                                tisicovka = "ⱓ"
                                carka = ""
                        else:
                                tisicovka = jednotka_na_hlah(int(str(vstup)[-4]))
                        
                elif pismo == "cyrilice":
                        jednotka = jednotka_na_cyr(int(str(vstup)[-1]))
                        desitka = desitka_na_cyr(vstup)
                        stovka = stovka_na_cyr(vstup)
                        tisicovka = jednotka_na_cyr(int(str(vstup)[-4]))
                
		if int(str(vstup)[-2]) == 1:  # pokud je v řádu desítek 1 (u -náct je jiný systém než u následujících desítek)

        		if pismo == "hlaholice":
                		desitka = "ⰹ" # rovnou se doplní 10
                	elif pismo == "cyrilice":
                		desitka = "і" # rovnou se doplní 10
                                        

                	stscislovka = carka+tisicovka+stovka+jednotka+desitka

		else: # u všech ostatních desítek normálně  

			stscislovka = carka+tisicovka+stovka+desitka+jednotka
                
                                                                                                                                                       

	return stscislovka

def jednotka_na_cyr(vstup): 
	radjednotek = vstup
	jednotka = ""

	if radjednotek == 1:
		jednotka = "а"
	elif radjednotek == 2:
		jednotka = "в"
        elif radjednotek == 3:
                jednotka = "г"
        elif radjednotek == 4:
                jednotka = "д"
        elif radjednotek == 5:
                jednotka = "е"
        elif radjednotek == 6:
                jednotka = "ѕ"
        elif radjednotek == 7:
                jednotka = "з"
        elif radjednotek == 8:
                jednotka = "и"
        elif radjednotek == 9:
                jednotka = "ѳ"

        return jednotka


def desitka_na_cyr(vstup):

	desitka = ""
	try:
		raddesitek = int(str(vstup)[-2])
	except:	
		raddesitek = 0


        if raddesitek == 1:
        	desitka = "і"
        elif raddesitek == 2:
        	desitka = "к"
        elif raddesitek == 3:
                desitka = "л"
        elif raddesitek == 4:
                desitka = "м"
        elif raddesitek == 5:
                desitka = "н"
        elif raddesitek == 6:
                desitka = "ѯ"
        elif raddesitek == 7:
                desitka = "о"
        elif raddesitek == 8:
                desitka = "п"
        elif raddesitek == 9:
                desitka = "ч"

	return desitka

def stovka_na_cyr(vstup):

	stovka = ""
	try:
		radstovek = int(str(vstup)[-3])
	except:
		radstovek = 0
		

	if radstovek == 1:
		stovka = "р"
	elif radstovek == 2:
		stovka = "с"
        elif radstovek == 3:
                stovka = "т"
        elif radstovek == 4:
                stovka = "ѹ"
        elif radstovek == 5:
                stovka = "ф"
        elif radstovek == 6:
                stovka = "х"
        elif radstovek == 7:
                stovka = "ѱ"
        elif radstovek == 8:
                stovka = "ѡ"
        elif radstovek == 9:
                stovka = "ц"


	return stovka
def jednotka_na_hlah(vstup):
        radjednotek = vstup
        jednotka = ""

        if radjednotek == 1:
                jednotka = "ⰰ"
        elif radjednotek == 2:
                jednotka = "ⰱ"
        elif radjednotek == 3:
                jednotka = "ⰲ"
        elif radjednotek == 4:
                jednotka = "ⰳ"
        elif radjednotek == 5:
                jednotka = "ⰴ"
        elif radjednotek == 6:
                jednotka = "ⰵ"
        elif radjednotek == 7:
                jednotka = "ⰶ"
        elif radjednotek == 8:
                jednotka = "ⰷ"
        elif radjednotek == 9:
                jednotka = "ⰸ"

        return jednotka


def desitka_na_hlah(vstup):

        desitka = ""
        try:
                raddesitek = int(str(vstup)[-2])
        except:
                raddesitek = 0


        if raddesitek == 1:
                desitka = "ⰹ"
        elif raddesitek == 2:
                desitka = "ⰻ"
        elif raddesitek == 3:
                desitka = "ⰼ"
        elif raddesitek == 4:
                desitka = "ⰽ"
        elif raddesitek == 5:
                desitka = "ⰾ"
        elif raddesitek == 6:
                desitka = "ⰿ"
        elif raddesitek == 7:
                desitka = "ⱀ"
        elif raddesitek == 8:
                desitka = "ⱁ"
        elif raddesitek == 9:
                desitka = "ⱂ"

        return desitka

def stovka_na_hlah(vstup):

        stovka = ""
        try:
                radstovek = int(str(vstup)[-3])
        except:
                radstovek = 0


        if radstovek == 1:
                stovka = "ⱃ"
        elif radstovek == 2:
                stovka = "ⱄ"
        elif radstovek == 3:
                stovka = "ⱅ"
        elif radstovek == 4:
                stovka = "ⱆ"
        elif radstovek == 5:
                stovka = "ⱇ"
        elif radstovek == 6:
                stovka = "ⱈ"
        elif radstovek == 7:
                stovka = "ⱉ"
        elif radstovek == 8:
                stovka = "ⱋ"
        elif radstovek == 9:
                stovka = "ⱌ"

	return stovka



napoveda = "\n  Old Church Slavonic Numerals’ Converter\n\n  ocsnum 1.0 (C) Martin Rybensky 2018, CC BY-NC-SA\n\n  Usage: ocsnum [parameters] [number]\n\n  -c, --cyrillic     show only cyrillic numeral as output\n  -g, --glagolitic   show only glagolitic numeral as output\n  -s, --slavonic     show only verbally expressed numeral in OCS\n  -h, --help	     show this help\n\n  Better, bidirectional OCS numeral converter can be found here:\n  http://prevodnik.gorazd.org:8081/old-church-slavonic-numerals-converter-kb\n\n"


'''
-------------------------------- SAMOTNY PROGRAM -------------------------------------
'''

try:
	param1 = sys.argv[1]
except:
	print napoveda
	sys.exit(0)


try:
	param2 = sys.argv[2]
except:
	param2 = ""


if param2.isdigit():
	user_input = int(param2)


if param1.isdigit():
	user_input = int(param1)
	print ""

	if user_input < 10000:
	        print "  Cyrillic numeral:    "+str(prevodcisla(user_input,"cyrilice"))
	if user_input < 6000:
        	print "  Glagolitic numeral:  "+str(prevodcisla(user_input,"hlaholice"))

	print "  Old Church Slavonic: "+cislo_na_slovo(user_input)
	print ""
	sys.exit(0)


elif param1 == "--cyrillic" or param1 =="-c":
        if user_input < 10000:
        	print str(prevodcisla(user_input,"cyrilice"))
        else:
                print 'unavailable'
                sys.exit(1)
elif param1 == "--glagolitic" or param1 == "-g":
        if user_input < 6000:
        	print str(prevodcisla(user_input,"hlaholice"))
        else:
                print 'unavailable'
                sys.exit(1)
elif param1 == "--slavic" or param1 == "-s":
	print cislo_na_slovo(user_input)

elif param1 == "--help" or param1 == "-h":
	print napoveda
	sys.exit(0)


else:
	print napoveda
        sys.exit(1)




