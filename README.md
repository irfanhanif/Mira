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
![Mira-1](https://raw.githubusercontent.com/irfanhanif/Mira/master/mira1.PNG)
![Mira-2](https://raw.githubusercontent.com/irfanhanif/Mira/master/mira2.PNG)

