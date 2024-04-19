# Worldclass Camera with ros2
opencv와 ros2를 활용하여 카메라 패키지를 구현해보자

![20240419_144907](https://github.com/IMddubin/Worldclass-Camera-ROS2/assets/103230856/acb35ecb-ff50-4730-acb0-ded4a9e9852e)

## 1. 프로젝트 환경
OS : Ubuntu 22.04 LTS
ROS2 : humble
need webcam

## 2. 환경 설정

- workspace 생성
  ```
  mkdir -p ~/<workspace_name>/src
  ```

- git clone & colcon build
  ```
  cd ~/<workspace_name>/src
  git clone https://github.com/IMddubin/Worldclass-Camera-ROS2.git
  ```
  
- install packages
  ```
    cd ../
    pip install -r requirements.txt
  ```

- build
  ```
  colcon build
  ```

## 3. 카메라 실행

- launch camera.launch.py : 카메라 frame을 publish 합니다.
  ```
  ros2 launch world_class_cam camera.launch.py
  ```
  
- 카메라 영상보기
  ```
  rqt
  ```

  좌측 상단 Plugins > Visualization > Image View click

  
  
  
## 4. 사진 저장

**3. 카메라 실행을 하여 동작하고 있어야 합니다.**

- service call : 이미지를 저장힙니다. (경로 : /home/your_pc/workspace_name/src/world_class_cam/world_class_cam/album/)
  ```
    ros2 service call /capture_image world_class_msg/srv/CaptureImage
  ```

## 5. 녹화 기능

**3. 카메라 실행을 하여 동작하고 있어야 합니다.**

- service call : 녹화를 시작합니다.
  
  ```
    ros2 service call /record_start world_class_msg/srv/RecordStart "{start: True, filename: subin}"
  ```

- service call : 녹화를 종료하고 저장을 합니다. (경로 : /home/your_pc/workspace_name/src/world_class_cam/world_class_cam/album/)
  ```
    ros2 service call /record_start world_class_msg/srv/RecordStart "{start: False, filename: subin}"
  ```
  
