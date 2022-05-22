import matplotlib.pyplot as plt
import numpy as np

yatay_eksen = ["1","2","3","4","5"]
dikey_eksen_1 = [1, 2, 1.5, 3, 2.5]
dikey_eksen_2 = [2, 3, 2.5, 4, 3.5]
dikey_eksen_3 = [3, 4, 3.5, 5, 4.5]
dikey_eksen_4 = [4, 5, 4.5, 6, 5.5]
plt.title('Marker Çeşitleri')

plt.plot(yatay_eksen, dikey_eksen_1, marker = 'x', label = 'marker = \'x\'')
plt.plot(yatay_eksen, dikey_eksen_2, marker = 'o', label = 'marker = \'o\'')
plt.plot(yatay_eksen, dikey_eksen_3, marker = 's', label = 'marker = \'s\'')
plt.plot(yatay_eksen, dikey_eksen_4, marker = 'd', label = 'marker = \'d\'')
plt.legend()
plt.grid()

plt.show()


