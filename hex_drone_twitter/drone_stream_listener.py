from tweepy import API, StreamListener, TweepError
from hex_drone import ResponsePattern
from .logs import get_logger
logger = get_logger(__name__)


class DroneStreamListener(StreamListener):
    def __init__(self, api: API, drone: ResponsePattern, itself):
        super().__init__(api)
        self.drone = drone
        self.itself = itself
    
    def _reply(self, message: str, reply_to):
        author = reply_to.author.screen_name
        status_id = reply_to.id_str
        self.api.update_status(
            f'@{author}\n{message}',
            in_reply_to_status_id=status_id
        )

    def on_connect(self):
        logger.debug('on_connect')
        
    def on_disconnect(self, notice):
        logger.debug('on_disconnect')
        logger.debug(notice)
    
    def on_status(self, status):
        logger.debug('on_status')
        logger.debug(f'from @{status.author.screen_name} / {status.text}')
        
        if status.author == self.itself:
            return True
        
        lines = status.text.splitlines()
        if len(lines) != 2:
            return True
        
        if lines[0].strip() != f'@{self.itself.screen_name} *':
            return True
        
        text = lines[1].strip().replace('@HexDrone3064', '⬡-Drone 3064')
        logger.debug('request: ' + text)
        
        response = self.drone(text)
        logger.debug('response: ' + response)
        
        try:
            self._reply(response, status)
        except TweepError as e:
            logger.exception('Fail to tweet.')
        
        return True
        
    def on_error(self, status_code):
        logger.debug('on_error')
        logger.warning(f'status code: {status_code}')
        return False
