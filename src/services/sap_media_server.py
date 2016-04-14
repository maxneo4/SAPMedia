import os
import sap_media_api
from max_dev import root_path


if __name__ == '__main__':
    root_path.set_root_path_from(__file__)
    port = int(os.environ.get('PORT', 5232))
    sap_media_api.app.run(host='127.0.0.1', port=port)