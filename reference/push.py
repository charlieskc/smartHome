import requests



data=dict(title='Title', body='Body', type='note')
requests.post('https://api.pushbullet.com/v2/pushes', auth=('o.ZBNInHoENd94UjTsedyvn6O1QGml0tPA',''), data=data)


