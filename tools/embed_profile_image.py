from pathlib import Path

IMAGE_B64 = 'PLACEHOLDER'

html_path = Path('app/src/main/assets/index.html')
html = html_path.read_text(encoding='utf-8')
data_uri = 'data:image/jpeg;base64,' + IMAGE_B64
html = html.replace('src="coach_icon.jpg"', 'src="' + data_uri + '"')
html_path.write_text(html, encoding='utf-8')
print('Embedded Abu Ramz profile image into the app HTML.')
