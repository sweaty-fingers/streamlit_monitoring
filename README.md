# 전체 과정 실행
```bash
python run_expriment.py
```


# 환경
- Windows OS
- python version 3.12.4

make virtualenv 맥이나 리눅스라면 pyenv 추천

```bash
python -m venv venv
or 
py -3 -m venv venv
```

```bash
# 가상환경 실행
venv\Scripts\activate

# 필요 라이브러리 설치
pip install -r requirements.txt
```

# 실행 예시

Device에서 프로그램(segmentation)이 실행되고 있으며 일정 시간간격으로 서버에 데이터를 전달하는 상황 시뮬레이션 코드
```cmd
# 실제 카메라 영상이 윈도우로 뜸
python runnning_code\capture_images_with_window.py 

# 백그라운드에서만 실행
python running_code\capture_images.py 
```

디바이스로부터 서버에 들어온 데이터 처리
```cmd
python running_code\make_log.py
```

대시보드 실행
```cmd
streamlit run dashboard/app.py
```

requirements.txt 생성
```cmd
pip install pipreqs

pipreqs {directory}
# or for window
pipreqs --encoding=utf8 {directory}
```

# 재학습 데이터셋
현재 노트북 환경에서 영상부터 모든 것을 실행하기에 무리가 있음으로 VOC 데이터셋 제외 CUSTOM 데이터 셋으로면 훈련.
VOC 통합 데이터를 사용하려 한다면

retraining/training/ 디렉터리에서 traininng_concated.py 파일을 training.py로 이름 바꾸기
