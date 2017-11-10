# Cara Menggunakan

## 1. import hebb

```python
from hebb import Hebb
```
## 2. format input data dan bobot

```python
data = [
	[[0,1,1,1,0,0],1],
	[[0,0,1,0,0,0],1],
	[[0.6,1,1,0,0,1],1],
	[[1,1,1,0,1,1],1],
	[[0.2,1,1,1,1,0.5],0],
	[[0.4,1,1,0,0,1],0],
	[[0.6,1,1,1,1,1],0],
	[[0.2,1,0,1,1,0.5],0]
]

bobot = [[0,0,0,0,0,0],0]
```
## 3. parameter
```python
hebb = Hebb(data=data, bb_awal=bobot, threshold=1)
```

## 4. fungsi penting
#### Menampilkan detail hasil perhitungan hebb
```python
hebb.show_detail()
```
#### Menampilkan hasil bobot akhir
```python
hebb.show_bobot_akhir()
```
#### Menampilkan detail hasil testing hebb
```python
hebb.detail_test()
```
#### Menampilkan hasil akhir testing
```python
hebb.hasil_test()
```
