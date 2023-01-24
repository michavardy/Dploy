import toml


class Connector:
    def __init__(self):
        self.load_DployConfig()

    def load_DployConfig(self):
        with open('DployConfig.toml', 'r') as conf:
            self.config = toml.loads(conf.read())

if __name__=="__main__":
    con = Connector()
    print(con.config)
