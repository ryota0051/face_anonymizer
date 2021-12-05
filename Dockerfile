FROM python:3.8.12-slim

RUN apt update && apt upgrade -y && \
    apt install -y libopencv-dev

WORKDIR /face_anonymizer

COPY ./requirements.txt /face_anonymizer

RUN pip install --upgrade pip && pip install -r requirements.txt

# 使用するモデルをdocker imageに含めるために実行
RUN python -c "import face_detection; face_detection.build_detector('RetinaNetMobileNetV1')"

COPY . ./
