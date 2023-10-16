import numpy as np

# def rgb2hsv(rgb):
#     rgb = rgb.astype('float')
#     maxv = np.amax(rgb, axis=2)
#     maxc = np.argmax(rgb, axis=2)
#     minv = np.amin(rgb, axis=2)
#     minc = np.argmin(rgb, axis=2)

#     hsv = np.zeros(rgb.shape, dtype='float')
#     hsv[maxc == minc, 0] = np.zeros(hsv[maxc == minc, 0].shape)
#     hsv[maxc == 0, 0] = (((rgb[..., 1] - rgb[..., 2]) * 60.0 / (maxv - minv + np.spacing(1))) % 360.0)[maxc == 0]
#     hsv[maxc == 1, 0] = (((rgb[..., 2] - rgb[..., 0]) * 60.0 / (maxv - minv + np.spacing(1))) + 120.0)[maxc == 1]
#     hsv[maxc == 2, 0] = (((rgb[..., 0] - rgb[..., 1]) * 60.0 / (maxv - minv + np.spacing(1))) + 240.0)[maxc == 2]
#     hsv[maxv == 0, 1] = np.zeros(hsv[maxv == 0, 1].shape)
#     hsv[maxv != 0, 1] = (1 - minv / (maxv + np.spacing(1)))[maxv != 0]
#     hsv[..., 2] = maxv

#     return hsv

# def hsv2rgb(hsv):
 
#     hi = np.floor(hsv[..., 0] / 60.0) % 6
#     hi = hi.astype('uint8')
#     v = hsv[..., 2].astype('float')
#     f = (hsv[..., 0] / 60.0) - np.floor(hsv[..., 0] / 60.0)
#     p = v * (1.0 - hsv[..., 1])
#     q = v * (1.0 - (f * hsv[..., 1]))
#     t = v * (1.0 - ((1.0 - f) * hsv[..., 1]))

#     rgb = np.zeros(hsv.shape)
#     rgb[hi == 0, :] = np.dstack((v, t, p))[hi == 0, :]
#     rgb[hi == 1, :] = np.dstack((q, v, p))[hi == 1, :]
#     rgb[hi == 2, :] = np.dstack((p, v, t))[hi == 2, :]
#     rgb[hi == 3, :] = np.dstack((p, q, v))[hi == 3, :]
#     rgb[hi == 4, :] = np.dstack((t, p, v))[hi == 4, :]
#     rgb[hi == 5, :] = np.dstack((v, p, q))[hi == 5, :]

#     return rgb


def rgb2hsv(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    intensity = (r + g + b) / 3

    if r == g == b:
        saturation = 0
    else:
        min_color = min(r, g, b)
        saturation = 1 - min_color / intensity

    return (r,g,b), saturation, intensity

def hsv2rgb(intensity, saturation, hsi):
    r, g, b = hsi
    if saturation == 0:
        return (int(intensity * 255), int(intensity * 255), int(intensity * 255))
    else:
        hue = np.arccos(0.5 * ((r - g) + (r - b)) / np.sqrt((r - g)**2 + (r - b) * (g - b)))
        if b > g:
            hue = 2 * np.pi - hue
        hue = hue * 180 / np.pi

        intensity = intensity * 255
        saturation = saturation * 255

        while hue < 0:
            hue += 360
        while hue > 360:
            hue -= 360

        if 0 <= hue < 120:
            r = intensity * (1 + (saturation * np.cos(hue)) / (np.cos(60 - hue) - np.cos(hue - 60)))
            b = intensity * (1 - saturation)
            g = 3 * intensity - (r + b)
        elif 120 <= hue < 240:
            hue = hue - 120
            g = intensity * (1 + (saturation * np.cos(hue)) / (np.cos(60 - hue) - np.cos(hue - 60)))
            r = intensity * (1 - saturation)
            b = 3 * intensity - (r + g)
        else:
            hue = hue - 240
            b = intensity * (1 + (saturation * np.cos(hue)) / (np.cos(60 - hue) - np.cos(hue - 60)))
            g = intensity * (1 - saturation)
            r = 3 * intensity - (r + g)

        return (int(r), int(g), int(b))