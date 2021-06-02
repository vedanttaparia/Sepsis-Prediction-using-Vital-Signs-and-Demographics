 # Sepsis Prediction using Vital Signs and Demographics
**Sepsis** is a medical emergency that describes the body’s immune response to an infection process that can lead to the end of immunity and death.

**Problem Statement:**
To predict Sepsis using Vital signs and Demographics from Patients clinical report so that patient gets time to recover in early-stage and some lives can be saved.

The challenging part in Prediction of Sepsis is that Data is not proper for accurate prediction. In most cases Data is Unstructured and if it is Structured there are lots of unnecessary values/data which is mostly null values as it is clinical data. So, preprocessing of Data is very important for accurate prediction. The dataset contains the samples of data for each patient collected over a certain interval of time. Each sample contains vital signs, laboratory data and demographics of a patient. 

All the learnings performed in this study are done using RNN-LSTM. The training mechanisms used to train the classifiers comprise every feature set, which includes the vital signs along with the physiological indicators such as heart rate, systolic blood pressure, respiratory rate, peripheral oxygen saturation, and temperature, the biochemistry lab values, the demographic and anthropomorphic aspects. Learning network used for RNN's construction of Long-Term Memory (LSTM) with 10 input layers, 5 hidden layers with a large number of 200 sets. 
The model consists of 5 layers:
Layer 1. LSTM layer comprising of 128 output cells having 10 initial input cell
Layer 2. LSTM layer comprising of 128 output cells
Layer 3. Dense layer with 64 output cells and ‘relu’ activation
Layer 4. Dense layer with 32 output cells and ‘tanh’ activation
Layer 5. Dense layer with single output cells 
Where, batch size=32 and epoch=250

**A.	Feature extraction**
The dataset contains the samples of data for each patient collected over a certain interval of time. Each sample contained 41 labels and 40 samples for the same patient. After feature extraction it was found that 30 labels had more than 90% null values (and were not relevant to the training model). Hence, the model was further proceeded by selecting 10 training labels and 1 output label.

**B.	Data Pre-processing**
The missing data was imputed and normalized using mean and standard deviation. And after the mean and deviation is found the data in the dataset is normalized . After the data normalization it was found that the data was highly imbalanced and had a high bias toward the data with non-sepsis label. In order to overcome that issue, we used random over sampling.

**C.	Training Model**
The main selected model for prediction used was LSTM-RNN. The model is divided into 5 layers of LSTM and Dense cells for epochs of 250 and validation size of 20% for a batch size of 32. The loss was computed using mean squared error.
The first and the second layer are LSTM layer of 128 output cells individually and the input taken is the 10 selected features which is taken in through the first layer. 

Now proceeding from the second layer we reduce the number of cells in the layers until there is a single binary output.

The third layer is a dense layer consist of 64 output cells with Relu being used as the activation function.

The last layer consists of a single dense layer cell with a sigmoid function 

**Comparison Graph**
![image](https://user-images.githubusercontent.com/64605506/120540375-3f8d3a00-c406-11eb-8e6a-c332ad5f3ccc.png)

**Deployment**
Flask is used for deploying the model to a website.

**output**

![image](https://user-images.githubusercontent.com/64605506/120540802-b7f3fb00-c406-11eb-8d40-0c30924ff78c.png)

![image](https://user-images.githubusercontent.com/64605506/120540823-bde9dc00-c406-11eb-9da5-f324748cfe14.png)

Therefore, further research that includes performance of a clinical trial is necessary to measure the clinical utility of machine learning models for early recognition of sepsis in infants.
