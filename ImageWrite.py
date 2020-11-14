from datetime import datetime

from PIL import Image


def scale_image(input_image, name):
    output_image_path = 'static/image/upload_image_users/' + name + '_' + str(
        datetime.now().strftime("%d_%B_%Y")) + '.jpg'
    width = 900
    height = None

    original_image = Image.open(input_image)
    w, h = original_image.size
    # print('\n', 'Размеры изображения на входе: {wide}px ширина x {height}px ' 'высота'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        raise RuntimeError('Ошибка. Превышение временного интервала обработки.')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('Обработанное изображение: {wide}px ширина x {height}px ''высота'.format(wide=width, height=height))

    return output_image_path

# scale_image(input_image='/Users/flame/Downloads/evgeniabrilevskaa_1604768008_1.jpg', name='pic')
# output_image_path='static/image/pillar_scaled.jpg', width=900)
