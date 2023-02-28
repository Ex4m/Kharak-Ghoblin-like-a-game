import numpy as np

inp = input("press any key to reval next section of the code: ")
print("\n------Základy v Array - rozdály, shape, ndim,size,dtype------")
print("""
multi_dim = np.array(
[
[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
[[13,14,15,16],[17,18,19,20],[21,22,23,24]]
])""")
multi_dim = np.array(
[
[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
[[13,14,15,16],[17,18,19,20],[21,22,23,24]]
])

print("""
print(multi_dim.shape)  # počet listů/objektů v array a jejich x,y elementů - ne jejich hodnoty
print(multi_dim.ndim)   # level / nesting size
print(multi_dim.size)   # v podstatě výstup z .shape a následně jich násobek ... tedy počet jednotlivých elementů ve všech listech
print(multi_dim.dtype)  # np je vyvinutý v jiném jazyce než v pythonu a tak je na správný typ dat choulostivější
                        # např. pokud mám v arrayi int a přidám tam str tak to všechno změní na str. v klasickém python listu to funguje separátně
""")

print(multi_dim.shape)  # počet listů/objektů v array a jejich x,y elementů - ne jejich hodnoty
print(multi_dim.ndim)   # level / nesting size
print(multi_dim.size)   # v podstatě výstup z .shape a následně jich násobek ... tedy počet jednotlivých elementů ve všech listech
print(multi_dim.dtype)  # np je vyvinutý v jiném jazyce než v pythonu a tak je na správný typ dat choulostivější
                        # např. pokud mám v arrayi int a přidám tam str tak to všechno změní na str. v klasickém python listu to funguje separátně

inp = input("press any key to reval next section of the code: ")
print("\n------Plnění arrays - full,zeron,ones a empty + step -----")
print("""
a = np.full((2,3,4), 4) #vytvoří 2 separátní listy, který každý obsahují 3 listy o 4 elementech a naplní je všechny číslem 4
print(a)
b = np.zeros((3,4,5))   #vytvoří 3 separátní listy, který každý obsahují 4 listy o 5 elementech a všechny naplní 0
print(b)
c = np.ones((1,2,3))    #vytvoří 1 separátní list, který obsahuje 2 listy o 5 elementech a všechny naplní 1
print(c)
d = np.empty((2,3,6))   #dělá to samé jen nenaplní listy žádnými čísly ale pouze alokuje pro ně místo v paměti, ale při printu se tam objevují náhodné floaty
print(d)

""")
a = np.full((2,3,4), 4) 
print(a)
b = np.zeros((3,4,5))   
print(b)
c = np.ones((1,2,3))    
print(c)
d = np.empty((2,3,6))   
print(d)

print("\narraye vzniklé pomocí stepu")
print("""
x_values = np.arange(0,1000,7)  #udělá list od 0 do 1000 s odskokem po 7
print(x_values)
y_values = np.linspace(0,1000,11) # vezme range od do a step zde nahrazuje dividera. Protože ale kalkuluje s mezerami je nutné zadávat +1 pokud chceš např. čísla od 0 do 1000 po 100
print(y_values)""")
x_values = np.arange(0,1000,7)  
print(x_values)
y_values = np.linspace(0,1000,11) 
print(y_values)

inp = input("press any key to reval next section of the code: ")
print("\n------Empty Values .nan a .inf -----")
print("""
np.nan      # používá se hlavně když potřebuji např. v arrayi nečím zaplnit místo aby program nespadl. Navíc pak můžu vyhledat a všechny nany nějak přepsat
np.inf      # zde pak výhoda např. při dělení 0 kdy to hodí tuto hlášku
print(np.isnan(np.sqrt(-1)))           # vrátí True protože není další hodnota
print(np.isinf(np.array([5,5]) / 0))   # vrátí True protože dělí 0
""")
np.nan      
np.inf      
print(np.isnan(np.sqrt(-1)))           
print(np.isinf(np.array([5,5]) / 0))   

inp = input("press any key to reval next section of the code: ")
print("\n------Rozdíly v matematických operacích mezi listy nativní v pythonu a numpy arrays------")
print("""
python_list_1 = [1,2,3,4,5]
python_list_2 = [6,7,8,9,10]

numpy_list_1 = np.array(python_list_1)
numpy_list_2 = np.array(python_list_2)
""")
python_list_1 = [1,2,3,4,5]
python_list_2 = [6,7,8,9,10]

numpy_list_1 = np.array(python_list_1)
numpy_list_2 = np.array(python_list_2)

print("""rozdíl při násobení/dělení listů 
print(python_list_1 * 5)    # zařadí 5 za sebe hodnoty z listu
print(numpy_list_1 * 5)     # vynásobí hodnoty v listu 5""")
print(python_list_1 * 5)    
print(numpy_list_1 * 5)     

inp = input("press any key to reval next section of the code: ")
print("\n------v python listu nelze přičítat hodnoty k jednotlivým elementům------")
try:
    print("python_list_1 + 5")
    print(python_list_1 + 5)
except Exception as chyba:
    print("toto je chyba kterou vyhazuje try při pokusu sčítání python listů")
    print(chyba)
print("\n------v numpy to lze, protože pracuje s elementy jako s vektory------")
print("numpy_list_1 + 5")
print(numpy_list_1 + 5)

print("\n------při sčítání listů v pythonu prostě listy za sebe spojíme, v numpy se vektorově sečtou elementy------") 
print("python_list_1 + python_list_2")
print(python_list_1 + python_list_2)
print("numpy_list_1 + numpy_list_2")
print(numpy_list_1 + numpy_list_2)

inp = input("press any key to reval next section of the code: ")
print("\n------Také je v numpy možné násobit mezi sebou elemnty stejného typu ale jiných dimenzí------") 
a1 = np.array([1,2,3,4])
a2 = np.array([[3],[2],[6]])
print("array 1")
print(a1)
print("array 2")
print(a2)
print("\na1 + a2")
print(a1 + a2)

inp = input("press any key to reval next section of the code: ")
print("\n------Můžeme volat různé funkce přímo na dané dimenze arraye------") 
a = np.array([[1,2,3,4],
            [2,3,4,5]]) 
print("vezme si např. 2-dimenzionální array")
print(a)
print("np.sqrt(a)") #odmocnina
print(np.sqrt(a))
print("np.sin(a)")
print(np.sin(a))
print("np.exp(a)")
print(np.exp(a))
print("np.log(a)")
print(np.log(a))

inp = input("press any key to reval next section of the code: ")
print("\n------append + concatenate na arraye-----")
print(a)
print("np.append(a, [7,8,9,10]) - a zde slouží jako základ ke kterému budeme následně přidávat [7,8,9,10]") 
b = np.append(a, [7,8,9,10])
print(b)
print("np.insert(a, 4, [7,8,9,10]) : a - základ, 4 - pozice od které chceme přidávat, [] - co chceme přidat")
c = np.insert(a, 4, [7,8,9,10])
print(c)
print("Concatenate")
print("""
con_1 = np.array([1,2,3,4,5],
                [7,8,9,10,11])
con_2 = np.array([12,13,14,15,16],
                [17,18,19,20,21])""")
con_1 = np.array([[1,2,3,4,5],
                [7,8,9,10,11]])
con_2 = np.array([[12,13,14,15,16],
                [17,18,19,20,21]])
print("np.concatenate((con_1,con_2), axis = 0 -  0 přidá do con_1 con_2 jako další řádky/listy - 1 přidá do aktuálních listů další elementy z con_2")                
con_1 = np.concatenate((con_1,con_2), axis = 0)
print(con_1)

inp = input("press any key to reval next section of the code: ")
print("\n------delete z arraye-----")
print(a)
print("np.delete(a, 1), np.delete(a, 4) - pokud nechám pouze takto, tak to jde čistě po elementech v arrayi a jejich přirazeném číslu v řadě")
d = np.delete(a, 1)
e = np.delete(a, 4)
print(d,e)
print("np.delete(a, 1, 0) - toto mě zbaví celého druhého řádku - listu")
f = np.delete(a, 1, 0)
print(f)
print(" - pokud bude druhá hodnota nenulová tak bude del likvidovat sloupce místo řádků")
g = np.delete(a, 2, 1)
print(g)


inp = input("press any key to reval next section of the code: ")
print("\n------Shape and Reshape arraye-----")
multi_dim_array = np.array([[1,2,3,4,5],
                            [6,7,8,9,10],
                            [11,12,13,14,15],
                            [16,17,18,19,20]])
print(multi_dim_array)
print("počet listů a jednotlivých elementů v arrayi")
print(multi_dim_array.shape)
print("multi_dim_array.reshape((5,4)) - toto udělá z arraye 5 listů po 4 elementech")
h = multi_dim_array.reshape((5,4))
print(h)
print("pár dalších příkladů - aby bylo kompatibilní musí násobek vždy sedět na původní shape - tedy v tomto případě 20")
print("multi_dim_array.reshape((2,2,5))")
print(multi_dim_array.reshape((2,2,5)))
print("multi_dim_array.reshape((5,1,2))")
print(multi_dim_array.reshape((5,2,2)))


inp = input("press any key to reval next section of the code: ")
print("\n------Aggregators z listů - min,max,mean,std, a sum -----")
print("vezmeme si multi_dim_array")

print("""
multi_dim_array.min()       # min hodnota z daného arraye
multi_dim_array.max()       # max ..
mlti_dim_array.std()        # standard deviation - např. bollinger bands
multi_dim_array.mean()      # průměr
multi_dim_array.sum()       # suma
np.median(multi_dim_array)  # medián
""")

print(multi_dim_array.min())
print(multi_dim_array.max())
print(multi_dim_array.std())
print(multi_dim_array.mean())
print(multi_dim_array.sum())
print(np.median(multi_dim_array))


inp = input("press any key to reval next section of the code: ")
print("\n------Random numbers generator -----")
print("""
numbers = np.random.randint(50,100, size = (2,4,5)) # náhodný integer číslo od 50 do 100 ve 2 listech o 4 podlistech a 5 elemetech
number = np.random.randint(100)                     # může být i jako np.random.randit(100) - zde vytvoří pouze jedno náhodné číslo od 0 do 100
""")
numbers = np.random.randint(50,100, size = (2,4,5)) 
print(numbers)
number = np.random.randint(100)                     
print(number)

print("\n coin flip")
print("12x hodí mincí s pravděpodobností 50 % a uloží do 2 listů s 3 podlisty a 5 elementy - výsledek v listech je kolikrát hodil 'hlavu' z x-(12) pokusů")
print("coin_flip = np.random.binomial(12, p = 0.5, size = (2,3,5))")
coin_flip = np.random.binomial(12, p = 0.5, size = (2,3,5))
print(coin_flip)

print("\n choice - náhodný výběr z elementů daného arraye")
print("ran_choice = np.random.choice([10,17,25,28,99], size =(3,2,4)) - var které bere pouze jako 1 list")
ran_choice = np.random.choice([10,17,25,28,99], size =(3,2,4))
print(ran_choice)

