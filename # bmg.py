# SANAL MANTIK DEVRESİ SİMÜLATÖRÜ
# Bu program AND, OR, XOR ve NOT kapılarını simüle eder
#  3-değişkenli mantık ifadesinin doğruluk tablolarını gösterir

# --- MANTIK KAPILARI ---

def AND_KAPISI(a, b):
    return a & b        # '&' operatoruND islemi par

def OR_KAPISI(a, b):
    return a | b        # '|' operatoru islemi par

def XOR_KAPISI(a, b):   
    return a ^ b        # '^' operatoru isemi yapar

def NOT_KAPISI(a):
    return 1 - a        # 0 ise 1, 1 ise 0 doner



def kontrol_giris(deger_adi):   # kullanıcıdan alınan değerin 0 veya 1 olduğunu kontrol eder
    deger = int(input(f"{deger_adi} girisini gir (0 veya 1): "))
    if deger != 0 and deger != 1:
        print("HATA: Sadece 0 veya 1 girebilirsiniz!")
        exit()
    return deger


print("=== SANAL MANTIK DEVRESİ ===")

a = kontrol_giris("A")  # kontrol_giris fonksiyonu ile kullanıcıdan A ve B değerleri alınır
b = kontrol_giris("B")



kapi = input("Kapı türünü seç (AND / OR / XOR / NOT): ").upper()  # .upper() ile büyük harfe çevirilir
if kapi == "AND":
    result = AND_KAPISI(a, b)
elif kapi  == "OR":
    result = OR_KAPISI(a, b)
elif kapi == "XOR":
    result = XOR_KAPISI(a, b)
elif kapi== "NOT":
    result = NOT_KAPISI(a)
else:
    print("Hatalı kapı türü!")
    exit()

print(f"Sonuç: {result}")

# --- DOĞRULUK TABLOLARI ---
print("\n=== 3 DEĞİŞKENLİ DOĞRULUK TABLOLARI ===")

print("\nA B C | A AND (B OR C) | A OR (B AND C) | A XOR (B AND C)")
print("--------------------------------------------------------")

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            sonuc1 = A & (B | C)
            sonuc2 = A | (B & C)
            sonuc3 = A ^ (B & C)

            print(A, B, C, "|      ", sonuc1,
                  "      |      ", sonuc2,
                  "      |      ", sonuc3)
