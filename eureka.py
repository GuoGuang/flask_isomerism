import py_eureka_client.eureka_client as eureka_client

"""
register to eureka
"""
def setEureka():
    server_host = "localhost"
    server_port = 9004
    eureka_client.init(eureka_server="http://localhost:5000/eureka",
                       app_name="service-movie",
                       # 当前组件的主机名，可选参数，如果不填写会自动计算一个，如果服务和 eureka 服务器部署在同一台机器，请必须填写，否则会计算出 127.0.0.1
                       instance_host=server_host,
                       instance_port=server_port,
                       # 调用其他服务时的高可用策略，可选，默认为随机
                       ha_strategy=eureka_client.HA_STRATEGY_RANDOM)


setEureka()
