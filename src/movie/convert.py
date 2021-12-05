import cv2

from typing import Callable
from src.detector.face import FaceDetectorBase


class MovieToAnonymizedMovie:

    def __init__(self, anonymizer: Callable,
                 face_detector: FaceDetectorBase):
        self.anonymizer = anonymizer
        self.face_detector = face_detector

    def convert(self, src: str, dst: str):
        '''動画中の顔を検出して匿名化し、保存するメソッド

        Parameters
        ----------
        src: str
            入力動画パス

        dst: str
            変換後の動画出力パス
        '''
        capture = cv2.VideoCapture(src)
        if not capture.isOpened():
            print('Video could not open')
            exit(-1)
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        fps = int(capture.get(cv2.CAP_PROP_FPS))
        num_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        # 保存用writer作成
        fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        writer = cv2.VideoWriter(dst, fmt, fps, (width, height))
        frame_count = 0
        while True:
            ret, frame = capture.read()
            if ret:
                boxes = self.face_detector.detect(frame)
                for box in boxes:
                    start_x, start_y, end_x, end_y = box
                    frame[start_y:end_y, start_x:end_x] = \
                        self.anonymizer(frame[start_y:end_y, start_x:end_x])
                writer.write(frame)
                frame_count += 1
                if frame_count % 10 == 0:
                    print(f'{frame_count} / {num_frames}')
            else:
                break
        print(f'{frame_count} / {num_frames}')
        writer.release()
        capture.release()
