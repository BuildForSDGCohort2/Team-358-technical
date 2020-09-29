# FACIAL/ACOUSTIC SOUND WAVE AND GESTURE DETECTION (FASGD-III)



[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5f8c971114f24441a06ebae6ef8b17ff)](https://app.codacy.com/gh/BuildForSDGCohort2/Team-358-technical?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDGCohort2/Team-358-technical&utm_campaign=Badge_Grade_Settings)  [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]




## DESCRIPTION

<p>  Facial/Acoustic Sound Wave And Gesture Detection <b>FASGD-III</b> is a security application that performs the following which are:

<ul>

<li> Facial Recognition </li>
<li> Sound Recognition </li>
<li> Gesture Recognition </li>


</ul>

</p>

<h3> Facial Recognition </h3>
<hr>

<div>
    <img src="static/images/pred1.jpg" width="800px" height="400px">
</div> <br>

<p style="margin-left: 10px;"> A facial recognition device is a device that takes an image or a video of a human face and compares it to other images in a database.
When building a facial recognition system, several pictures of the subject must have been taken at different angles and stored in a folder called the images dataset.
This dataset which comprises of various images is trained on a deep learning or machine learning classifier to learn a mapping function on relationships between the face.
Once the machine learning classifier learns this mapping function, a serialized model weight file is generated and saved which is used to make live predictions on the individual faces. <br> 

Facial recognition system is a complex image-processing problem in real world applications with complex effects of illumination, occlusion and recognition techniques in image analysis. A <b>detection</b> application is used to find position of the faces in a given image, while a <b>recognition</b> algorithm is used to classify given images with known structured properties. This properties are used commonly in most of computer vision applications. Also, <b>recognition </b> application use standard images and detection algorithms to detect faces and extract facial features which include the <b>eyes, eyebrows, nose,</b> and <b>mouth.</b> This features make the algorithm more complicated than a single detection or recognition algorithm. <br> 

The first step for a face recognition algorithm is to get an image frame from a camera, perform a face detection and then a recognition process on the grabbed frame. 
The input image which is in form of <b>digital data</b> is sent to the face detection classifier or algorithm which is responsible for extracting <b>facial features</b> in the image. Once this is achieved, the next step would be in recognition of the face from the extracted facial embeddings. 
<br> 


</p>


<h3> Hand Gesture Recognition </h3>
<hr>

<div>
    <img src="static/images/pred2.jpg" width="800px" height="400px">
</div> <br>

<p> Hand gesture recognition is a topic in computer science and language technology with the goal of interpreting human hand gestures via machine learning algorithms. This approach is made using cameras and computer vision algorithms to interpret sign language.
With this camera, one can generate a depth map of what is being seen through the camera at short range, and use the data to approximate a 3D representation of what is being seen.  <br>

In the hand gesture recognition, a single camera is used to explore the vision-based application of the security system. This security system would have had the user customize various functions of a number of different hand gestures. For example, the hang gestures functions could be the in following pattern:
 <ul>
  <li> <b>Gesture A: </b>  Disable Alarm </li>
  <li> <b> Gesture B:</b>  Unlock the security system </li>
  <li> <b> Gesture C: </b> Call the police or Dial 911 </li>
 </ul>

Thus, this functions would be executed when a physical implementation is performed.

The hand gesture recognition works when a motion sensor perceives and interprets movements as the basic source of data input.
<ul>
  <li> Firstly, the camera feeds the image data into a sensing device that is connected to the system. </li>
  <li> Secondly, the system identifies meaningful gestures from an established gesture library where each gesture is matched to a system command by the user. </li>
  <li> Thirdly, the system connects each registered hand gesture, interprets the gesture and uses the library to identify meaningful gestures that match the library. Finally, once the gesture has been interpreted, the system executes the command or function correlated to the specific gesture. </li>

</ul>
</p>

<h3> Null Readings </h3>
<hr>
<div>
    <img src="static/images/null.jpg" width="800px" height="400px">
</div> <br>

<p> This occurs when the the cameras are closed, therefore the input returns a <b>None</b> type value. </p>



<h3> Sound Recognition </h3>
<hr>

<p>  <b>Sound recognition</b> is a technology, which is based on both traditional pattern recognition theories and audio signal analysis methods. Sound recognition technologies contain preliminary data process, <b> feature extraction </b> and classification algorithms. Sound recognition can classify feature vectors. Feature vectors are created as a result of preliminary data processing and <b> linear predictive coding. </b> <br>
Sound recognition technologies are used for:

<ul>
<li> Music recognition </li>
<li> Speech recognition </li>
<li> Automatic alarm detection and identification for surveillance, monitoring systems, based on the acoustic environment. </li>
<li> Assistance to disabled or elderly people affected in their hearing capabilities. </li>
<li> Identifying species of animals such as fish and mammals, e.g in acoustical oceanography </li>

</ul>

</p> <br>


<h4> SECURITY </h4>
<hr>
<p>
In monitoring and security, an important contribution to alarm detection and alarm verification can be supplied, using sound recognition techniques. In particular,
these methods could be helpful for intrusion detection in places like offices, stores, private homes or for the supervision of public premises exposed to person
aggression.

</p> <br>

<h4> ASSISTANCE </h4>
<hr>
<p> Solutions based on a sound recognition technology can offer assistance to disabled and elderly people affected in hearing capabilities, helping them to keep or
recover some independence in their daily occupations.


</p> <br>



## WORKING PRINCIPLE

<div>
   <img src="ANDELADOCS/FASGD-III Diagram-Page-1.jpg" width="900px" height="500px">
</div>

<br>
<p style="margin-left: 10px;"> In the security system, the facial recognition model is the first application to perform its functions, because the cameras exposed are always accepting frames from the outside world.

The cameras which are positioned at specific areas, scans the face seen in view to make predictions on if the identified persons matches the trained facec stored in its database.

Thus, if the subject face has been registered on the system like that of the owner and it runs a scan nothing really happens. However, if the subject's face has not been registered on the security system and it runs a scan, this causes the system to either sound an alarm or send notification to the owner's mobile application.

 </p>





## PREREQUISITES

<p> The following packages and modules are needed for the application to work on your system:
  <ul>
      <li> Python 3.6.6 </li>
      <li> <b> Anaconda</b> Package Manager </li>
      <li> Face-recognition module </li>
      <li> Flask </li>
      <li> Flask-SQLAlchemy </li>
      <li> Imutils </li>
      <li> Keras </li>
      <li> Librosa (Sound Wave Library) </li>
      <li> Scikit-learn </li>
      <li> Scipy </li>
      <li> Sklearn </li>
      <li> SoundFile </li>
      <li> Tensorflow </li>
      <li> Werkzeug </li>
      <li> Joblib </li>
      <li> FFmpeg </li>

  </ul>


</p>



# INSTALLATION

### USING ANACONDA

<p> Download <b>Anaconda </b> Package manager and install it on your operating system distribution. After installation, follow the instructions below by typing the commands in your command prompt inorder to set up your conda environment. </p>

<p> In your project directory, you would see a file called <b>ProjectEnvironment.yaml</b> file. The file contains all the modules and packages needed for building your environment. <br>
Open a command prompt or terminal in the working directory for this project and type the following commands. </p>

- #### CREATE ML ENVIRONMENT

<p>
    Install pyaudio and portaudio for your distribution.
    <ul>
   <li> Install pyaudio here: <a href="https://github.com/jleb/pyaudio"> <b> link </b> </a>  </li>
   <li> Install portaudio here: <a href="https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error"> <b> link </b> </a> </li>
   <li> Other references for installation: <a href="https://gist.github.com/diegopacheco/d5d4507988eff995da297344751b095e"> <b> link </b> </a> </li>
   <li> Using Anaconda to install pyaudio: <a href="https://anaconda.org/anaconda/pyaudio"> <b> Link </b> </a> </li>
   <li> Real Python explanation for speech recognition: <a href="https://realpython.com/python-speech-recognition/"> <b> Link </b> </a></li>
   <li> Pulse Audio access denied: <a href="https://forums.linuxmint.com/viewtopic.php?t=295346"> <b> Link </b> </a></li>
   <li> Installing PulseAudio: <a href="https://core.docs.ubuntu.com/en/stacks/audio/pulseaudio/docs/install-pulseaudio"> <b> Link </b> </a> </li>
   <li> Installing PulseAudio On Ubuntu: <a href="https://linuxhint.com/pulse_audio_sounds_ubuntu/"> <b> Link</b> </a> <a href="https://www.howtoinstall.me/ubuntu/18-04/pulseaudio/"> <b>Link-2</b> </a> </li>
    </ul>
</p>

<p> Linux users, also try installing the following dependencies if you get this error: <br>
    <b> python3: src/hostapi/alsa/pa_linux_alsa.c:3641: PaAlsaStreamComponent_BeginPolling: Assertion `ret == self->nfds' failed. Aborted </b>

<ul>
<li> <b>pa_linux_alsa.c:3636 Assertion ret == self-> ntds' failed: </b> <a href="https://app.assembla.com/spaces/portaudio/tickets/268/details?tab=activity"> <b>Link</b> </a> </li>

<li>  <p> Other Errors Occured could include the following: </p>

<ul>
<li> <b> no sound, Alsa unable to open slave </b> <a href="https://bbs.archlinux.org/viewtopic.php?id=173709"> <b> Link </b> </a> </li>

<li> Installing <b>pulseaudio</b> from the terminal: <a href="https://askubuntu.com/questions/426648/how-to-reinstall-pulseaudio-ubuntu-12-04"> <b> Link </b> </a> </li>

</ul>  

</li>

</ul>

</p>


```console

Andela@team-358:~$ sudo apt-get remove libportaudio2

```


```console

Andela@team-358:~$ sudo apt-get install libasound2-dev

Andela@team-358:~$ git clone -b alsapatch https://github.com/gglockner/portaudio

Andela@team-358:~$ cd portaudio

Andela@team-358:~/portaudio$ ./configure && make

Andela@team-358:~/portaudio$ sudo make install

Andela@team-358:~/portaudio$ sudo ldconfig

Andela@team-358:~/portaudio$ cd ..

```


```console

Andela@team-358:~$ conda env create --file ProjectEnvironment.yaml

```


- #### LIST ALL CONDA ENVIRONMENTS

```console

Andela@team-358:~$ conda env list

Andela@team-358:~$ conda info --envs

```

- #### OUTPUT

```console
base                  *  /home/Andela/anaconda3
ml                       /home/Andela/anaconda3/envs/ml

```


- #### ACTIVATE "(ml)" ENVIRONMENT

```console

Andela@team-358:~$ conda activate ml

```

#### INSTALLING FROM REQUIREMENTS.TXT FILE

```console

(ml)Andela@team-358:~$ pip install -r requirement.txt

```


## RUNNING THE APPLICATION

<p> After setting up your environment and installing the necessary modules and dependencies. Open a terminal
window inside the root directory and execute the <b>"app.py"</b> file using this command  </p>

```console

(ml)Andela@team-358:~$ python app.py  

```

<p> Once executed, you should see the following message displayed below if working properly. </p>

```console

* Serving Flask app "app" (lazy loading)
 * Environment: production
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


```


## AUTHORS/CONTRIBUTING


| Image  | Fullname                                            |
| ------ | --------------------------------------------------- |
| <img src="ANDELADOCS/img1.jpg" width="90px" height="80px" style=" float: left; margin-right: 70px;">  | Mbonu Chinedum (Software Engineer) |
| <img src="ANDELADOCS/img2.jpeg" width="90px" height="80px" style=" float: left; margin-right: 70px;"> | Adetunji Oluwaferanmi (Team-lead) |
| <img src="ANDELADOCS/img3.jpg" width="90px" height="80px" style=" float: left; margin-right: 70px;">  | Ugochukuwu Umeoke  |
| <img src="ANDELADOCS/img4.jpg" width="90px" height="80px" style=" float: left; margin-right: 70px;">  | Abiola Fagbemi |



## ACKNOWLEDGMENTS

<ul>
<li> ANDELA TEAM </li>
<li> Codecademy </li>
<li> Google Build For SDG </li>
</ul>

## REFERENCES

- www.google.com

- https://en.wikipedia.org/wiki/Sound_recognition#:~:text=Sound%20recognition%20is%20a%20technology,feature%20extraction%20and%20classification%20algorithms.
