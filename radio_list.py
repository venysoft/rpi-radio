class radio:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
radios = []
radios.append(radio("cerna_hora", "https://playerservices.streamtheworld.com/api/livestream-redirect/HITRADIO_CERNAHORA_128.mp3"))
radios.append(radio("evropa2", "http://ice.actve.net/fm-evropa2-128"))
radios.append(radio("frekvence1", "http://ice.actve.net/fm-frekvence1-128"))
radios.append(radio("Rocková zábava","https://ice.abradio.cz/rockzabava128.mp3"))
