from typing import List

import cv2
import numpy as np
import face_detection

from src.inference import lite_retina_face


class FaceDetectorBase:
    def detect(self, img: np.ndarray) -> List[List[int]]:
        pass


class FaceDetectorRetinaFace(FaceDetectorBase):
    def __init__(self, th: float = 0.5):
        self.model = face_detection.build_detector(
            'RetinaNetMobileNetV1',
            confidence_threshold=th,
        )

    def detect(self, img: np.ndarray) -> List[List[int]]:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.model.detect(img_rgb)
        return np.abs(results[:, :4].astype('int')).tolist()


class FaceDetectorLiteRetinaFace(FaceDetectorBase):
    def __init__(self, onnx_path: str, th: float = 0.7):
        self.net = cv2.dnn.readNetFromONNX(onnx_path)
        self.th = th

    def detect(self, img: np.ndarray) -> List[List[int]]:
        return lite_retina_face.inference(
            net=self.net,
            img=img,
            th=self.th
        )
