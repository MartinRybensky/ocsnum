#!/usr/bin/python
# -*- coding: utf-8 -*-


# license Creative Commons BY-NC-SA 3.0
# Created by Martin Rybensky

__version__ = '0.01.01'
__author__ = 'Martin Rybensky'

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





'''
/**********************************************************************************
 * 
 *  Definice funkcí převádějících čísla na slovní vyjádření ve staroslověnštině
 * 
 *  Základem je funkce cislo_na_slovo(), ze které jsou všechny ostatní funkce 
 *  na základě řádu zadaného čísla volány.
 * 
 *  Testování nenulové hodnoty každého řádu je voláno kvůli vyhodnocení, zda
 *  má být za slovním vyjádřením aktuálně vypsaného řádu tečka či и
 * 
 **********************************************************************************/
'''




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



'''
-------------------------------- SAMOTNY PROGRAM -------------------------------------
'''


try:
    user_input = sys.argv[1]
    user_input = int(user_input)
except:
    print 'you must specify a number as a parameter'
    sys.exit(0)


vystup = cislo_na_slovo(user_input)
print ""
print "  Cyrillic numeral:    авгдезѕиѳклмнѯопчрстѹфццѡ"
print "  Glagolitic numeral:  ⱑⱋⰼⰴ"
print "  Old Church Slavonic: "+vystup
print ""
sys.exit(0)


