#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = float(input("Masukkan sebuah bilangan: "))

if x > 0:
    print("Bilangan positif")
elif x < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")


# In[2]:


x = float(input("Masukkan sebuah bilangan: "))
result = "Bilangan positif" if x > 0 else "Bilangan negatif" if x < 0 else "Bilangan nol"
print(result)


# In[10]:


def jumlah_hari(bulan):
    if bulan == 2:
        return 29  
    elif bulan in [4, 6, 9, 11]:
        return 30  
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31 
    else:
        return -1 


bulan = int(input("Masukkan bulan (1-12): "))

hari = jumlah_hari(bulan)

if hari != -1:
    print("Jumlah hari:", hari)
else:
    print("Bulan yang dimasukkan tidak valid.")


# In[11]:


def jenis_segitiga():
    try:
        sisi1 = int(input("Masukkan sisi 1: "))
        sisi2 = int(input("Masukkan sisi 2: "))
        sisi3 = int(input("Masukkan sisi 3: "))
        
        if sisi1 == sisi2 == sisi3:
            print("3 sisi sama")
        elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
            print("2 sisi sama")
        else:
            print("Tidak ada yang sama")
    except ValueError:
        print("Input tidak valid. Masukkan bilangan bulat.")
        
jenis_segitiga()


# In[ ]:




