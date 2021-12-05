import os
import argparse

from src.detector.face import FaceDetectorRetinaFace
from src.movie.anonymizer import paint_black
from src.movie.convert import MovieToAnonymizedMovie


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--src',
        default='test1.mp4',
        help='inputディレクトリ内の動画ファイル名'
    )
    parser.add_argument('--model', default='RetinaFace', help='使用するモデル')
    parser.add_argument('--th', default=0.5, help='検出しきい値', type=float)
    return parser.parse_args()


def main():
    args = get_args()
    face_detector = None
    if args.model == 'RetinaFace':
        face_detector = FaceDetectorRetinaFace(th=args.th)
    if face_detector is None:
        print(f'{args.model}は使用できません')

    src = f'./input/{args.src}'
    dst = f'./output/result_{os.path.basename(src)}'
    if not os.path.exists(src):
        print(f'{src}が存在しません')
        exit(-1)

    convertor = MovieToAnonymizedMovie(
        anonymizer=paint_black,
        face_detector=face_detector
    )
    convertor.convert(src, dst)
    print(f'{dst}に結果を出力しました。')


if __name__ == '__main__':
    main()
