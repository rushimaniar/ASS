# Automated Surveillance System
This is our final year project. <br>
Dated `12th April, 2018`, I declare it to have completed. <br>

The aim of this project is to review surveillance video feeds and based on that determine if the activities going on in the video are anomalous or normal.<br>
This project is specialized towards Hotels but the underlying core framework can be used in any environment. <br>

The following phases are involved in its working:
- Break video into frames
- Gain semantic data of each frame
- Pass this data through rules in the Rule Engine
- Determine if activivies are abnormal or regular.

# Usage
> main.py --video path/to/feed --rules <rules> --camera <camera_name> --debug-levels <A,D,R,C>
Additionally, the `--list` arguement can be used to list all the available rules.

# Dependencies
This project depends on the following:
- CUDA
- OpenCV
- feh
- YOLOv3

# Disclaimer
Yeh project me bahut zyada jhol hai.<br>
If you are a junior, you may feel free to use this project in any sense you deem useful. <br>
I also urge you to try for a challenging problem defination as your final year project because, you will learn one of these two things very well: You will either learn a new technology or you will learn (really well) how to work around something. <br>
This project is **full** of hacks everywhere, but they're put together well for something that was made in under a week. Don't do that. Or do it if you like the fun. <br>
I am just happy I am done with this :) <br>

**Goodbye**