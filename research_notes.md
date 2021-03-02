# Research Notes
Find here interesting links and resources for ML libraries and CNN for image rcognition!

General Notes:
- We don't give a damn about inference. All in for predictability.
- Tensorflow seems to be the biggest hit and I'm willing to focus in on this one due to its ease of use for working with **deep neural networks**, image classification, GPU acceleration capabilities, and the ability to run code in Google collab which is fantastic for collaborative coding [(it's like Google docs for code)](https://www.youtube.com/watch?v=iGWbqhdjf2s&ab_channel=ComputerScience). You can also use Keras on top of Tensorflow seamlessly for any reason we may need.
  - [5min tensorflow demo](https://www.youtube.com/watch?v=QfNvhPx5Px8&ab_channel=SirajRaval)
  - There are like millions of tutorial videos so just go out there and browse a bit.


Available Libraries (Python):
- Tensorflow (my choice ~ Luka)
  -  Core task is building deep learning models
  -  Image, Text, and Speech recognition
  -  Effortless collaboration of ideas and code (available in google collab because TF was developed by Google)
  -  GPU accelerated training (I spent a lot of money on a beast GPU [RTX 2070 super]. We should definitely take advantage of this for reducing our training times)
- Keras
  - [Cheatsheet to see available functions](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Keras_Cheat_Sheet_Python.pdf) 
- Scikit-learn
  -  Develped for modelling but I think it's mostly non CNN models.
  -  Can use random tree classifiers for labeled images. [Short Tutorial](https://www.youtube.com/watch?v=PO4hePKWIGQ&ab_channel=PyRevolution) but we want to implement CNNs
- Pytorch
  - Tensor computing with GPU acceleration
  - Easy to learn, use and integrate with the rest of the Python ecosystem
  - Very customizable, widely used in deep learning research (maybe too much for us to learn)
  - Not optimized for speed
