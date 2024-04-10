import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


hetek_szama = 52
edzesek_szama = hetek_szama * 2


idok = np.arange(1, edzesek_szama + 1)
sulyok_1_percent = 40 * (1 + 0.01) ** (idok / 2) 


ismetlesek = 4 + (idok % 4 > 1) * 3  


adatok_1_percent = pd.DataFrame({
    'Edzés Sorszáma': idok,
    'Súly (kg)': np.round(sulyok_1_percent, 2),
    'Ismétlések száma': ismetlesek
})


excel_fajl_neve_1_percent = 'C:/Users/benit/OneDrive/Asztali gép/fekvenyomas_progresszio_1_percent.xlsx'

adatok_1_percent.to_excel(excel_fajl_neve_1_percent, index=False)


plt.figure(figsize=(12, 6))
plt.plot(adatok_1_percent['Edzés Sorszáma'], adatok_1_percent['Súly (kg)'], label='Súly (kg)', marker='o', color='blue')
plt.title('Fekvenyomás Progresszió Heti 2 Edzéssel és Heti 1% Növekedéssel Egy Éven Át')
plt.xlabel('Edzés Sorszáma')
plt.ylabel('Súly (kg)')
plt.twinx()
plt.plot(adatok_1_percent['Edzés Sorszáma'], adatok_1_percent['Ismétlések száma'], label='Ismétlések száma', marker='x', color='red')
plt.ylabel('Ismétlések száma')
plt.legend(loc='upper left')
plt.grid(True)

plt.show()