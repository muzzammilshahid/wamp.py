from wampproto import auth, serializers

from wamp import wsjoiner, session


class Client:
    def __init__(
        self,
        authenticator: auth.IClientAuthenticator,
        serializer: serializers.Serializer = serializers.JSONSerializer(),
    ):
        self._authenticator = authenticator
        self._serializer = serializer

    def connect(self, url: str, realm: str) -> session.Session:
        j = wsjoiner.WAMPSessionJoiner(self._authenticator, self._serializer)
        details = j.join(url, realm)

        return session.Session(details)
