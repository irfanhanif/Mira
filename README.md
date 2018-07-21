# Tugas Akhir Irfan Hanif
Tugas akhir berjudul "*Klasifikasi Perintah Bahasa Natural Menggunakan Global Vectors for Word Representations, Transfer Learning, dan Convolutional Neural Networs Pada Aplikasi Chatbots*" <br>
**Irfan Hanif** <br>
**05111440000177** <br> <br>

S1 Informatika <br>
Institut Teknologi Sepuluh Nopember <br>
Surabaya

## Case Study
The chatbot was built to answer Frequently Asked Questions (FAQs) of Schematics. [What is Schematics?](https://schematics.its.ac.id/). <br>
To get FAQs Schematics dataset, please email me at: if.irfanhanif@gmail.com (indonesian language used).

## Corpus
**Wikipeda Bahasa Indonesia** : [here](https://dumps.wikimedia.org/idwiki/latest/) <br>
**LAPOR! Dataset** : [here](http://data.go.id/dataset/data-aspirasi-dan-pengaduan-masyarakat) <br> <br>

**Corpus Wiki + Lapor** : [here](https://drive.google.com/file/d/1fQaPzbNEiJ3BK7YoOu-lZNMzQdiNSIhi/view?usp=sharing) <br>
**GloVe generated** : [here](https://drive.google.com/file/d/1pdmiL-q26YN6gfKgplh8kMrtPPwp_wB_/view?usp=sharing) <br> <br>

Total token : 82.953.449 <br>
Unique words : 2.216.260 <br>
Total vocabs used : 331.286 <br><br>

## Environment
### Machine
* OS: Ubuntu 16.04.
* CPU: Intel core i7 4720HQ (4 cores).
* GPU: NVidia GeForce GTX 950m 2GB.
* Python 2.7.

### GloVe
You can download GloVe source code based on C language at  [nlp.stanford.edu/projects/glove](https://nlp.stanford.edu/projects/glove/).
### Gensim
`sudo pip install --upgrade gensim` --- [Read more](https://radimrehurek.com/gensim/install.html)
### TensorFlow
For GPU usage, don't forget to install **CUDA Toolkit**, **cuDNN SDK**, and its **environment variables**.<br>
Install TensorFlow (CPU): `sudo pip install tensorflow`<br>
Install TensorFlow (GPU): `sudo pip install tensorflow-gpu`<br>
For your own convenience, please follow complete instructions [here](https://www.tensorflow.org/install/install_linux).
### Keras
`sudo pip install keras` --- [Read more](https://keras.io/#installation)
### Scikit-Learn
`sudo pip install -U scikit-learn` --- [Read more](http://scikit-learn.org/stable/install.html)
### Line Bot SDK
To use LINE API Messenger, first you need to install **Line Bot SDK** `sudo pip install line-bot-sdk`. Then you can deploy your own app at Heroku. For complete tutorial, please follow this instructions [here](https://developers.line.me/en/docs/messaging-api/building-sample-bot-with-heroku/). You can use your own VPS with SSL installed.
### Results
GloVe word embeddings Bahasa Indonesia semantic test with *common-capital-countries* : **86.4%**
Convolutional Neural Networks trained on Schematics FAQs dataset: **95.6%**
### Scheenshots
<img src="https://raw.githubusercontent.com/irfanhanif/Mira/master/mira1.PNG" width="300"/> <img src="https://raw.githubusercontent.com/irfanhanif/Mira/master/mira2.PNG" width="300"/>

### How To Run
1. `IPython Notebook/Tugas-Akhir-Final.ipynb` adalah file ipython notebook yang berisi bagaimana data FAQs Schematics dan LAPOR! melalui proses preprocessing hingga menghasilkan file numpy yang siap menjadi masukan dari Convolutional Neural Networks.
2. Untuk mendapatkan word embeddings GloVe, dapat menjalankan source code yang dibuka secara publik oleh Pennington et al. (2014) pada alamat GloVe yang telah dilampirkan di atas.
3. File source code CNN per skenario dapat dilihat seluruhnya pada folder `ConvNN/`
4. Skenario yang ada pada tugas akhir ini yang ada terdiri dari tiga skenario. (1) CNN tanpa transfer learning pada file `ConvNN/cnn_data_target_wtl.py`, (2) CNN dengan transfer learning skenario 1 pada file `ConvNN/cnn_data_target_tl_1.py`, dan (3) CNN dengan transfer learning skenario 2 pada file `ConvNN/cnn_data_target_tl_2.py`.
5. Folder `Mira/` berisi setiap file yang harus diletakkan pada server chatbot. Word embddings harus diletakkan pada basis data untuk chatbot ini.
6. `wordembd2db.py` adalah file yang ditulis untuk memindahkan word embedding yang diload pada RAM ke basis data. 

### Testing 
1. `IPython Notebook/Glove-Test.ipynb` adalah file yang berisi testing untuk word embeddings GloVe. `IPython Notebook/Confusion Matrix.ipynb` adalah file yang berisi bagaimana menampilkan confusion matrix pada model akhir CNN.
2. `SpeedAnalysis/` adalah folder yang berisi testing untuk kecepatan learning pada CNN. 
3. `GloVe-1.2/eval` adalah folder yang berisi evaluasi semantik pada word embeddings.