import subprocess
import datetime
import time

base_url = 'https://webcams.borealisbroadband.net'
images = [
    'potterws/potterwsmega',
    'hilton/hilton2mega',
    'searsmall/searsmall1280',
    'glennweb/glennws-mega',
    'shipcreek/shipcreekmega',
    'fourthavenue/4thandd1280',
    'alaskacam/alaskacammega'
]

save_dir = 'images'
subprocess.run(f'mkdir {save_dir}', shell=True)

while True:
    for img in images:
        try:
            timestamp = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
            fname = img.split('/')[0]
            savepath = f'{save_dir}/{fname}_{timestamp}.jpg'
            subprocess.run(f'curl {base_url}/{img}.jpg -o {savepath}', shell=True)
        except Exception as e:
            print(img)
            print(e)
            print()
        finally:
            time.sleep(10)

    time.sleep(60 * 60)
