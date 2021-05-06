from flask import Blueprint, request
from appReWate.appservice import parse_service
import threading
from appReWate.utils import file_tool
import manage

appReWater_bp = Blueprint('water', __name__)


@appReWater_bp.route("/link")
def link():
    re_water_path = manage.app.config.get("RE_WATER_PATH")
    url = request.args.get('url')  # 获取链接
    print(url)
    if url:
        # 识别链接并下载#返回文件名
        file_name = parse_service.link_check(url, re_water_path)
        if file_name:
            path = re_water_path + file_name
            t1 = threading.Thread(target=file_tool.remove_file, args=(path, 30))
            t1.start()
            return file_name
        else:
            return 'error'
    else:
        return "参数无效"
