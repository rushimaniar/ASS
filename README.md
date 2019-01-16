# Automated Surveillance System
This is our final year project. <br>
Dated `12th April, 2018`, I declare it to have completed. It will not be developed or supported any longer by me.<br>

The aim of this project is to review surveillance video feeds and based on that determine if the activities going on in the video are anomalous or normal.<br>
This project is specialized towards Hotels but the underlying core framework can be used in any environment. <br>

The following phases are involved in its working:
- Break video into frames
- Gain semantic data of each frame
- Pass this data through rules in the Rule Engine
- Determine if activivies are abnormal or regular.

# Usage
```main.py --video path/to/feed --rules <rules> --camera <camera_name> --debug-levels <A,D,R,C>```
<br>
Additionally, the `--list` arguement can be used to list all the available rules.

# Dependencies
This project depends on the following:
- CUDA
- OpenCV
- feh
- YOLOv3
