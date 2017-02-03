#!flask/bin/python
from datetime import datetime

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import subprocess
import sensehat


app = Flask(__name__)
api = Api(app)


actions = {
    'action1': {
        '_id': 1, 
        'action': 'sensehat',
        'time': datetime.now().strftime('%H:%M:%S'), 
        'result': True
    },
    'action2':{
        'id': 2, 
        'action': 'IR',
        'time':datetime.now().strftime('%H:%M:%S'),
        'result': True
    }
}

def abort_if_action_not_exist(actionId):
    if actionId not in actions:
        abort(404, message="Action {} doesn't exist".format(actionId))

parser = reqparse.RequestParser()
parser.add_argument('action')
parser.add_argument('actiontype')

class Action(Resource):
    def get(self, actionId):
        abort_if_action_not_exist(actionId)
        return actions[actionId]

    def delete(self, actionId):
        abort_if_action_not_exist(actionId)
        del actions[actionId]
        return '', 204

    def put(self, actionId):
        args = parser.parse_args()
        action = {'action': args['action']}
        actions[actionId] = action
        return action, 201
    

class ActionList(Resource):
    def get(self):
        return actions

    def post(self):
        args = parser.parse_args()
        actionId = int(max(actions.keys()).lstrip('action')) + 1
        actionId = 'action%i' % actionId
        actions[actionId] = {'action': args['action']}
        return actions[actionId], 201


class Perform(Resource):
    def get(self):
        args = parser.parse_args()
        if args['action'] == "sensehat":   
            return sensehat.demo()
        elif args['action'] == "kef": 
            if args['actiontype']:
                subprocess.check_output(["irsend SEND_ONCE kef " + args['actiontype']], shell=True)
                return args['actiontype'] + " is triggered."
        elif args['action'] == "dyson": 
            if args['actiontype']:
                subprocess.check_output(["irsend SEND_ONCE dyson " + args['actiontype']], shell=True)
                return args['actiontype'] + " is triggered."
        else:
             abort(404, message="Action is not recognized - Usage example= http://pi.kaiching.net:8080/perform?action=dyson&actiontype=KEY_POWER") 
    def post(self):
        args = parser.parse_args()
        if args['action'] == "sensehat":            
            return sensehat.demo()
        abort(404, message="Action is not recognized") 



api.add_resource(ActionList, '/actionlist')
api.add_resource(Action, '/action/<actionId>')
api.add_resource(Perform, '/perform')

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=8080)
