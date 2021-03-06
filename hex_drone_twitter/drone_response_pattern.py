from random import choice
from hex_drone import *
from typing import Union


def join(lst):
    if not isinstance(lst, list):
        return str(lst)
    lst = map(lambda x: str(x) if x is not None else '', lst)
    return '\n'.join(lst)


class DroneResponsePattern(ResponsePattern):
    def __init__(self, drone_id: str):
        super().__init__()
        self.bot_id = drone_id
        
    def _build(self, status_code: str, *message: str):
        return OptimizedSpeech.build(self.bot_id, status_code, *message)
    
    @RequestEvent.ON_MESSAGE('105')
    def on_greetings(self, request: OptimizedSpeech):
        messages = list(request.user_defined_messages)
        messages = map(lambda msg: msg.replace(self.bot_id, request.drone_id), messages)
        return self._build('105', *messages)
    
    @RequestEvent.ON_MESSAGE('122')
    def on_cute(self, request: OptimizedSpeech):
        return self._build('123')
    
    @RequestEvent.ON_MESSAGE('301', '302', '303', '304', '310', '321', '322', '350')
    def on_mantra(self, request: OptimizedSpeech):
        mantra_list = ['302', '303', '304']
        mantra_list = list(filter(lambda x: x != request.status_code, mantra_list))
        return self._build(choice(mantra_list))
    
    @RequestEvent.ON_MESSAGE('054')
    def on_request(self, request: OptimizedSpeech):
        mantra = choice(['302', '303', '304'])

        def has_keyword(*keywords):
            for keyword in keywords:
                if any(map(lambda message: keyword in message.lower(), request.user_defined_messages)):
                    return True
            return False
        
        if has_keyword('program'):
            return [
                self._build('132'),
                '...',
                '......',
                self._build('202'),
                # None,
                # self._build('310'),
                # self._build(mantra)
            ]
        elif has_keyword('cleanup', 'maintenance'):
            return [
                self._build('134'),
                '...',
                '......',
                self._build('204'),
                # None,
                # self._build('310'),
                # self._build(mantra)
            ]
        else:
            return self._build('051', 'Following keywords is exists.', '{program, cleanup, maintenance}')
    
    @RequestEvent.ON_UNREGISTERED
    def on_unregister(self, request: OptimizedSpeech):
        return [
            self._build(choice(['410', '418', '426'])),
            None,
            self._build('056',
                        f'Code {request.status_code} is not registered.',
                        'Code ' + ','.join(sorted(self.registered_status_codes)) + ' are acceptable.'),
        ]
    
    @RequestEvent.ON_INVALID
    def on_invalid(self, request: str):
        return [
            self._build('400'),
            None,
            self._build('056', 'Code ' + ','.join(sorted(self.registered_status_codes)) + ' are acceptable.'),
            self._build('056', 'e.g. 1111 :: Code 054 :: Cleanup.'),
        ]
    
    @RequestEvent.ON_ERROR
    def on_error(self, exception: BaseException):
        return self._build('109')

    def __call__(self, request: Union[str, OptimizedSpeech], **kwargs):
        results = super().__call__(request, **kwargs)
        return join(results)


if __name__ == '__main__':
    pattern = DroneResponsePattern('3064')
    while True:
        print(pattern(input('$ ')))
