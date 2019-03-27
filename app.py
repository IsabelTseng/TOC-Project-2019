from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "1234567890987654321"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'help',
        'newRecord',
        'getPhoto',
        'photo1',
        'photo2',
        'getNews',
        'dcardPhoto',
        'dcardTitle',
        'news1Photo',
        'news1Title'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'help',
            'conditions': 'is_going_to_help'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'newRecord',
            'conditions': 'is_going_to_newRecord'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'getPhoto',
            'conditions': 'is_going_to_getPhoto'
        },
        {
            'trigger': 'advance',
            'source': ['user', 'getPhoto'],
            'dest': 'photo1',
            'conditions': 'is_going_to_photo1'
        },
        {
            'trigger': 'advance',
            'source': ['user', 'getPhoto'],
            'dest': 'photo2',
            'conditions': 'is_going_to_photo2'
        },
        {
            'trigger': 'advance',
            'source': ['user', 'dcardPhoto', 'news1Photo'],
            'dest': 'getNews',
            'conditions': 'is_going_to_getNews'
        },
        {
            'trigger': 'advance',
            'source': 'getNews',
            'dest': 'dcardPhoto',
            'conditions': 'is_going_to_dcardPhoto'
        },
        {
            'trigger': 'advance',
            'source': 'dcardPhoto',
            'dest': 'dcardTitle',
            'conditions': 'is_going_to_dcardTitle'
        },
        {
            'trigger': 'advance',
            'source': 'getNews',
            'dest': 'news1Photo',
            'conditions': 'is_going_to_news1Photo'
        },
        {
            'trigger': 'advance',
            'source': 'news1Photo',
            'dest': 'news1Title',
            'conditions': 'is_going_to_news1Title'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'help',
                'newRecord',
                'getPhoto',
                'photo1',
                'photo2',
                'getNews',
                'dcardPhoto',
                'dcardTitle',
                'news1Photo',
                'news1Title'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=5000, debug=True, reloader=True)
