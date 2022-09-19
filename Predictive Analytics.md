# LAPORAN PROYEK MACHINE LEARNING - DWI NUR AGUSTINA
#
#
## Domain Proyek
*Foreign Exchange (forex)* saat ini berkembang pesat sebagai salah satu model investasi yang menggiurkan, karena *forex trading* memiliki tingkat pengembalian yang tinggi. *Forex* merupakan kegiatan jual beli mata uang suatu negara untuk mendapatkan keuntungan. *Forex* dan valas (Valuta Asing) adalah hal yang sama, hanya saja berbeda pada penggunaannya. Valas biasanya ditransaksikan pada bank atau tempat penukaran uang, sedangkan transaksi *forex* biasanya dilakukan secara *online*. Pergerakan nilai *forex* yang cukup signifikan dan besarnya keuntungan yang ditawarkan ternyata menarik beberapa masyarakat atau kalangan tertentu untuk berkecimpung dalam *forex market*. *Forex market* memiliki fungsi pokok untuk membantu kelancaran lalu lintas pembayaran internasional. Ada tujuh mata uang dunia yang lazim di perdagangkan di *forex market*, yaitu Dollar Amerika (USD), Poundsterling Inggris (GBP), Euro Dollar (EUR), Swiss Franc (CHF), Japanese Yen (JPY), Australian Dollar (AUD), dan Canadian Dollar (CAD).

Menurut data survei *BIS (Bank International for Settlement*, bank sentral dunia) yang dilakukan pada akhir tahun 2004, nilai transaksi *forex market* mencapai lebih dari USD$ 1,4 triliun per hari. Dan di tahun 2006, nilai transaksi pasar *forex* telah melebihi USD$ 2 trilun per harinya. Dengan demikian, prospek investasi di perdagangan *forex* sangat bagus. Dengan tingginya nilai pada *forex market*, resiko yang dihadapi pun akan semakin besar pula. *Forex* termasuk investasi kategori *high risk* alias beresiko tinggi karena transaksi yang kurang tepat sasaran dapat langsung menggerus modal deposit di dalam akun dengan cepat, tergantung mata uang apa yang ditransaksikan. Resiko yang harus dihadapi para *trader forex* juga tidak main-main. Arus dana bergerak begitu cepat, sehingga jika salah mengambil keputusan, maka memiliki kemungkinan kehilangan dana 100%.

Sesungguhnya risiko kerugian atau keuntungan pun tergantung dari keahlian memprediksi pergerakan *forex* serta harus ahli memprediksi kapan harus membeli atau menjual. Selain itu juga harus mengetahui kapan harus masuk, berapa lama menunggu dan melakukan pembelian atau menjualnya kembali karena itu merupakan keputusan yang sangat berbahaya dan akan mempengaruhi nasib dana selanjutnya. Untuk itu harus selalu memperbaharui informasi untuk dapat memperkirakan nilai *forex* di masa mendatang. Salah satu cara yang dapat dilakukan adalah dengan menggunakan *forecasting*. Peramalan *(forecasting)* adalah suatu teknik untuk meramalkan keadaan dimasa yang akan datang menggunakan data-data di masa lalu. Peramalan dalam *forex* ini adalah peramalan *time series*. Dengan mendeteksi pola dan kecenderungan data *time series*, kemudian memformulasikannya dalam suatu model, maka dapat digunakan untuk memprediksi data yang akan datang. Model dengan akurasi yang tinggi akan menyebabkan nilai prediksi cukup valid untuk digunakan sebagai pendukung dalam proses pengambilan keputusan.


## *Business Understanding*
#### 1. *Problem Statements*
Berdasarkan latar belakang di atas, maka dapat dirumuskan permasalahan sebagai berikut:
- Bagaimana cara menganalisis data harga *forex* pada *market EUR/USD = X*?
- Bagaimana cara mengolah data agar dapat dilatih dengan baik oleh model?
- Bagaimana cara membangun model yang dapat memprediksi *time series forecasting* dengan tingkat akurasi yang baik?

#### *2. Goals*
Penelitian ini dilakukan dengan tujuan sebagai berikut:
- Dapat memprediksi harga *forex* pada *market EUR/USD* dengan menggunakan model *machine learning*
- Dapat mengolah data dengan optimal agar dapat dilatih dengan baik oleh model *machine learning*
- Dapat menemukan model yang dapat memprediksi *time series forecasting* dengan tingkat akurasi yang baik

#### *3. Solution Statements*
Dari rumusan masalah dan tujuan yang telah diuraikan, solusi yang dapat dilakukan adalah sebagai berikut:
- Melakukan analisis dengan cara menangani *missing value* pada data, mencari korelasi pada data, menangani *outlier* pada data, dan melakukan normalisasi pada data. Selain itu juga dapat melakukan eksplorasi dan pemrosesan pada data dengan memvisualisasikannya.
- Membuat model regresi untuk memprediksi harga yang akan datang. Dimana dalam proyek ini rencananya akan memakai algoritma *Support Vector Regression, KNN,* dan *Gradient Boosting Regression*.
- Melakukan *hyperparameter tuning* agar model dapat berjalan pada performa yang terbaik


## *Data Understanding*
Dataset yang digunakan pada proyek ini adalah dataset yang diambil dari website https://www.kaggle.com/ lebih tepatnya yaitu https://www.kaggle.com/datasets/meehau/EURUSD. Dimana dataset yang digunakan memiliki format .csv dan mempunyai total 14783 *records* dan 6 *columns*. Kolom-kolom tersebut diantaranya yaitu :
1. *Time* : merupakan tanggal dan waktu data tersebut direkam
2. *Open* : merupakan harga pembukaan pada hari tersebut
3. *High* : merupakan harga tertinggi pada hari tersebut
4. *Low* : merupakan harga terendah pada hari tersebut
5. *Close* : merupakan harga penutupan pada hari tersebut
6. *Volume* : merupakan banyaknya transaksi pada hari tersebut


## *Data Preparation*
Teknik *data preparation* yang dilakukan adalah sebagai berikut:
1. Menghapus fitur yang tidak diperlukan dengan fungsi *drop*
Hal tersebut dilakukan karena pada proyek kali ini tidak memerlukan fitur *time, close*, dan *volume*. Sehingga ketiga fitur tersebut akan dihapus.

2. Melakukan *splitting* pada dataset
Dataset akan dibagi menjadi 2, yaitu *train* dan *test data*. *Train data* digunakan sebagai *training model*, sedangkan *test data* digunakan sebagai validasi apakah model yang digunakan sudah akurat atau belum. Proposi yang umum dalam *splitting dataset* adalah 80:20, 80% sebagai *train data* dan 20% sebagai *test data*, sehingga pada proyek ini akan menggunakan proporsi tersebut.

3. Melakukan *data normalization*
Normalisasi data dilakukan agar model dapat bekerja dengan lebih optimal. Biasanya, normalisasi akan mentransformasi data dalam skala tertentu. Pada proyek ini, data akan dinormalisasi pada skala 0 hingga 1. Data yang dinormalisasi adalah *X_train* dan *X_test* dengan menggunakan *library MinMaxScaler*.


## *Modeling*
Model yang digunakan pada proyek kali ini adalah *Support Vector Regression, KNN,* dan *Gradient Boosting Regression*.
1. *Support Vector Regression
Support Vector Regression* memiliki prinsip yang sama dengan SVM, namun SVM biasanya digunakan dalam klasifikasi. Pada SVM, algoritma tersebut berusaha mencari jalan terbesar yang bisa memisahkan sampel dari kelas berbeda, sedangkan SVR mencari jalan yang dapat menampung sebanyak mungkin sampel di jalan. Untuk *hyperparameter* yang digunakan pada model ini adalah sebagai berikut:
- *kernel : hyperparameter* ini digunakan untuk menghitung kernel matriks sebelumnya. 
- *C : hyperparameter* ini adalah parameter regularisasi digunakan untuk menukar klasifikasi yang benar dari contoh *training* terhadap maksimalisasi margin fungsi keputusan.
- *gamma : hyperparameter* ini digunakan untuk menentukan seberapa jauh pengaruh contoh pelatihan, dimana jika nilainya rendah berarti jauh dan jika nilainya tinggi berarti dekat.
Untuk nilai setiap *hyperparameter* disetiap algoritma adalah sebagai berikut :
kernel : ['rbf']
C : [0.001, 0.01, 0.1, 10, 100, 1000]
gamma : [0.3, 0.03, 0.003, 0.0003]

Kelebihan dari *Support Vector Regression* adalah lebih efektif pada data dimensi tinggi (data dengan jumlah fitur yang banyak) dan memorinya lebih efisien karena menggunakan *subset* poin pelatihan. Sedangkan kekurangan dari *Support Vector Regression* adalah sulit dipakai pada data skala besar.

2. *K-Nearest Neighbors (KNN)
K-Nearest Neighbors* atau KNN merupakan algoritma *machine learning* yang bekerja dengan mengklasifikasikan data baru menggunakan kemiripan antara data baru dengan sejumlah data (k) pada data yang telah ada. Algoritma ini dapat digunakan untuk klasifikasi dan regresi. Untuk *hyperparameter* yang digunakan pada model ini hanya 1 yaitu *n_neighbors, hyperparameter* ini adalah jumlah tetangga yang diperlukan untuk menentukan letak data baru. Dimana *n_neighbors* memiliki nilai sebesar 1 dan 10.

Kelebihan dari *K-Nearest Neighbors (KNN)* adalah dapat menerima data yang masih *noisy*, sangat efektif apabila jumlah datanya banyak, dan mudah diimplementasikan. Sedangkan kekurangan dari *K-Nearest Neighbors (KNN)* adalah sensitif pada *outlier* dan rentan pada fitur yang kurang informatif.

3. *Gradient Boosting Regression
Gradient Boosting Regression* adalah algoritma *machine learning* yang menggunakan teknik *ensembel learning* dari *decision tree* untuk memprediksi nilai. *Gradient Boosting Regression* sangat mampu menangani *pattern* yang kompleks dan data ketika *linear model* tidak dapat menangani. Untuk *hyperparameter* yang digunakan pada model ini adalah sebagai berikut:
- *criterion : hyperparameter* yang digunakan untuk menemukan fitur dan ambang batas optimal dalam membagi data.
- *learning_rate : hyperparameter training* yang digunakan untuk menghitung nilai koreksi bobot padad waktu proses *training*. Umumnya nilai *learning rate* berkisar antara 0 hingga 1.
- *n_estimators* : jumlah tahapan *boosting* yang akan dilakukan.
Untuk nilai setiap *hyperparameter* disetiap algoritma adalah sebagai berikut :
*criterion : 'squared_error'
learning_rate* : 0.01
*n_estimators* : 1000

Kelebihan dari *Gradient Boosting Regression* adalah hasil pemodelan yang lebih akurat, model yang stabil dan lebih kuat *(robust)*, serta dapat digunakan untuk menangkap hubungan *linear* maupun *non linear* pada data. Sedangkan kekurangan dari *Gradient Boosting Regression* adalah pengurangan kemampuan interpretasi model, waktu komputasi dan desain tinggi, serta tingkat kesulitan yang tinggi dalam pemilihan model.


## *Evaluation*
Untuk evaluasi pada proyek kali ini adalah menggunakan *mse (mean squared error)*, dimana metrik tersebut digunakan untuk mengukur seberapa dekat garis pas dengan titik data.

![image](https://user-images.githubusercontent.com/97511774/191058303-7e790b2b-31bc-45c8-890d-0d6e01b3a274.png)

Dimana : n = jumlah titik data, Yi = nilai sesungguhnya, dan Yi_hat = nilai prediksi. 

Untuk proyek kali ini terdapat 2 model yang dapat berjalan dengan performa optimal yaitu, Gradient Boosting model dan K-Nearest Neighbors. Sehingga dapat disimpulkan bahwa model dapat memprediksi harga dari pasar foreign exchange (forex) dari data tes dengan baik. Sehingga kedepannya dapat membantu para trader dalam melakukan keputusan pembelian atau penjualan pasar. Berikut merupakan hasil dari *mse (mean squared error)*.

|                  | train_mse | test_mse |
|------------------|-----------|----------|
| SVR              | 0.000404  | 0.000415 |
| KNN              | 0.0       | 0.0      |
| GradientBoosting | 0.0       | 0.0      |

Dari tabel diatas dapat dilihat bahwa algoritma SVR memiliki nilai *mse (mean squared error)* pada *data train* sebesar 0.000404 dan pada *data test* sebesar 0.000415. Kemudian pada algoritma KNN memiliki nilai *mse (mean squared error)* pada *data train* sebesar 0.0 dan pada *data test* sebesar 0.0. Dan pada algoritma *GradientBoosting* memiliki nilai *mse (mean squared error)* pada *data train* sebesar 0.0 dan pada *data test* sebesar 0.0. Hal tersebut menunjukkan bahwa pada proyek kali ini terdapat 2 model yang dapat berjalan dengan performa optimal yaitu, Gradient Boosting model dan K-Nearest Neighbors.

Dan dibawah ini merupakan hasil plot visualisasi *mse (mean squared error)*.
![image](https://user-images.githubusercontent.com/97511774/191059160-ed851385-826e-4bdd-9d2e-22dae3144e72.png)



## Reference
[1] Y. Z. M. K. Zexin Hu, "A Survey of Forex and Stock Price Prediction Using Deep Learning," MDPI, vol. 4, no. 9, pp. 1-30, 2021. 

[2] L. Saputri, "IMPLEMENTASI JARINGAN SARAF TIRUAN RADIAL BASIS FUNCTION (RBF) PADA PERAMALAN FOREIGN EXCHANGE (FOREX)," UPI, Bandung, 2016.
