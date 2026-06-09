from flask import Flask, send_file, abort, Response
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
from time import sleep
import cfg

app = Flask(__name__)

def create_tile_img(zoom, x, y, fmt):
    img = Image.new('RGB', (256,256), 'white')
    draw = ImageDraw.Draw(img)
    draw.rectangle((0,0, 255,255), fill='AliceBlue', outline='CornflowerBlue')
    
    txt = f'zoom={zoom}\nx={x}\ny={y}\n\nformat={fmt}\n'
    #font = ImageFont.load_default()
    font = ImageFont.truetype("/app/FreeMonoBold.ttf", 20)
    # Use textbbox to find dimensions of the text
    _, _, tw, th = draw.textbbox((0, 0), txt, font=font)
    draw.text(((256-tw)/2, (256-th)/2), text=txt, fill='CornflowerBlue', font=font)
    #draw.text((256/2, 256/2), txt, font=font, anchor="mm")
    
    
    img_io = BytesIO()
    if fmt == 'jpeg':
        img.save(img_io, 'JPEG', quality=70)
    else:
        img.save(img_io, fmt.upper())
        
    img_io.seek(0)
    return img_io

@app.route('/tile/<int:zoom>/<int:x>/<int:y>')
def get_tile(zoom, x, y):
    #return f'zoom={zoom} x={x} y={y}'
    
    if random.randrange(cfg.ERR_CHANCE) == 0: # имитация ошибок сервера
        abort(500, 'Something goes wrong. Sorry :(')
        
    if random.randrange(cfg.ERR_CHANCE) == 0: # имитация возврата некорректных данных
        return 'this is NOT image data!!!'
    
    if random.randrange(cfg.ERR_CHANCE) == 0: # имитация возврата некорректных данных №2
    #if True:
        return Response('this is NOT image data!!!', mimetype='image/jpeg')
    
    fmt = random.choice (cfg.FORMATS)
    print(f'img. format={fmt}')
    sleep(cfg.RESP_DELAY_SEC)
    return send_file(create_tile_img(zoom, x, y, fmt), mimetype='image/'+fmt)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
