from config.env_config import db
from sqlalchemy_serializer import SerializerMixin


class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movie'

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='电影名称')
    desc = db.Column(db.Text, nullable=False, info='电影描述')
    classify = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='类别')
    actor = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='主演')
    director = db.Column(db.String(500), nullable=False, server_default=db.FetchedValue(), info='导演')
    cover_pic = db.Column(db.String(300), nullable=False, server_default=db.FetchedValue(), info='封面图')
    pics = db.Column(db.String(1000), nullable=False, server_default=db.FetchedValue(), info='图片地址')
    magnet_url = db.Column(db.String(5000), nullable=False, server_default=db.FetchedValue(), info='磁力下载地址')
    online__url = db.Column('online _url', db.String(5000), nullable=False, server_default=db.FetchedValue(),
                            info='在线播放地址')
    pub_date = db.Column(db.BigInteger, nullable=False, index=True, info='发布日期')
    rating = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='评分')
    source = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='来源')
    visits = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='阅读数')
    is_recommend = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否推荐，0不推荐，1推荐')
    update_at = db.Column(db.BigInteger, nullable=False)
    create_at = db.Column(db.BigInteger, nullable=False)

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self, key, items[key])

    def columns_to_dict(self):
        dict_ = {}
        for key in self.__mapper__.c.keys():
            dict_[key] = getattr(self, key)
        return dict_
