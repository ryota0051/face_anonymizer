import cv2
import numpy as np


def mosaic(img: np.ndarray, ratio: float = 0.5) -> np.ndarray:
    '''画像にモザイク処理を施す

    Parameters
    ----------
    img : np.ndarray
        対象画像
    ratio: float
        縮小倍率

    Returns
    -------
    np.ndarray
        モザイク処理を施した画像
    '''
    h, w = img.shape[:2]
    img = cv2.resize(img, None, fx=ratio, fy=ratio)
    img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
    return img


def paint_black(img: np.ndarray) -> np.ndarray:
    '''画像と同じサイズの黒画像を返す

    Parameters
    ----------
    img : np.ndarray
        入力画像

    Returns
    -------
    np.ndarray
        黒塗りされた画像
    '''
    return np.zeros_like(img)
