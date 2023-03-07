import numpy as np

# Írj egy olyan fügvényt, ami megfordítja egy 2d array oszlopait
# Be: [[1,2],[3,4]]
# Ki: [[2,1],[4,3]]
# column_swap()
def column_swap(input_arr) -> np.array:
    return input_arr[:, ::-1]


#Készíts egy olyan függvényt ami összehasonlít két array-t és adjon vissza egy array-ben, hogy hol egyenlőek
# Pl Be: [7,8,9], [9,8,7]
# Ki: [1]
# compare_two_array()
# egyenlő elemszámúakra kell csak hogy működjön
def compare_two_array(a1, a2) -> np.array:
    return a1 == a2


#Készíts egy olyan függvényt, ami vissza adja a megadott array dimenzióit:
# Be: [[1,2,3], [4,5,6]]
# Ki: "sor: 2, oszlop: 3, melyseg: 1"
# get_array_shape()
# 3D-vel még műküdnie kell!
def get_array_shape(input_arr: np.array) -> str:
    arr_shape = np.shape(input_arr)
    return f"sor: {arr_shape[0]}, oszlop: {arr_shape[1]}, melyseg: {arr_shape[2]}"


# Készíts egy olyan függvényt, aminek segítségével elő tudod állítani egy neurális hálózat tanításához szükséges Y-okat egy numpy array-ből.
#Bementként add meg az array-t, illetve hogy mennyi class-od van. Kimenetként pedig adjon vissza egy 2d array-t, ahol a sorok az egyes elemek. Minden nullákkal teli legyen és csak ott álljon egyes, ahol a bementi tömb megjelöli
# Be: [1, 2, 0, 3], 4
# Ki: [[0,1,0,0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]
# encode_Y()
def encode_Y(input_arr, class_count) -> np.array:
    return np.identity(class_count)[input_arr]
