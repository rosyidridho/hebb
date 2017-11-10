class Hebb:
    def __init__(self, data, bb_awal, threshold):
        self.data=data
        self.bb_awal=bb_awal
        self.threshold=threshold
        self.result=[]

    def perubahan_bobot(self, data):
        return map(lambda x: float(x)*data[1], data[0])

    def bobot_akhir(self, bbt_awal, perub_bobot, target):
        w = map(lambda x, y: float(x)+float(y), bbt_awal[0], perub_bobot)
        b = target
        return [w,b]

    def show_detail(self):
        self.result=[]
        bbt_akhir=self.bb_awal
        for d in self.data:
            pb = self.perubahan_bobot(data=d)
            bbt_akhir = self.bobot_akhir(bbt_awal=bbt_akhir, perub_bobot=pb, target=d[1])
            hasil = [d[0], d[1], pb[0], pb[1], bbt_akhir[0], bbt_akhir[1]]
            self.result.append(hasil)
        return self.result

    def show_bobot_akhir(self):
        bbt_akhir = self.show_detail()
        return [bbt_akhir[-1][4], bbt_akhir[-1][5]]

    def Y_net(self, T, N):
        return 1 if N >= T else 0

    def detail_test(self):
        bbt_akhir = self.show_bobot_akhir()
        self.result=[]
        for d in self.data:
            net = sum(map(lambda x, y: float(x)*float(y), d[0], bbt_akhir[0]))
            Ynet = self.Y_net(T=self.threshold, N=net)
            cek = "Sama" if Ynet == d[1] else "Tidak Sama"
            data = [d[0], net, Ynet, d[1], cek]
            self.result.append(data)
        return self.result

    def hasil_test(self):
        jml_data = 0
        akurasi = 0
        for dt in self.detail_test():
            akurasi = akurasi+1 if dt[4] == "Sama" else akurasi+0
            jml_data += 1
        akurasi = float(akurasi)/float(jml_data)*100.0
        return akurasi
