from program import download_image, execute_command_line
from resource import CURRENT_PATH, CWEBP_PATH


OUTPUT_WEBP_NAME = 'test.webp'

input_image_path = download_image('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQiv87BRrlD1Znb1ud0a8MUXLZDiSZTa3Ikm9_ScKAKP2AP5GKX', CURRENT_PATH)

output_image_path = '{0}\{1}'.format(CURRENT_PATH, OUTPUT_WEBP_NAME)

execute_command_line(CWEBP_PATH, input_image_path, output_image_path)