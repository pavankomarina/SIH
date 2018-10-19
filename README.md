# Voice based login system  

This project uses voice as a metric to authorise login based on a Gausian Mixture Model (GMM) model
trained on coefficients obtained from Mel Frequency Cepstral coefficients (MFCC)

### Training
The voice sample is first cleaned to get rid of unnecessary noise. MFCC is calculated for each sample followed by a Discrete Fourier transform (DFT) anf Log Transform and the data is utilized by a GMM to cluster the voice samples based on the MFCC values.

### Deployment
The project runs on Django. The web interface prompts for the user to speak. The recorded voice is then matched with the trained GMM model,
to find the best cluster it fits into. If the match is above a certain threshold value (say 90%) then the user is authorised.

### Improvements
1) Noise reduction must be taken care
2) Distinction of an actual voice from a recording
3) A better understanding of GMM and the clusters made (visualization of the clusters)
4) Enhanced training of the model (with more dataset)
5) Try different filter values for MFCC
