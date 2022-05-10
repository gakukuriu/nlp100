import pymongo
from flask import Flask, render_template, request, Markup

client = pymongo.MongoClient('localhost', 27017)
db = client.artist_db
co = db.artist

def templateGen(data):
    name = 'アーティスト名：'
    area = '活動場所：'
    aliases = '別名：'
    start = '活動開始日：'
    end = '活動終了日：'
    tags = 'タグ：'
    if 'name' in data:
        name += data['name']
    if 'area' in data:
        area += data['area']
    if 'aliases' in data:
        for i in range(len(data['aliases'])):
            aliases += data['aliases'][i]['name']
            if i != len(data['aliases'])-1:
                aliases += '/'
    if 'begin' in data:
        if 'year' in data['begin']:
            start += str(data['begin']['year']) + '年'
        if 'month' in data['begin']:
            start += str(data['begin']['month']) + '月'
        if 'date' in data['begin']:
            start += str(data['begin']['date']) + '日'
    if 'end' in data:
        if 'year' in data['end']:
            end += str(data['end']['year']) + '年'
        if 'month' in data['end']:
            end += str(data['end']['month']) + '月'
        if 'date' in data['end']:
            end += str(data['end']['date']) + '日'
    if 'tags' in data:
        for i in range(len(data['tags'])):
            tags += data['tags'][i]['value']
            if i != len(data['tags'])-1:
                tags += ', '
    return(name + '<br>' + area + '<br>' + aliases + '<br>' + start + '<br>' + end + '<br>' + tags + '<br><br>')


app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form['name']
        aliase = request.form['aliase']
        tag = request.form['tag']
        area = request.form['area']
        key = {}
        if name != '':
            key['name'] = name
        if aliase != '':
            key['aliases.name'] = aliase
        if tag != '':
            key['tags.value'] = tag
        if area != '':
            key['area'] = area
        temp = ''
        for data in co.find(key).sort('rating.count', pymongo.DESCENDING):
            temp += templateGen(data)
        return(render_template('index.html', answer=Markup(temp)))

if __name__ == '__main__':
    app.run()
