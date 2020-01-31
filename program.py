import os
import requests


def download_image(image_url, local_path, output_name='temp.jpg'):
    image_local_path = '%s\%s' % (local_path, output_name)
    image = requests.get(image_url).content

    file = open(image_local_path, 'wb')
    file.write(image)
    file.close()

    return image_local_path


def execute_command_line(cwebp_exe, input_image_path, output_image_path, width=0, height=0):
    TEMPLATE_COMMAND = '{0} {1} -q 90 -metadata none {3} -preset picture -o {2}'

    if width > 0 and height > 0:
        command_size = '-resize {0} {1}'.format(width, width)
    elif width > 0 and height <= 0:
        command_size = '-resize {0} {0}'.format(width)
    else:
        command_size = ''

    command = TEMPLATE_COMMAND.format(cwebp_exe, input_image_path, output_image_path, command_size)
    os.system(command)
